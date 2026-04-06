# 파운데이션: 모션 (Motion)

## 개요

인터랙션 모션 시스템. 사용자의 액션에 즉각적이고 자연스럽게 반응하는 것을 목표로 함. `prefers-reduced-motion` 접근성 대응 필수.

| 항목 | 값 |
|---|---|
| 최소 Duration | 50ms (버튼 Press) |
| 최대 Duration | 500ms (스켈레톤) |
| 기본 Easing | ease-out (cubic-bezier(0, 0, 0.2, 1)) |
| 접근성 | prefers-reduced-motion: reduce 대응 필수 |

---

## 디자인 토큰 — Primitive

### Duration (지속 시간)

| 토큰 | 값 | 사용처 |
|---|---|---|
| `duration/instant` | 50ms | 버튼 Press, 즉각 피드백 |
| `duration/fast` | 100ms | Hover 상태, 포커스 링 |
| `duration/normal` | 200ms | Fade, Slide, Scale — 일반 전환 |
| `duration/slow` | 300ms | 모달 진입, 드로어, 페이지 전환 |
| `duration/slower` | 400ms | Accordion Expand/Collapse |
| `duration/lazy` | 500ms | 스켈레톤, 로딩 전환 |

### Easing (가속 곡선)

| 토큰 | 값 | 사용처 |
|---|---|---|
| `easing/linear` | linear | 로딩 스피너, 무한 반복 |
| `easing/in` | cubic-bezier(0.4, 0, 1, 1) | 요소 퇴장, 닫힘 |
| `easing/out` | cubic-bezier(0, 0, 0.2, 1) | 요소 등장, 열림 — **가장 많이 사용** |
| `easing/inOut` | cubic-bezier(0.4, 0, 0.2, 1) | 페이지 전환, 탭 이동 |
| `easing/spring` | cubic-bezier(0.34, 1.56, 0.64, 1) | 모달 팝인, Scale 강조 (오버슈트) |
| `easing/overshoot` | cubic-bezier(0.34, 1.30, 0.64, 1) | Toast 팝인, 알림 강조 (미세 오버슈트) |

---

## 디자인 토큰 — Semantic

| 토큰 | Duration | Easing | 사용처 |
|---|---|---|---|
| `motion/hover` | duration/fast (100ms) | easing/out | 버튼 hover, 링크 컬러 변화 |
| `motion/press` | duration/instant (50ms) | easing/inOut | 버튼 클릭, 탭 피드백 |
| `motion/fade` | duration/normal (200ms) | easing/out | Tooltip, Badge 등장/소멸 |
| `motion/slide` | duration/normal (200ms) | easing/out | 드롭다운, 사이드바 슬라이드 |
| `motion/scale` | duration/normal (200ms) | easing/spring | 모달 팝인, 카드 호버 확대 |
| `motion/page` | duration/slow (300ms) | easing/out | 페이지/탭 전환 |
| `motion/expand` | duration/slow (300ms) | easing/out | Accordion, Collapse 토글 |

---

## 인터랙션 패턴별 적용

### 버튼
- Hover: `motion/hover` (background 색상 전환)
- Press: `motion/press` + scale(0.97)
- Loading → Idle: `motion/fade`

### 모달 / 다이얼로그
- 등장: `motion/scale` (scale 0.95 → 1, translateY(8px) → 0)
- 오버레이: `motion/fade` (opacity 0 → 0.48)
- 퇴장: `motion/fade` (opacity → 0)

### 드롭다운 / 툴팁
- 등장: `motion/fade` + translateY(4px) → 0
- 퇴장: `motion/fade` + translateY(0) → 4px

### 드로어
- 등장: `motion/page` (translateX(100%) → 0)
- 퇴장: `motion/page` (translateX(0) → 100%)

### Toast
- 등장: `motion/scale` (easing/overshoot) + translateY(8px) → 0
- 퇴장: `motion/fade`

---

## 접근성 대응

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

모든 애니메이션은 이 미디어 쿼리 하나로 비활성화되도록 CSS transition/animation 기반으로 구현.

---

## Figma Make 프롬프트

```
다음 스펙으로 모션(Motion) 시스템을 구성해줘:

Duration 값 (ms):
- instant: 50ms — 버튼 Press
- fast: 100ms — Hover 상태
- normal: 200ms — 일반 전환 (Fade, Slide, Scale)
- slow: 300ms — 모달, 드로어, 페이지 전환
- slower: 400ms — Accordion 펼침/닫힘
- lazy: 500ms — 스켈레톤, 로딩

Easing 곡선:
- linear: linear — 스피너 무한 회전
- in: cubic-bezier(0.4, 0, 1, 1) — 퇴장
- out: cubic-bezier(0, 0, 0.2, 1) — 등장 (기본)
- inOut: cubic-bezier(0.4, 0, 0.2, 1) — 페이지 전환
- spring: cubic-bezier(0.34, 1.56, 0.64, 1) — 모달 팝인
- overshoot: cubic-bezier(0.34, 1.30, 0.64, 1) — Toast 팝인

Semantic 조합:
motion/hover = 100ms + ease-out — 버튼 hover
motion/press = 50ms + ease-in-out — 버튼 클릭
motion/fade = 200ms + ease-out — Tooltip, Badge 등장
motion/slide = 200ms + ease-out — 드롭다운 슬라이드
motion/scale = 200ms + spring — 모달 팝인
motion/page = 300ms + ease-out — 페이지 전환
motion/expand = 300ms + ease-out — Accordion 토글

Prototype 탭에서 각 패턴을 시연할 수 있도록 인터랙티브 컴포넌트 구성.
접근성: prefers-reduced-motion 대응 명시.
```
