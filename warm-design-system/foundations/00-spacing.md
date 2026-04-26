# 파운데이션: 스페이싱 (Spacing)

## 개요

4px를 최소 단위로 하는 간격 시스템. 모든 값은 4의 배수. Primitive(원시값) → Semantic(의미 기반) 2레이어 구조.

| 항목 | 값 |
|---|---|
| 기준 단위 | 4px |
| 규칙 | 모든 간격은 4의 배수 |
| 라이트/다크 | 동일 |

---

## 디자인 토큰 — Primitive

| 토큰 | 값 | rem |
|---|---|---|
| `spacing/0` | 0px | 0 |
| `spacing/1` | 4px | 0.25rem |
| `spacing/2` | 8px | 0.5rem |
| `spacing/3` | 12px | 0.75rem |
| `spacing/4` | 16px | 1rem |
| `spacing/5` | 20px | 1.25rem |
| `spacing/6` | 24px | 1.5rem |
| `spacing/8` | 32px | 2rem |
| `spacing/10` | 40px | 2.5rem |
| `spacing/12` | 48px | 3rem |
| `spacing/16` | 64px | 4rem |
| `spacing/20` | 80px | 5rem |
| `spacing/24` | 96px | 6rem |

---

## 디자인 토큰 — Semantic

### 컴포넌트 내부 간격 (Component)

컴포넌트 내부 패딩, 아이콘-텍스트 간격 등에 사용.

| 토큰 | 참조 | 값 | 사용처 |
|---|---|---|---|
| `spacing/component-xs` | spacing/1 | 4px | 아이콘 내부 패딩 |
| `spacing/component-sm` | spacing/2 | 8px | 인라인 요소 간격 |
| `spacing/component-md` | spacing/3 | 12px | 버튼 수직 패딩 |
| `spacing/component-lg` | spacing/4 | 16px | 카드 내부 패딩 |
| `spacing/component-xl` | spacing/6 | 24px | 섹션 내부 패딩 |

### 레이아웃 간격 (Layout)

컴포넌트 간 여백, 섹션 간 간격 등에 사용.

| 토큰 | 참조 | 값 | 사용처 |
|---|---|---|---|
| `spacing/layout-xs` | spacing/4 | 16px | 컴포넌트 간 최소 간격 |
| `spacing/layout-sm` | spacing/6 | 24px | 카드 간 간격 |
| `spacing/layout-md` | spacing/8 | 32px | 섹션 간 간격 |
| `spacing/layout-lg` | spacing/12 | 48px | 페이지 섹션 간격 |
| `spacing/layout-xl` | spacing/20 | 80px | 랜딩 섹션 간격 |

### 인라인 간격 (Inline)

텍스트 내부, 뱃지·태그 등 인라인 요소에 사용.

| 토큰 | 참조 | 값 |
|---|---|---|
| `spacing/inline-xs` | spacing/1 | 4px |
| `spacing/inline-sm` | spacing/2 | 8px |
| `spacing/inline-md` | spacing/3 | 12px |
| `spacing/inline-lg` | spacing/4 | 16px |

---

## 사용 원칙

- 컴포넌트 내부 패딩: `component-*` 토큰 사용.
- 컴포넌트 사이 간격: `layout-*` 토큰 사용.
- 4px 미만의 값(2px, 3px)은 예외적으로만 허용.
- 임의 값(매직 넘버) 사용 금지.

---

## Figma Make 프롬프트

```
다음 스펙으로 스페이싱 시스템을 Figma Variables (Number 타입)로 구성해줘:

Collection — Spacing (Mode 없음, Number 타입):

Primitive:
spacing/0 = 0
spacing/1 = 4
spacing/2 = 8
spacing/3 = 12
spacing/4 = 16
spacing/5 = 20
spacing/6 = 24
spacing/8 = 32
spacing/10 = 40
spacing/12 = 48
spacing/16 = 64
spacing/20 = 80
spacing/24 = 96

Semantic (Primitive를 Alias로 연결):
component/xs = spacing/1 (4px) — 아이콘 내부 패딩
component/sm = spacing/2 (8px) — 인라인 간격
component/md = spacing/3 (12px) — 버튼 수직 패딩
component/lg = spacing/4 (16px) — 카드 내부 패딩
component/xl = spacing/6 (24px) — 섹션 내부 패딩
layout/xs = spacing/4 (16px) — 컴포넌트 간 최소
layout/sm = spacing/6 (24px) — 카드 간 간격
layout/md = spacing/8 (32px) — 섹션 간 간격
layout/lg = spacing/12 (48px) — 페이지 섹션
layout/xl = spacing/20 (80px) — 랜딩 섹션
```
