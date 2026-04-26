# 🗺️ 에이전트 가이드 (Repository AGENTS.md)

이 레포지토리는 **디자인 시스템 자동 생성 스킬**과 그 결과물(디자인 시스템 인스턴스)들을 관리합니다. AI 에이전트가 작업을 시작할 때 이 문서가 진입점입니다.

## 🎯 레포의 목적

개발자가 직접 디자인을 하지 않고도 일관된 디자인 시스템을 가질 수 있도록, 다음 두 갈래의 입력으로부터 표준화된 명세를 자동 생성합니다:

1. **HTML/CSS 코드**나 디자인 설명에서 추출
2. **Figma 디자인 시스템 링크**(Figma MCP)에서 추출

## 🧭 프로젝트 맵 (Top-Level)

| 경로 | 내용 |
|---|---|
| [`skills/design-system-gen/`](skills/design-system-gen/) | **생성 스킬 본체** — SKILL.md, references, 스캐폴드 |
| [`design-systems/`](design-systems/) | **결과물(인스턴스)들** — 각 하위 디렉토리가 하나의 디자인 시스템 |
| `design-systems/{brand}/` | 단일 디자인 시스템 인스턴스 (foundations/, components/, docs/, README.md, AGENTS.md) |

## 📚 스킬 사용법 (요약)

자세한 워크플로우는 [`skills/design-system-gen/SKILL.md`](skills/design-system-gen/SKILL.md)에 정의돼 있습니다. 핵심만:

1. **Phase 0** — 입력이 HTML/CSS인지 Figma URL인지 판별
2. **Phase 0.5** — `skills/design-system-gen/assets/scaffold/`를 `design-systems/{brand-name}/`로 복사하고 플레이스홀더 치환
3. **Phase 1A/1B** — 토큰·컴포넌트 추출 (Figma는 Variables 우선)
4. **Phase 2** — `foundations/00-*.md` 작성
5. **Phase 3** — `components/NN-*.md` 작성. **체크리스트 루프**: [`references/component_checklist.md`](skills/design-system-gen/references/component_checklist.md)의 모든 항목이 ✅/⏭️/⛔로 결정될 때까지 반복. 각 컴포넌트는 [`references/state_matrix.md`](skills/design-system-gen/references/state_matrix.md)의 ■ 필수 상태를 모두 다뤄야 함. 종료 시 `components/00-INDEX.md` 보고
6. **Phase 4** — 품질 자가 검증 + 토큰 환원율 리포트

## 📜 레포 차원의 불변 규칙 (Invariants)

작업 시 다음 규칙은 절대 어기지 않습니다:

1. **결과물 위치**: 새 디자인 시스템은 항상 `design-systems/{brand-name}/` 하위에. 레포 루트나 다른 경로에 직접 작성 금지.
2. **스캐폴드 우선**: 새 인스턴스는 반드시 `assets/scaffold/`에서 복사로 시작. 빈 디렉토리에서 직접 만들지 말 것.
3. **체크리스트 루프**: Phase 3는 단발 작업이 아니라 **모든 표준 카탈로그 항목이 결정될 때까지의 루프**. `00-INDEX.md`가 없으면 미완료.
4. **Semantic Token Only**: 컴포넌트 명세에 raw hex/픽셀 직접 사용 금지. `foundations`의 Semantic Token만 참조.
5. **Figma 우선순위**: Figma 입력 시 Variables → Component metadata → Screenshot 휴리스틱 순. Variables로 환원 가능한 값을 절대 raw로 적지 말 것.
6. **스캐폴드 변경 영향**: `assets/scaffold/`를 수정하면 *이후* 생성되는 모든 인스턴스의 베이스가 바뀝니다. 기존 인스턴스는 자동 갱신되지 않으니 별도 마이그레이션 필요.

## 🧩 인스턴스 사이의 관계

각 `design-systems/{brand}/` 인스턴스는 **독립적**입니다 — 토큰이나 컴포넌트를 인스턴스 간에 공유하지 않습니다. 미래에 스크린 명세가 여러 시스템을 "믹스"하는 기능이 추가될 예정이지만, 지금은 1 인스턴스 = 1 자기완결 디자인 시스템입니다.

## 🚀 새 작업을 받을 때

- **새 디자인 시스템 생성 요청** → SKILL.md를 따라 Phase 0부터 진행
- **기존 인스턴스 수정 요청** → 해당 `design-systems/{brand}/AGENTS.md`를 먼저 읽고 그 인스턴스의 컨벤션을 따름
- **스킬 자체 수정 요청** → `skills/design-system-gen/` 안의 SKILL.md / references / scaffold만 수정. 결과물에 직접 손대지 말 것 (스캐폴드를 고치고 마이그레이션하는 게 원칙)
