# 컴포넌트: 버튼 (Button)

## 개요
사용자의 액션을 트리거하는 클릭 가능한 인터랙티브 요소. 디자인 시스템의 가장 기본적인 컴포넌트.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 폰트 | Pretendard, Medium 500 |
| 보더 반경 | `radius/button` = 8px |
| 포커스 링 | `shadow/focus` = 0 0 0 3px rgba(242,106,0,0.20) |
| 호버 모션 | 100ms cubic-bezier(0, 0, 0.2, 1) |
| 프레스 모션 | 50ms cubic-bezier(0.4, 0, 0.2, 1) |

---

## 변형 (Variant)

### Primary (주요)
- **배경**: `color/primary/default` (#F26A00 라이트 / #FF8A1E 다크)
- **텍스트**: `color/primary/on-primary` (#FFFFFF 라이트 / neutral-950 다크)
- **호버**: `color/primary/hover` (#C75200)
- **액티브**: `color/primary/active` (#9C3D00)
- **사용처**: 주요 CTA, 저장, 확인

### Secondary (보조)
- **배경**: `color/surface/1`
- **텍스트**: `color/text/primary`
- **보더**: 1px solid `color/border/default`
- **호버**: 보더 → `color/border/strong`, 배경 → `color/surface/2`
- **사용처**: 보조 액션, 취소

### Ghost
- **배경**: transparent
- **텍스트**: `color/primary/default`
- **보더**: 1px solid `color/primary/default`
- **호버**: 배경 → `color/primary/subtle`
- **사용처**: 텍스트 버튼, 인라인 액션

### Subtle (저강조)
- **배경**: `color/primary/subtle`
- **텍스트**: `color/primary/default`
- **호버**: 배경 → `color/primary/tint`
- **사용처**: 저강조 CTA

### Danger (위험)
- **배경**: `color/error/default`
- **텍스트**: #FFFFFF
- **호버**: 배경 → `color/error/text`
- **사용처**: 삭제, 위험 액션

---

## 크기 (Size)

| 크기 | 폰트 | 패딩 | 토큰 |
|---|---|---|---|
| Large (lg) | 16px / 500 | 12px 24px | `text/label-lg` |
| Medium (md) | 14px / 500 | 9px 18px | `text/label-md` |
| Small (sm) | 13px / 500 | 6px 14px | `text/label-sm` |

---

## 상태 (State)

| 상태 | 설명 |
|---|---|
| Default | 기본 상태 |
| Hover | 배경/색상 미세 변화 — 100ms ease-out |
| Active / Pressed | 더 어두운 색상 — 50ms ease-in-out, scale(0.97) |
| Focus | `shadow/focus` 링 (오렌지, 3px) |
| Disabled | opacity 0.4, 커서 not-allowed, 포인터 이벤트 없음 |
| Loading | 텍스트 숨김, 중앙 스피너 오버레이 |

---

## 아이콘 포함
- 아이콘은 레이블 좌측 또는 우측, 6px 간격 (`spacing/inline-sm`)
- 아이콘 크기는 버튼 사이즈의 폰트 크기에 맞춤

---

## 접근성
- 아이콘 전용 버튼은 `aria-label` 필수
- 비활성 상태: `aria-disabled="true"` 사용
- 포커스 링 항상 표시
- 최소 터치 영역: 높이 44px (lg 사이즈 충족)

---

## Figma Make 프롬프트

```
다음 스펙으로 버튼(Button) 컴포넌트를 만들어줘:

변형: Primary, Secondary, Ghost, Subtle, Danger
크기: Large (16px, 패딩 12px 24px), Medium (14px, 패딩 9px 18px), Small (13px, 패딩 6px 14px)
폰트: Pretendard Medium 500
보더 반경: 8px

Primary: 배경 #F26A00, 흰색 텍스트, 호버 #C75200, 액티브 scale(0.97)
Secondary: 흰색 배경, 1px 회색 보더, 호버 시 보더 진해짐
Ghost: 투명 배경, 오렌지 텍스트/보더, 호버 시 연한 오렌지 배경
Danger: 배경 #E8321E, 흰색 텍스트

상태: 기본, 호버, 액티브, 포커스(3px 오렌지 링), 비활성(40% 불투명도), 로딩(스피너)

Auto Layout 적용, 모든 색상과 간격에 Variables 사용.
네이밍: Button / {변형} / {크기}
```
