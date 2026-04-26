#!/usr/bin/env python3
"""
WCAG 명암비 자동 검증 스크립트.

사용:
  python check_contrast.py <pairs_file>

pairs_file 형식 (한 줄에 하나, 콤마 구분):
  fg_hex,bg_hex,label,min_ratio
예:
  #171719,#FFFFFF,text/primary on surface/1 (Light),7.0
  #F7F7F8,#171719,text/primary on surface/1 (Dark),7.0

주석은 `;`로 시작하는 줄. (`#`은 hex 값이라 사용 안 함.)

종료 코드:
  0 — 모든 페어 통과
  1 — 하나 이상 미달

WCAG 기준:
  - AA 큰 텍스트(18pt+ or 14pt+ bold): 3.0
  - AA 본문: 4.5
  - AAA 큰 텍스트: 4.5
  - AAA 본문: 7.0
"""
from __future__ import annotations
import sys


def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    h = hex_str.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    """WCAG 2.x 상대 휘도."""
    def channel(c: int) -> float:
        s = c / 255.0
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast_ratio(fg_hex: str, bg_hex: str) -> float:
    l1 = relative_luminance(hex_to_rgb(fg_hex))
    l2 = relative_luminance(hex_to_rgb(bg_hex))
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def main() -> int:
    if len(sys.argv) != 2:
        print(f"사용: {sys.argv[0]} <pairs_file>", file=sys.stderr)
        return 2

    pairs_path = sys.argv[1]
    fail = 0
    total = 0

    with open(pairs_path, encoding='utf-8') as f:
        for line_num, raw in enumerate(f, 1):
            line = raw.strip()
            if not line or line.startswith(';'):
                continue
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 4:
                print(f"line {line_num}: invalid format, expected 4 fields", file=sys.stderr)
                continue
            fg, bg, label, min_ratio_str = parts[:4]
            try:
                min_ratio = float(min_ratio_str)
            except ValueError:
                print(f"line {line_num}: invalid min_ratio '{min_ratio_str}'", file=sys.stderr)
                continue

            ratio = contrast_ratio(fg, bg)
            total += 1
            mark = '✅' if ratio >= min_ratio else '❌'
            if ratio < min_ratio:
                fail += 1
            print(f"{mark}  {ratio:5.2f}:1  (≥{min_ratio:.1f})  {label}")

    print(f"\n총 {total}개 중 {total - fail}개 통과 / {fail}개 실패")
    return 0 if fail == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
