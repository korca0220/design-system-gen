# {{Brand Name}} Design System

이 프로젝트는 **{{Brand Name}} ({{Brand Color}})** 브랜딩을 기반으로 한 제품 디자인 시스템입니다. 일관된 시각적 언어와 고품질의 사용자 경험을 제공하기 위해 파운데이션(Tokens)과 컴포넌트(UI Elements)로 구성되어 있습니다.

## 🏗️ 프로젝트 구조

- **[foundations/](./foundations/)**: 디자인 시스템의 원재료인 디자인 토큰(Color, Typography, Spacing, Shadow, Border Radius, Motion)이 정의되어 있습니다.
- **[components/](./components/)**: 파운데이션 토큰을 조합하여 만든 재사용 가능한 UI 컴포넌트 명세입니다.
- **[docs/](./docs/)**: 시스템 설계 결정 내역(ADR) 및 작업 계획서가 기록됩니다.

## 🎨 핵심 아이덴티티
- **Brand Color**: `{{Brand Color}}`
- **Typography**: `{{Primary Typeface}}`
- **Design Philosophy**: {{한 줄로 요약한 디자인 무드/철학}}

## 🔗 출처 (Source)
- **입력 종류**: {{html-css | figma | raw}}
- **Figma 링크**: {{Figma URL — Figma 입력일 때만}}

## 🛠️ 기여 가이드
새로운 컴포넌트나 파운데이션을 추가할 때는 각 디렉토리의 `TEMPLATE.md`를 참조하여 일관된 형식으로 작성하십시오. 모든 컴포넌트는 반드시 `foundations`에 정의된 **Semantic Token**만을 사용하여 스타일링되어야 합니다.
