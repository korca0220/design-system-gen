---
name: design-system-gen
description: Extract and document design systems (foundations and components) from HTML/CSS, raw design inputs, or Figma URLs (via Figma MCP). Use when a user provides UI code OR a Figma design system link and wants to standardize it into foundations/ and components/ directories with detailed markdown specifications following project conventions.
---

# Design System Generator

이 스킬은 HTML/CSS 코드, 디자인 결과물, 또는 **Figma 디자인 시스템 링크**를 분석하여 표준화된 디자인 시스템 명세(Foundations/Components)를 자동으로 추출하고 문서화합니다.

## 📁 출력 위치 (Output Location)

모든 결과물은 레포 루트의 `design-systems/{brand-name}/` 하위에 생성합니다 (예: `design-systems/warm/`, `design-systems/cool/`). 한 레포에 여러 디자인 시스템 인스턴스를 공존시킬 수 있도록 멀티 인스턴스 구조를 유지하세요.

## 🚀 워크플로우 (Workflows)

### Phase 0: 입력 종류 분기 (Input Routing)
사용자가 제공한 입력의 종류를 먼저 판별합니다.
- **(A) HTML/CSS 코드 또는 디자인 설명** → Phase 1A로 진행
- **(B) Figma URL** (`figma.com/design/...`, `figma.com/file/...`) → Phase 1B로 진행 (Figma MCP 사용)

### Phase 1A: HTML/CSS 기반 브랜드 아이덴티티 및 토큰 분석 (Discovery)
입력된 HTML/CSS나 디자인 설명에서 고유한 브랜드 아이덴티티와 디자인 패턴을 식별합니다.
- **브랜드 아이덴티티 정의**: 입력값에서 가장 지배적인 핵심 컬러(Key Color), 전체적인 디자인 무드(예: 미니멀, 사이버펑크, 따뜻함 등), 그리고 톤앤매너를 먼저 정의합니다.
- **색상**: 주요 배경색, 텍스트 색상, 보더 색상을 추출하고 브랜드 컬러와의 연관성을 분석합니다.
- **타이포그래피**: 폰트 종류, 굵기(Weight), 크기(Size), 줄 높이(Line Height)를 식별합니다.
- **간격/레이아웃**: 패딩, 마진, 그리드 간격을 분석합니다.
- **기타**: 보더 반경(Border Radius), 그림자(Shadow), 애니메이션/모션 패턴을 기록합니다.

### Phase 1B: Figma 기반 토큰 및 컴포넌트 추출 (Discovery — Figma MCP)
Figma URL이 주어진 경우, Figma MCP의 도구를 사용해 디자인 시스템을 직접 읽어옵니다. 자세한 절차는 [references/figma_extraction.md](references/figma_extraction.md)를 따릅니다.

순서:
1. **URL 파싱**: `fileKey`, `nodeId` 추출 (`node-id`의 `-`를 `:`로 변환).
2. **변수 우선 추출** — `mcp__claude_ai_Figma__get_variable_defs`로 Variables(Color/Number/String 등)를 먼저 가져옵니다. 토큰이 변수화되어 있다면 이 결과가 그대로 `foundations/`의 Primitive/Semantic 매핑이 됩니다 (가장 큰 레버리지).
3. **컴포넌트 인덱스** — `mcp__claude_ai_Figma__search_design_system` 또는 `get_metadata`로 컴포넌트/세트 목록을 가져옵니다. 컴포넌트 수가 많으면 사용자에게 어떤 항목을 문서화할지 **반드시 확인**하세요 (한 번에 전체 처리는 비효율).
4. **컴포넌트별 컨텍스트** — 선택된 각 컴포넌트에 대해 `mcp__claude_ai_Figma__get_design_context` + `get_screenshot`을 호출하여 variants/states/anatomy를 추출합니다.
5. **토큰 폴백** — Variables가 없거나 raw hex/absolute layout이 다수면, 스크린샷 + Phase 1A의 휴리스틱으로 폴백합니다. 이 경우 환원율이 낮음을 사용자에게 명시적으로 경고하세요.

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
- **토큰 환원율 (Token Coverage)**: foundations Semantic Token으로 환원되지 못한 raw hex/픽셀 값의 개수를 집계해 사용자에게 리포트합니다. 신뢰도의 핵심 지표입니다.
- **Figma Make**: 각 컴포넌트 하단에 디자이너가 바로 활용할 수 있는 상세한 Figma 생성 프롬프트를 포함합니다.

## 📜 주요 규칙 (Core Rules)
- **Output Path**: 결과물은 항상 `design-systems/{brand-name}/` 하위에 작성합니다. 레포 루트에 직접 작성하지 마세요.
- **Semantic Token Only**: 컴포넌트 명세 작성 시 반드시 Semantic Token만을 참조해야 합니다.
- **No Magic Numbers**: 모든 수치는 `foundations`의 스페이싱/폰트 시스템 내의 값으로 치환하십시오.
- **Accessible Design**: 명암비 및 키보드 접근성(Focus Ring) 명세를 반드시 포함하세요.
- **Figma 우선순위**: Figma 입력의 경우 Variables → Component metadata → Screenshot 휴리스틱 순으로 신뢰합니다. Variables로 환원 가능한 값을 절대 raw hex로 적지 마세요.
