# 📚 지식 저장소 (Knowledge System)

이 디렉토리는 Harness Engineering의 핵심 원칙 중 하나인 **P9(Knowledge System)** 에 따라 리포지토리의 모든 결정과 컨텍스트를 버전 관리되는 마크다운 형식으로 기록하는 공간입니다. 에이전트와 인간 엔지니어의 공통 'System of Record' 역할을 수행합니다.

## 디렉토리 구조 및 용도 (P5: Progressive Disclosure)

- `/adr/` : **아키텍처 결정 기록 (Architecture Decision Records)**
  - 왜 특정 기술과 패턴을 도입했는지, 어떤 대안이 있었는지 역사적 맥락을 기록합니다.
  - 에이전트의 환각(Hallucination)이나 기존 시스템에 맞지 않는 툴 제안을 방지합니다.
  - **작성 기준**: 새로운 주요 라이브러리 도입, 레이어 변경, 컨벤션 수립 시 작성합니다.

- `/exec-plans/` : **스프린트 계약 및 실행 계획 (Sprint Contracts)**
  - 작업을 시작하기 전 "무엇을, 어떻게, 어떤 기준으로" 할지 사람 또는 평가 에이전트와 합의하는 문서입니다.
  - 진행 상황, 완료 여부, 알려진 기술 부채(Tech Debt)가 여기에 모두 기록됩니다.

## 운영 규칙
- 파일명은 주로 `NNN-title.md` (ADR) 또는 `YYYYMMDD-task-name.md` (Exec Plans) 형식을 따릅니다.
- 더 이상 유효하지 않은 문서(Drift 발생)는 P7(Garbage Collection) 원칙에 따라 발견 즉시 갱신하거나 폐기해야 합니다.
