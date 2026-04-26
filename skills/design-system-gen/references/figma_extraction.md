# 🎨 Figma 디자인 시스템 추출 가이드 (Figma MCP)

Figma URL을 입력으로 받았을 때, Figma MCP 도구를 사용해 디자인 시스템을 추출하는 절차입니다. SKILL.md의 Phase 1B에서 이 문서를 참조합니다.

---

## 1. URL 파싱

| URL 패턴 | 추출 값 |
|---|---|
| `figma.com/design/:fileKey/:fileName?node-id=:nodeId` | `fileKey`, `nodeId` (`-` → `:`로 변환) |
| `figma.com/design/:fileKey/branch/:branchKey/...` | `fileKey = branchKey` |
| `figma.com/file/...` (구버전) | `figma.com/design/...`과 동일하게 처리 |

`node-id`가 없으면 파일 루트로 간주하고 `get_metadata`로 페이지 목록부터 시작합니다.

---

## 2. 변수(Variables) 우선 추출

> **가장 중요한 단계.** 디자이너가 Variables로 토큰화를 했는지가 결과물 품질의 80%를 결정합니다.

```
mcp__claude_ai_Figma__get_variable_defs(fileKey, nodeId)
```

반환된 변수를 다음과 같이 분류해 `foundations/`로 매핑합니다:

| Figma Variable Collection | 매핑 위치 |
|---|---|
| Color (Primitive) | `foundations/00-color.md` Primitive 섹션 |
| Color (Semantic / Aliased) | `foundations/00-color.md` Semantic 섹션 |
| Number (spacing/4, spacing/8...) | `foundations/00-spacing.md` |
| Number (radius/sm, radius/md...) | `foundations/00-border-radius.md` |
| String (font family/size) | `foundations/00-typography.md` |
| Effect (shadow) | `foundations/00-shadow.md` |

**네이밍 정규화**: Figma의 `color/primary/default` 같은 변수명은 [token_naming.md](token_naming.md)의 컨벤션에 그대로 부합하므로 가능한 한 원본 이름을 유지합니다. 단, `Primary/Default` 같은 PascalCase는 `color/primary/default`로 정규화하세요.

---

## 3. 컴포넌트 인덱스

```
mcp__claude_ai_Figma__search_design_system(fileKey, query)   # 또는
mcp__claude_ai_Figma__get_metadata(fileKey, nodeId)
```

전체 컴포넌트 수가 많을 경우(>10) 한 번에 처리하지 말고, **사용자에게 우선순위 컴포넌트 목록을 확인받습니다**:

> "이 파일에 컴포넌트 N개를 발견했습니다. 어떤 그룹부터 문서화할까요?
>  1) 기본 입력(Button, Input, Select...)
>  2) 피드백(Toast, Alert, Modal...)
>  3) 데이터 표시(Table, Card, List...)
>  4) 전체"

선택된 컴포넌트만 Phase 4까지 진행합니다.

---

## 4. 컴포넌트별 디자인 컨텍스트

선택된 각 컴포넌트(Component Set 권장)에 대해:

```
mcp__claude_ai_Figma__get_design_context(fileKey, nodeId)
mcp__claude_ai_Figma__get_screenshot(fileKey, nodeId)
```

`get_design_context` 응답에서 추출할 정보:

- **Variants/Properties** → `components/NN-xxx.md`의 Variants 섹션
- **Code Connect 매핑** (있을 경우) → 컴포넌트 명세에 `// Code: <path>` 메모로 부착
- **Annotations** (디자이너 주석) → "Designer Notes"로 보존
- **CSS variables 형태의 토큰 참조** → Semantic Token으로 직접 매핑
- **Raw hex / absolute positioning** → 폴백 신호 (아래 5번 참조)

State(Hover/Focus/Active/Disabled)는 보통 별도 variant로 존재하므로 Component Set의 모든 variant를 순회해 추출합니다.

---

## 5. 폴백 (Variables가 없거나 부족할 때)

조건:
- `get_variable_defs`가 빈 결과 또는 < 10개를 반환
- `get_design_context`에서 raw hex / absolute layout이 다수

이 경우:
1. 스크린샷 기반으로 SKILL.md Phase 1A의 휴리스틱(색상 군집화, 간격 그리드 추정 등)을 적용합니다.
2. 추정한 토큰을 명시적으로 "Inferred"로 표기합니다.
3. 사용자에게 **품질 저하 경고**를 출력합니다:

> "⚠️ 이 Figma 파일은 Variables 토큰화가 부족합니다.  
>  결과물은 추정값에 기반하므로 디자이너 검수가 필요합니다."

---

## 6. 산출물 체크리스트

Figma 입력으로 생성할 때 결과 디렉토리에 반드시 포함되어야 하는 것:

- [ ] `foundations/00-*.md` (Variables 기반 우선)
- [ ] `components/NN-*.md` (선택된 컴포넌트만, TEMPLATE 준수)
- [ ] `README.md` (브랜드 아이덴티티 요약 + Figma 링크 백포인터)
- [ ] `AGENTS.md` (재사용 가능한 에이전트 가이드 — `warm` 인스턴스의 것 참조)

---

## 7. 도구 호출 요약 (Quick Reference)

```text
URL 입력
  ↓
get_variable_defs        ──→ foundations/ Primitive·Semantic 채우기
  ↓
search_design_system     ──→ 컴포넌트 목록 → 사용자 확인
  ↓
get_design_context (각각) ──→ components/ variants/states 채우기
get_screenshot     (각각) ──→ 시각 검증 + 폴백 입력
  ↓
quality_criteria.md 4대 기준 + token_coverage 채점 → 완료
```
