# 📐 레이아웃 문법 (Layout Grammar)

스크린 명세 Skeleton 섹션의 표준 위계 문법입니다. Framework-neutral하게 화면 구조를 표현하기 위한 5단계 계층 + 메타 마커.

---

## 🌳 5단계 위계

| 레벨 | 이름 | 의미 | 예시 |
|---|---|---|---|
| 1 | **Page** | 화면 전체 (viewport) | `Page (viewport: mobile)` |
| 2 | **Region** | 의미 단위 영역 (페이지 내 고수준 분할) | `Header`, `Hero`, `Content`, `Footer`, `Floating` |
| 3 | **Section** | Region 내부의 묶음 (반복/그룹) | `User Card`, `Action Bar`, `List` |
| 4 | **Slot** | 단일 컴포넌트가 들어가는 자리 | `leading`, `title`, `trailing` |
| 5 | **Component** | DS 컴포넌트 참조 | `↳ component: design-systems/wanted/components/15-avatar.md` |

> Slot은 항상 Component로 끝납니다. Component 없는 Slot은 ❌.

---

## 📝 표기 규칙

들여쓰기 트리 형식 (코드 블록 안에):

```
Page (viewport: mobile)
├── Region: Header
│   └── Section: TopBar
│       ├── Slot: leading
│       │   ↳ component: design-systems/wanted/components/09-icon-button.md
│       ├── Slot: title
│       │   ↳ component: design-systems/wanted/components/16-label.md
│       └── Slot: trailing
│           ↳ component: design-systems/wanted/components/09-icon-button.md
├── Region: Content
│   ├── Section: Hero Card
│   │   ↳ component: design-systems/wanted/components/06-card.md
│   │   ├── Slot: image
│   │   │   ↳ <Custom name="HeroImage">
│   │   ├── Slot: title
│   │   │   ↳ component: design-systems/wanted/components/16-label.md
│   │   └── Slot: description
│   │       ↳ component: design-systems/wanted/components/16-label.md
│   └── Section: Action List
│       └── (반복) Item × N
│           ↳ component: design-systems/wanted/components/04-chip.md
└── Region: Floating
    └── Slot: snackbar
        ↳ component: design-systems/wanted/components/08-snackbar.md
```

### 메타 마커

| 마커 | 의미 | 예시 |
|---|---|---|
| `(반복)` | 같은 슬롯이 데이터 배열만큼 반복 | `(반복) Item × N ↳ component: ...chip.md` |
| `(조건)` | 특정 상태에서만 노출 | `(조건: empty) ↳ component: ...fallback-view.md` |
| `<Custom name="...">` | DS에 없는 요소 — 추후 DS 합류 후보 | `<Custom name="HeroImage">` |
| `(viewport: ...)` | 폼팩터별 분기 | `(viewport: tablet+) ↳ component: ...drawer.md` |
| `↳ slot: <name>` | 같은 컴포넌트의 내부 슬롯으로 진입 | Card의 leading/title/description처럼 합성 컴포넌트 |

### Region 표준 이름 (권장)

도메인에 맞게 자유 명명 가능하지만 다음이 일반적이라 검색·재사용에 유리:

- **Header** — 상단 고정 영역 (TopNavigation 류)
- **Hero** — 첫 화면 임팩트 영역 (큰 이미지/타이틀)
- **Content** — 주요 콘텐츠 영역 (스크롤 가능)
- **Sidebar** — 사이드 보조 영역 (데스크탑 위주)
- **Footer** — 하단 고정 영역 (BottomNavigation 류)
- **Floating** — 절대 위치 오버레이 (FAB, Snackbar, Modal 트리거 등)

---

## 🎯 합성 컴포넌트의 Slot 표기

`Card`, `Modal`, `Snackbar` 같은 합성 컴포넌트는 자체 슬롯을 가집니다. 이때 두 가지 표기:

**A. 컴포넌트만 참조 (간단)**
```
↳ component: design-systems/wanted/components/06-card.md
   (variant: default, leading: avatar, title: text, body: paragraph)
```
→ 슬롯 채움은 Bindings 섹션에서.

**B. 슬롯 트리 명시 (복잡한 합성)**
```
↳ component: design-systems/wanted/components/06-card.md
   ├── ↳ slot: thumbnail
   │   ↳ <Custom name="HeroImage">
   ├── ↳ slot: title
   │   ↳ component: design-systems/wanted/components/16-label.md
   └── ↳ slot: actions
       └── (반복) ↳ component: design-systems/wanted/components/01-button.md
```

**권장**: 슬롯이 3개 이하면 A, 그 이상이거나 슬롯 안에 또 컴포넌트 들어가면 B.

---

## 🚦 반응형 분기

뷰포트별로 다른 구조가 필요할 때:

```
Region: Content
├── (viewport: mobile)
│   └── Section: Single Column
│       └── (반복) ↳ component: ...card.md
└── (viewport: tablet+)
    └── Section: Grid 2-col
        └── (반복) ↳ component: ...card.md
```

frontmatter `viewport.responsive`에 적힌 폼팩터마다 명시. 모든 폼팩터에서 동일하면 분기 생략.

---

## ❌ 안티패턴

이런 표기는 피하세요:

- **인라인 스타일** — `Slot: title (color: #0066FF, padding: 16px)` ❌. 색상/패딩은 항상 Bindings 섹션의 토큰 참조.
- **JSX 흉내** — `<Card><Avatar /></Card>` ❌. JSX는 framework-specific. 트리는 들여쓰기로.
- **DS 외부 컴포넌트 직접 참조** — `↳ component: @mui/Button` ❌. 외부에서 빌리려면 frontmatter `imports`에 등록 후 `imports/...` 경로로.
- **Component 없는 Slot** — `Slot: title` 이후 component 라인 없음 ❌. Custom이라도 명시.
