---
name: design-system-gen
description: Extract and document design systems (foundations and components) from HTML/CSS or raw design inputs. Use when a user provides UI code and wants to standardize it into foundations/ and components/ directories with detailed markdown specifications following project conventions.
---

# Design System Generator

이 스킬은 HTML/CSS 코드나 디자인 결과물을 분석하여 표준화된 디자인 시스템 명세(Foundations/Components)를 자동으로 추출하고 문서화합니다.

## 🚀 워크플로우 (Workflows)

### Phase 1: 브랜드 아이덴티티 및 디자인 토큰 분석 (Discovery)
입력된 HTML/CSS나 디자인 설명에서 고유한 브랜드 아이덴티티와 디자인 패턴을 식별합니다.
- **브랜드 아이덴티티 정의**: 입력값에서 가장 지배적인 핵심 컬러(Key Color), 전체적인 디자인 무드(예: 미니멀, 사이버펑크, 따뜻함 등), 그리고 톤앤매너를 먼저 정의합니다.
- **색상**: 주요 배경색, 텍스트 색상, 보더 색상을 추출하고 브랜드 컬러와의 연관성을 분석합니다.
- **타이포그래피**: 폰트 종류, 굵기(Weight), 크기(Size), 줄 높이(Line Height)를 식별합니다.
- **간격/레이아웃**: 패딩, 마진, 그리드 간격을 분석합니다.
- **기타**: 보더 반경(Border Radius), 그림자(Shadow), 애니메이션/모션 패턴을 기록합니다.

### Phase 2: 파운데이션 수립 (Foundations)
추출된 토큰을 `foundations/` 디렉토리에 명세화합니다.
- `foundations/TEMPLATE.md` 형식을 엄격히 준수하세요.
- **Primitive vs Semantic**: 값 그 자체(Primitive)와 역할 기반 이름(Semantic)을 분리하여 정의합니다.
- **토큰 명명 규칙**: [references/token_naming.md](references/token_naming.md) 가이드를 따릅니다.

### Phase 3: 컴포넌트 명세 작성 (Components)
UI 요소(Button, Input, Card 등)를 식별하여 `components/` 디렉토리에 명세화합니다.
- `components/TEMPLATE.md` 형식을 엄격히 준수하세요.
- **상태 정의**: Hover, Active, Focus, Disabled 상태에 따른 토큰 변화를 기술합니다.
- **변형(Variants)**: Primary, Secondary, Ghost 등 디자인 옵션을 분류합니다.

### Phase 4: 품질 검증 및 브릿지 (Validation & Bridge)
- **디자인 품질**: [references/quality_criteria.md](references/quality_criteria.md)의 4대 기준을 스스로 평가하고 피드백합니다.
- **Figma Make**: 각 컴포넌트 하단에 디자이너가 바로 활용할 수 있는 상세한 Figma 생성 프롬프트를 포함합니다.

## 📜 주요 규칙 (Core Rules)
- **Semantic Token Only**: 컴포넌트 명세 작성 시 반드시 Semantic Token만을 참조해야 합니다.
- **No Magic Numbers**: 모든 수치는 `foundations`의 스페이싱/폰트 시스템 내의 값으로 치환하십시오.
- **Accessible Design**: 명암비 및 키보드 접근성(Focus Ring) 명세를 반드시 포함하세요.
