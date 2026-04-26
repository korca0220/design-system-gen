#!/usr/bin/env python3
"""
스크린 명세 .md 파일 자동 검증.

검증 항목 (validation_checklist.md):
- frontmatter 파싱 가능 (yaml 유효)
- frontmatter `extends` 가 디자인 시스템 디렉토리에 존재
- 모든 `↳ component: <path>` 참조가 실제 파일 존재
- color/spacing/radius/text/motion/shadow 토큰이 베이스 DS foundations에 존재
- Bindings 섹션에 raw hex (#xxxxxx) 또는 raw px (Npx) 없음 (코드 블록 / Custom 슬롯 제외)

사용:
  python3 validate_screen.py <screen.md>
  python3 validate_screen.py <screens/{project}/>           # 디렉토리면 전체 검증
  python3 validate_screen.py --repo-root <path> <target>    # 레포 루트 명시 (기본: 자동 탐지)

종료 코드:
  0 — 모두 통과
  1 — 하나 이상 실패
  2 — 사용 오류
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path


def find_repo_root(start: Path) -> Path:
    """git root를 찾거나 design-systems/ 디렉토리가 있는 곳을 root로."""
    p = start.resolve()
    for ancestor in [p] + list(p.parents):
        if (ancestor / ".git").exists() or (ancestor / "design-systems").is_dir():
            return ancestor
    return p


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """간단한 YAML frontmatter 파서. yaml 라이브러리 의존성 회피."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    yaml_block = text[3:end].strip()
    body = text[end + 4:].lstrip()

    fm: dict = {}
    stack: list[tuple[int, dict]] = [(0, fm)]
    for raw in yaml_block.splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        # indent
        stripped = raw.lstrip(" ")
        indent = len(raw) - len(stripped)
        # pop deeper levels
        while stack and stack[-1][0] >= indent and len(stack) > 1:
            stack.pop()
        # key: value 또는 key:
        if ":" not in stripped:
            continue
        key, _, val = stripped.partition(":")
        key = key.strip()
        val = val.strip()
        # remove quotes
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        # array literal
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            stack[-1][1][key] = [s.strip().strip('"').strip("'") for s in inner.split(",") if s.strip()]
            continue
        if val == "":
            new_dict: dict = {}
            stack[-1][1][key] = new_dict
            stack.append((indent + 2, new_dict))
        else:
            stack[-1][1][key] = val
    return fm, body


def split_sections(body: str) -> dict[str, str]:
    """## 헤더 기준으로 섹션 분리."""
    sections: dict[str, str] = {}
    current = "_preamble"
    buf: list[str] = []
    for line in body.splitlines():
        m = re.match(r"^## +(\d+\.\s+)?(.+?)(?:\s*\(.*\))?\s*$", line)
        if m:
            sections[current] = "\n".join(buf)
            current = m.group(2).strip()
            buf = []
        else:
            buf.append(line)
    sections[current] = "\n".join(buf)
    return sections


def strip_code_blocks(text: str) -> str:
    """``` 코드 블록 제거 (안의 raw 값은 분석 제외)."""
    return re.sub(r"```[\s\S]*?```", "", text)


def strip_custom_slots(text: str) -> str:
    """`<Custom name="...">` 마커 안의 인라인 표기 제거 (간단히 마커만 제거)."""
    return re.sub(r"<Custom[^>]*>", "", text)


def find_component_refs(body: str, repo_root: Path) -> list[tuple[str, bool]]:
    """↳ component: <path> 또는 ref: `<path>` 형태에서 component 경로 추출."""
    refs: set[str] = set()
    # ↳ component: design-systems/.../components/NN-name.md
    for m in re.finditer(r"↳\s*component:\s*([\w/\-.]+\.md)", body):
        refs.add(m.group(1))
    # ref: `design-systems/.../components/NN-name.md`
    for m in re.finditer(r"ref:\s*`([\w/\-.]+\.md)`", body):
        refs.add(m.group(1))
    results: list[tuple[str, bool]] = []
    for ref in sorted(refs):
        results.append((ref, (repo_root / ref).is_file()))
    return results


TOKEN_RE = re.compile(r"`((?:color|spacing|radius|text|motion|shadow|font|atomic|opacity)/[\w/\-.]+)`")


def find_token_refs(body: str) -> list[str]:
    refs: set[str] = set()
    for m in TOKEN_RE.finditer(body):
        refs.add(m.group(1))
    return sorted(refs)


def token_exists_in_ds(token: str, ds_root: Path) -> bool:
    """토큰이 베이스 DS foundations 또는 components 본문에 등장하는지 (간이 텍스트 매칭)."""
    target = f"`{token}`"
    foundations = ds_root / "foundations"
    if foundations.is_dir():
        for f in foundations.glob("*.md"):
            try:
                if target in f.read_text(encoding="utf-8"):
                    return True
            except OSError:
                pass
    return False


HEX_RE = re.compile(r"#[0-9a-fA-F]{6}\b")
PX_RE = re.compile(r"\b\d+(?:\.\d+)?px\b")


def find_raw_values_in_bindings(sections: dict[str, str]) -> tuple[list[str], list[str]]:
    """Bindings 섹션 본문(코드블록/Custom 마커 제외)에서 raw hex/px 추출."""
    bindings = ""
    for name, text in sections.items():
        if "Bindings" in name or "구체값" in name:
            bindings += text + "\n"
    if not bindings:
        return [], []
    cleaned = strip_code_blocks(bindings)
    cleaned = strip_custom_slots(cleaned)
    hexes = HEX_RE.findall(cleaned)
    pxs = PX_RE.findall(cleaned)
    return hexes, pxs


def validate_screen(path: Path, repo_root: Path) -> tuple[bool, list[str]]:
    """단일 스크린 검증. 반환: (전체 통과?, 메시지 목록)"""
    msgs: list[str] = []
    text = path.read_text(encoding="utf-8")

    # 1. frontmatter
    fm, body = parse_frontmatter(text)
    if not fm:
        msgs.append("❌ frontmatter 없음 또는 파싱 실패")
        return False, msgs
    msgs.append(f"✅ frontmatter parse OK (name={fm.get('name', '?')})")

    # 2. extends 유효
    extends = fm.get("extends")
    if not extends:
        msgs.append("❌ frontmatter.extends 없음")
        return False, msgs
    ds_root = repo_root / "design-systems" / extends
    if not ds_root.is_dir():
        msgs.append(f"❌ extends '{extends}' → {ds_root} 디렉토리 없음")
        return False, msgs
    msgs.append(f"✅ extends '{extends}' OK ({ds_root.relative_to(repo_root)})")

    ok = True

    # 3. component 참조
    refs = find_component_refs(body, repo_root)
    missing_refs = [r for r, exists in refs if not exists]
    if missing_refs:
        ok = False
        for r in missing_refs:
            msgs.append(f"❌ 컴포넌트 참조 없음: {r}")
    msgs.append(f"  → component refs: {len(refs) - len(missing_refs)} OK / {len(missing_refs)} missing (총 {len(refs)})")

    # 4. token 참조
    tokens = find_token_refs(body)
    missing_tokens = [t for t in tokens if not token_exists_in_ds(t, ds_root)]
    if missing_tokens:
        # 토큰 누락은 경고로 (실제로 있으나 본 검증이 못 잡는 케이스가 많음)
        msgs.append(f"⚠️  baseline DS foundations에 매칭 안 되는 토큰 ({len(missing_tokens)}개) — 검수 필요:")
        for t in missing_tokens[:10]:
            msgs.append(f"      - {t}")
        if len(missing_tokens) > 10:
            msgs.append(f"      ... +{len(missing_tokens) - 10}")
    else:
        msgs.append(f"  → token refs: {len(tokens)}개 모두 baseline DS에 존재")

    # 5. Bindings의 raw 값
    sections = split_sections(body)
    hexes, pxs = find_raw_values_in_bindings(sections)
    if hexes:
        ok = False
        msgs.append(f"❌ Bindings 섹션에 raw hex {len(hexes)}개: {hexes[:5]}{'...' if len(hexes) > 5 else ''}")
    if pxs:
        # px는 더 흔히 의도된 값이 많아 (border 두께 등) — 경고로
        msgs.append(f"⚠️  Bindings 섹션에 raw px {len(pxs)}개 (의도된 경우는 OK): {pxs[:5]}{'...' if len(pxs) > 5 else ''}")
    if not hexes and not pxs:
        msgs.append("  → Bindings raw 값 없음 ✅")

    return ok, msgs


def validate_target(target: Path, repo_root: Path) -> int:
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = sorted(p for p in target.glob("*.md") if not p.name.startswith("00-INDEX") and p.name != "README.md" and p.name != "TEMPLATE.md")
    else:
        print(f"❌ 대상이 파일도 디렉토리도 아님: {target}", file=sys.stderr)
        return 2

    total_fail = 0
    for f in files:
        print(f"\n=== {f.relative_to(repo_root)} ===")
        ok, msgs = validate_screen(f, repo_root)
        for m in msgs:
            print(f"  {m}")
        if not ok:
            total_fail += 1
            print("  → 결과: ❌ 실패")
        else:
            print("  → 결과: ✅ 통과")

    print(f"\n총 {len(files)}개 중 {len(files) - total_fail}개 통과 / {total_fail}개 실패")
    return 0 if total_fail == 0 else 1


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("target", help="검증할 .md 파일 또는 screens 디렉토리")
    p.add_argument("--repo-root", default=None, help="레포 루트 경로 (기본: 자동 탐지)")
    args = p.parse_args()

    target = Path(args.target).resolve()
    repo_root = Path(args.repo_root).resolve() if args.repo_root else find_repo_root(target)
    print(f"repo-root: {repo_root}")
    return validate_target(target, repo_root)


if __name__ == "__main__":
    sys.exit(main())
