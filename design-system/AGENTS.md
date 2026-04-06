# 🗺️ Agent Entry Point (AGENTS.md)

환영합니다, AI 에이전트. 
이 리포지토리는 **Harness Engineering** 철학에 따라 구축되었습니다. 이 파일은 당신이 코드베이스를 파악하기 위한 '최상위 지도(Map)'입니다. (Harness P1: Agent Entry Point)

## 🧭 탐색 경로 (Progressive Disclosure - P5)

모든 정보를 이 파일에 담지 마세요. 상세한 컨텍스트와 규칙은 아래 지식 저장소(System of Record)를 참조하여 점진적으로 파악하세요.

- 📚 **문서 디렉토리 가이드**: [docs/README.md](docs/README.md) - 리포지토리 전체 문서 구조 안내
- 🏛️ **아키텍처 결정 기록(ADR)**: [docs/adr/](docs/adr/) - 특정 기술/패턴 도입 배경 및 히스토리
- 📝 **스프린트 작업 계약(Exec Plans)**: [docs/exec-plans/](docs/exec-plans/) - 작업을 시작하기 전 "무엇을, 어떻게, 어떤 기준으로" 할지 합의
- 🎨 **디자인 시스템 명세**:
  - 파운데이션: [foundations/](foundations/)
  - 컴포넌트: [components/](components/)

## 📜 하네스 핵심 불변 규칙 (Invariants - P3, P6)

작업 시 다음의 아키텍처 규칙과 프론트엔드 설계 원칙을 반드시 준수해야 합니다.

1. **Layered Architecture**: 데이터와 관심사는 고정된 레이어 (`Types → Config → Repo → Service → Runtime → UI`) 순서로만 흐릅니다. 레이어 우회는 기계적(Linter)으로 금지됩니다.
2. **Frontend Quality**: 코드를 생성할 때 "AI Slop(밋밋하고 예상 가능한 패턴)"을 지양하고, 4대 기준(**Design Quality, Originality, Craft, Functionality**)을 충족해야 합니다.
3. **No Drift**: 실제 코드와 맞지 않는 오래된 문서는 직접 업데이트하거나 PR을 통해 삭제(Garbage Collection)하세요.

## 🚀 다음 단계 (Next Steps)

작업을 시작하기 전, `/docs/exec-plans/` 내에서 자신에게 할당된 최근 Sprint Contract를 읽고 목표를 숙지한 뒤, 템플릿에 맞추어 작업을 실행하세요.
