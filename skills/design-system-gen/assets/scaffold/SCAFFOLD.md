# Design System Scaffold

이 디렉토리는 **결과물이 아니라 스캐폴드**입니다. SKILL의 Phase 0.5(Scaffold)에서 새로운 디자인 시스템 인스턴스를 만들 때 `design-systems/{brand-name}/`로 그대로 복사되는 베이스 템플릿입니다.

## 📦 포함된 파일

- `README.md` — 결과물 루트 README (브랜드 아이덴티티 요약)
- `AGENTS.md` — 에이전트용 프로젝트 맵 + Invariants
- `foundations/TEMPLATE.md` — 파운데이션(토큰) 작성 템플릿
- `components/TEMPLATE.md` — 컴포넌트 명세 작성 템플릿
- `docs/README.md` — 지식 저장소 가이드
- `docs/adr/TEMPLATE.md` — 디자인/아키텍처 결정 기록 템플릿
- `docs/exec-plans/TEMPLATE.md` — 작업 실행 계획 템플릿

## 🔤 플레이스홀더

복사 후 SKILL이 다음 토큰을 실제 값으로 치환합니다:

| 플레이스홀더 | 의미 |
|---|---|
| `{{Brand Name}}` | 브랜드/디자인 시스템 이름 (예: "Warm", "Cool Blue") |
| `{{Brand Color}}` | 핵심 컬러 hex 또는 토큰 표기 (예: `#F26A00`) |
| `{{Primary Typeface}}` | 주요 폰트 패밀리 (예: `Pretendard`) |
| `{{한 줄로 요약한 디자인 무드/철학}}` | 디자인 톤앤매너 한 줄 |
| `{{html-css \| figma \| raw}}` | 입력 종류 |
| `{{Figma URL — Figma 입력일 때만}}` | Figma 원본 링크 (Figma 입력일 때만 채움) |

`TEMPLATE.md` 류의 파일은 치환하지 않고 **그대로** 복사합니다 (사용자가 새 컴포넌트/파운데이션을 추가할 때 참조하는 형식 기준).

## ⚠️ 수정 시 주의

이 스캐폴드를 변경하면 **이후에 생성되는 모든 디자인 시스템 인스턴스**의 베이스가 바뀝니다. 기존 인스턴스(예: `design-systems/warm/`)는 자동으로 갱신되지 않으므로, 큰 변경이 있다면 별도로 마이그레이션을 진행하세요.
