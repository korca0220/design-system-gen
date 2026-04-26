# {{Project Name}} — Screen Specifications

이 디렉토리는 **{{Project Name}}** 프로젝트의 스크린 명세 모음입니다. 각 .md 파일은 framework-neutral한 형식으로 작성되어 React/Flutter/SwiftUI 등 어떤 코드 생성기로도 동일하게 변환됩니다.

## 🎨 베이스 디자인 시스템
- **Primary**: `{{base-design-system}}` (→ [`design-systems/{{base-design-system}}/`](../../design-systems/{{base-design-system}}/))
- **Imports**: {{다른 DS에서 빌려오는 컴포넌트가 있다면 여기에 명시, 없으면 "없음"}}

## 📂 스크린 인덱스
- [00-INDEX.md](00-INDEX.md) — 전체 화면 흐름과 통계

## 🔗 출처 (Source)
- **종류**: {{figma | screenshot | code}}
- **소스 URL**: {{Source URL}}
- **분석 시점**: {{YYYY-MM-DD}}

## 🛠️ 새 스크린 추가
1. `TEMPLATE.md`를 복사해 `NN-screen-name.md`로 작성
2. frontmatter의 `extends`에 베이스 DS 이름 명시
3. Skeleton → Bindings → Intent 순서로 채움
4. `00-INDEX.md`에 항목 추가
