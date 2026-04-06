# 🏗️ 디자인 시스템 토큰 명명 규칙 (Token Naming)

이 프로젝트는 **Primitive(원시)**와 **Semantic(의미론적)**이라는 두 계층의 토큰 구조를 사용합니다.

---

### 1. Primitive Tokens (기초 레이어)
- **정의**: 디자인 시스템의 원재료입니다. 색상, 수치 등 고유한 값을 나타냅니다.
- **예시**:
    - `color/orange/500` (#F26A00)
    - `spacing/4` (16px)
    - `fontSize/16` (16px)
- **규칙**: 라이트/다크 모드와 관계없이 변하지 않는 고유한 값으로 정의하세요.

### 2. Semantic Tokens (의미 레이어)
- **정의**: 컴포넌트에서 실질적으로 참조하는 토큰입니다. 목적과 역할에 따라 이름을 붙입니다.
- **예시**:
    - `color/primary/default`: 주요 버튼이나 링크의 배경색. (Light: orange/500, Dark: orange/400)
    - `spacing/component-md`: 버튼이나 인풋의 수직 패딩. (spacing/3 = 12px)
- **규칙**: 컴포넌트는 반드시 Semantic Token만을 참조해야 합니다. 라이트/다크 모드별로 서로 다른 Primitive Token을 매핑할 수 있습니다.

### 3. 네이밍 컨벤션
- **색상 (Color)**: `color/[목적]/[단계]`
    - 예: `color/text/primary`, `color/border/subtle`, `color/surface/1`
- **간격 (Spacing)**: `spacing/[카테고리]-[사이즈]`
    - 예: `spacing/component-sm`, `spacing/layout-lg`
- **반경 (Radius)**: `radius/[컴포넌트 유형]`
    - 예: `radius/button`, `radius/card`
- **타이포그래피 (Typography)**: `text/[카테고리]-[사이즈]`
    - 예: `text/body-md`, `text/heading-xl`
