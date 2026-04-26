# 파운데이션: 그림자 (Shadow)

## 개요

5단계 Elevation 기반 그림자 시스템. Warm Neutral 베이스 컬러(rgba(26,25,22,...))를 사용해 차갑지 않고 따뜻한 그림자를 표현. 다크 모드는 별도 강도 적용.

| 항목 | 값 |
|---|---|
| 베이스 컬러 | rgba(26, 25, 22, ...) — Warm Neutral |
| 단계 | 5단계 Elevation |
| 다크 모드 | rgba(0,0,0,...) 계열로 강도 높임 |

---

## 디자인 토큰 — Primitive

### 라이트 모드

| 토큰 | 값 | 사용처 |
|---|---|---|
| `shadow/1` | 0 1px 2px rgba(26,25,22,0.06), 0 1px 3px rgba(26,25,22,0.04) | 인풋, 버튼 기본 |
| `shadow/2` | 0 2px 4px rgba(26,25,22,0.06), 0 4px 8px rgba(26,25,22,0.06) | 카드, 패널 |
| `shadow/3` | 0 4px 8px rgba(26,25,22,0.06), 0 8px 24px rgba(26,25,22,0.08) | 드롭다운, Toast |
| `shadow/4` | 0 8px 16px rgba(26,25,22,0.08), 0 16px 40px rgba(26,25,22,0.10) | 모달, 다이얼로그 |
| `shadow/5` | 0 16px 32px rgba(26,25,22,0.10), 0 32px 64px rgba(26,25,22,0.12) | 커맨드팔레트 |

### 다크 모드

| 토큰 | 값 |
|---|---|
| `shadow/1` | 0 1px 2px rgba(0,0,0,0.20), 0 1px 3px rgba(0,0,0,0.16) |
| `shadow/2` | 0 2px 4px rgba(0,0,0,0.20), 0 4px 8px rgba(0,0,0,0.20) |
| `shadow/3` | 0 4px 8px rgba(0,0,0,0.24), 0 8px 24px rgba(0,0,0,0.28) |
| `shadow/4` | 0 8px 16px rgba(0,0,0,0.28), 0 16px 40px rgba(0,0,0,0.32) |
| `shadow/5` | 0 16px 32px rgba(0,0,0,0.32), 0 32px 64px rgba(0,0,0,0.40) |

---

## 디자인 토큰 — Semantic

| 토큰 | 참조 | 사용처 |
|---|---|---|
| `shadow/card` | shadow/2 | 카드, 패널 |
| `shadow/dropdown` | shadow/3 | 드롭다운, 팝오버 |
| `shadow/modal` | shadow/4 | 모달, 다이얼로그, 드로어 |
| `shadow/toast` | shadow/3 | Toast 알림 |
| `shadow/sticky` | shadow/2 | Sticky 헤더, 고정 요소 |
| `shadow/focus` | 0 0 0 3px rgba(242,106,0,0.20) | 포커스 링 (라이트) |
| `shadow/focus` (다크) | 0 0 0 3px rgba(255,138,30,0.28) | 포커스 링 (다크) |

---

## 포커스 링 규칙

- 모든 인터랙티브 요소(버튼, 인풋, 체크박스, 탭 등)에 `:focus-visible` 시 표시.
- 색상: Primary 색상 기반 (`shadow/focus`).
- 두께: 3px 외곽선.
- 오프셋: 0px (요소 바깥쪽 바로 붙임).

---

## Figma Make 프롬프트

```
다음 스펙으로 그림자(Shadow/Elevation) 시스템을 구성해줘:

5단계 Elevation, Warm Neutral 베이스 컬러 사용:

Level 1 (shadow/1): 미세한 그림자
  - 라이트: 0 1px 2px rgba(26,25,22,0.06), 0 1px 3px rgba(26,25,22,0.04)
  - 다크: 0 1px 2px rgba(0,0,0,0.20)

Level 2 (shadow/2): 카드
  - 라이트: 0 2px 4px rgba(26,25,22,0.06), 0 4px 8px rgba(26,25,22,0.06)
  - 다크: 0 2px 4px rgba(0,0,0,0.20), 0 4px 8px rgba(0,0,0,0.20)

Level 3 (shadow/3): 드롭다운, Toast
  - 라이트: 0 4px 8px rgba(26,25,22,0.06), 0 8px 24px rgba(26,25,22,0.08)
  - 다크: 0 4px 8px rgba(0,0,0,0.24), 0 8px 24px rgba(0,0,0,0.28)

Level 4 (shadow/4): 모달
  - 라이트: 0 8px 16px rgba(26,25,22,0.08), 0 16px 40px rgba(26,25,22,0.10)
  - 다크: 0 8px 16px rgba(0,0,0,0.28), 0 16px 40px rgba(0,0,0,0.32)

Level 5 (shadow/5): 커맨드팔레트
  - 라이트: 0 16px 32px rgba(26,25,22,0.10), 0 32px 64px rgba(26,25,22,0.12)
  - 다크: 0 16px 32px rgba(0,0,0,0.32), 0 32px 64px rgba(0,0,0,0.40)

포커스 링: 0 0 0 3px rgba(242,106,0,0.20) (라이트) / rgba(255,138,30,0.28) (다크)

Semantic 매핑:
shadow/card = Level 2
shadow/dropdown = Level 3
shadow/modal = Level 4
shadow/toast = Level 3
shadow/sticky = Level 2
shadow/focus = 포커스 링

Light/Dark Mode 분리하여 Variables 구성.
```
