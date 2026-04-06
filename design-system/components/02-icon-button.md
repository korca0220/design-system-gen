# 컴포넌트: 아이콘 버튼 (Icon Button)

## 개요
아이콘만 포함하는 정사각형 버튼. 텍스트 레이블이 불필요한 간결한 액션 트리거에 사용.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 보더 반경 | `radius/button` = 8px |
| 포커스 링 | `shadow/focus` = 0 0 0 3px rgba(242,106,0,0.20) |
| 호버 모션 | 100ms cubic-bezier(0, 0, 0.2, 1) |
| 프레스 모션 | 50ms cubic-bezier(0.4, 0, 0.2, 1) |

---

## 크기 (Size)

| 크기 | 가로 × 세로 | 아이콘 크기 |
|---|---|---|
| Large (lg) | 44 × 44px | 18px |
| Medium (md) | 36 × 36px | 16px |
| Small (sm) | 28 × 28px | 14px |

---

## 변형 (Variant)

### Primary
- **배경**: `color/primary/default`
- **아이콘 색상**: `color/primary/on-primary`
- **호버**: `color/primary/hover`

### Secondary
- **배경**: `color/surface/1`
- **아이콘 색상**: `color/text/primary`
- **보더**: 1px solid `color/border/default`
- **호버**: 보더 → `color/border/strong`

### Ghost
- **배경**: transparent
- **아이콘 색상**: `color/text/secondary`
- **호버**: 배경 → `color/surface/2`, 아이콘 → `color/text/primary`

---

## 상태 (State)

| 상태 | 설명 |
|---|---|
| Default | 기본 상태 |
| Hover | 배경/보더 변화 — 100ms ease-out |
| Active | scale(0.94) — 50ms ease-in-out |
| Focus | `shadow/focus` 링 |
| Disabled | opacity 0.4, 커서 not-allowed |

---

## 접근성
- 액션을 설명하는 `aria-label` 항상 필요 (예: `aria-label="편집"`)
- 호버 시 툴팁으로 액션 레이블 표시
- 최소 터치 영역: 44px (lg 사이즈)

---

## Figma Make 프롬프트

```
다음 스펙으로 아이콘 버튼(Icon Button) 컴포넌트를 만들어줘:

크기: Large (44×44px, 아이콘 18px), Medium (36×36px, 아이콘 16px), Small (28×28px, 아이콘 14px)
변형: Primary, Secondary, Ghost
보더 반경: 8px

Primary: 오렌지 배경 (#F26A00), 흰색 아이콘
Secondary: 흰색 배경, 1px 회색 보더, 어두운 아이콘
Ghost: 투명 배경, 회색 아이콘, 호버 시 연한 배경

상태: 기본, 호버, 액티브(scale 0.94), 포커스(3px 오렌지 링), 비활성(40% 불투명도)

아이콘이 가운데 정렬된 정사각형 Auto Layout 사용.
네이밍: Icon Button / {변형} / {크기}
```
