---
name: screen-spec-gen
description: Convert UI screens (from Figma URL or screenshots) into framework-neutral Markdown specifications that compose the design system's tokens and components. Use when a user provides a Figma screen link (or screenshot description) AND a target design system instance to "describe" the screen with — output is .md files consumable by code generators for any framework (React, Flutter, SwiftUI, etc.).
---

# Screen Specification Generator

이 스킬은 UI 스크린을 **framework-neutral한 .md 명세**로 변환합니다. 산출된 .md는 특정 디자인 시스템(`design-systems/{brand}/`)의 토큰과 컴포넌트 vocabulary로 작성되어, React/Flutter/SwiftUI 등 어떤 프레임워크의 코드 생성기로도 동일하게 변환 가능합니다.

> **상위 스킬과의 관계**: 본 스킬은 [`design-system-gen`](../design-system-gen/SKILL.md)이 *생산*한 디자인 시스템을 *소비*하는 두 번째 스킬입니다. 디자인 시스템 = 어휘, 스크린 명세 = 그 어휘로 짠 문장.

## 📁 출력 위치 (Output Location)

**모든 스크린 명세는 레포 루트의 `screens/{project}/` 하위에 생성합니다.** 디자인 시스템 인스턴스(`design-systems/{brand}/`)와 독립된 위치 — 한 프로젝트가 여러 DS를 믹스하거나, DS 변경 없이 화면만 다시 생성하는 경우를 모두 깔끔히 처리.

- 기본 패턴: `screens/{project}/NN-screen-name.md` (NN은 두 자리 순서, 화면 흐름 순서대로)
- 베이스 디자인 시스템은 각 스크린의 frontmatter `extends`로 지정
- 예: `screens/dailypiece/01-profile.md` 가 `extends: wanted` 명시 → `design-systems/wanted/`의 컴포넌트 참조

> **이전 컨벤션 비호환**: 이전 버전 SKILL.md는 `design-systems/{brand}/screens/`를 권장했으나, 그 구조는 한 DS에 종속된 스크린만 표현 가능했음. 본 컨벤션이 더 일반적이므로 **모든 신규 작업은 루트 `screens/`로 진행**합니다. 기존 인스턴스는 마이그레이션 권장.

## 🚀 워크플로우 (Workflows)

### Phase 0: 입력과 베이스 디자인 시스템 결정 (Routing)
다음 두 가지를 명확히 합니다:

1. **입력 종류**:
   - **(A) Figma URL** — 가장 정확한 입력 (Figma MCP로 디자인 컨텍스트 + 스크린샷 추출)
   - **(B) 스크린샷 + 텍스트 설명** — Figma 한도 부족 또는 비공개 파일일 때 폴백
   - **(C) 코드 (HTML/JSX 등)** — 이미 있는 화면을 systematize 하는 경우
2. **베이스 디자인 시스템 인스턴스**:
   - 결과물의 모든 토큰/컴포넌트 참조가 어느 `design-systems/{brand}/`을 가리키는지 결정
   - 기본은 단일 시스템. 믹스가 필요하면 frontmatter에 `extends:` + `imports:` 명시 (Phase 0.5 참조)

### Phase 0.5: 스캐폴드 + Frontmatter 결정
출력 디렉토리에 [`assets/scaffold/`](assets/scaffold/)의 베이스 파일들을 복사합니다 (단, `SCAFFOLD.md` 제외). 그리고 각 스크린 .md의 frontmatter를 결정합니다:

```yaml
---
name: 화면 이름 (예: "오늘의 한 조각")
extends: wanted               # 베이스 DS 인스턴스 (필수)
imports: []                   # 다른 DS에서 빌려오는 컴포넌트 (예: ["cool/components/chart"])
source:
  type: figma | screenshot | code
  url: <Figma URL or 출처>
  node_id: 8:2                # Figma 입력일 때
viewport:
  primary: mobile             # mobile | tablet | desktop
  responsive: [mobile]        # 지원 폼팩터
---
```

### Phase 1A: Figma 기반 스크린 추출 (가장 효율적 입력)
Figma URL이 주어진 경우, 다음 절차로 화면을 분석합니다 (Figma MCP 호출 비용을 최소화).

1. **노드 ID 파싱**: `node-id=X-Y` → `X:Y`
2. **`get_design_context(fileKey, nodeId)` 1콜** — 가장 풍부한 응답. 다음을 한 번에 얻음:
   - 화면 스크린샷 (시각 검증용)
   - 자동 생성 React 코드 + Tailwind (구조 힌트로만 사용, 결과물엔 포함 X)
   - Code Connect 매핑 (있으면 컴포넌트 매칭에 직접 활용)
   - Annotation, Variable 참조
3. **`get_screenshot`은 기본 생략** — `get_design_context`에 이미 포함됨. 별도 영역 검증이 필요할 때만 추가 호출.
4. **호출 한도 절약**: 한 화면 = 한 콜 원칙. 자식 노드를 또 호출하지 마세요.

### Phase 1B: 스크린샷 + 설명 기반 (폴백)
Figma 입력 없이 스크린샷·설명만 있는 경우:
- 스크린샷의 시각 위계를 region/section으로 식별
- 사용자에게 의도/플로우 질문으로 보완
- 디자인 시스템 컴포넌트 카탈로그에서 가장 가까운 매칭 선택

### Phase 1C: 기존 코드 기반
이미 React/HTML로 화면이 있는 경우:
- JSX 트리를 region/section으로 매핑
- 인라인 스타일·매그닉넘버를 디자인 시스템 토큰으로 환원
- 비표준 컴포넌트는 가장 가까운 DS 컴포넌트로 매핑하거나 "Custom" 마커

### Phase 2: 3-Layer 명세 작성

각 스크린 .md는 **Skeleton / Bindings / Intent** 3개 레이어를 가집니다 — 형식은 [components/TEMPLATE.md](assets/scaffold/screens/TEMPLATE.md) 참조. 레이아웃 문법은 [references/layout_grammar.md](references/layout_grammar.md), 컴포넌트 매핑 규칙은 [references/binding_rules.md](references/binding_rules.md).

**2.1 Skeleton (구조 골격)**
- 레이아웃 그리드와 컴포넌트 슬롯의 위계 트리
- 각 슬롯은 베이스 DS 컴포넌트 .md를 직접 참조 (예: `components/01-button.md`)
- Custom 영역은 `<Custom name="...">`로 표기

**2.2 Bindings (구체값 결합)**
- 각 슬롯의 variant, size, state, content를 명시
- 모든 색상/간격은 베이스 DS의 Semantic Token만 참조
- raw 값(`#xxxxxx`, `Npx`) 금지 — 환원 못 하면 디자인 시스템에 토큰 추가 PR 후보로 표시

**2.3 Intent (의도/접근성/플로우)**
- 사용자 의도, 화면 진입/이탈 트리거
- 핵심 액션 우선순위
- 접근성 주석 (포커스 순서, 스크린 리더 의도, reduced motion 등)
- 짧은 산문 OK (이 섹션만)

### Phase 3: 검증

> ⚠️ **이 단계는 단발 점검이 아니라 루프입니다.** 검증 실패 항목이 0이 될 때까지 Phase 2와 본 단계를 반복합니다.

**3.1 자동 검증 실행 (필수)**
```
python3 skills/screen-spec-gen/scripts/validate_screen.py screens/{project}/
```
스크립트가 다음을 자동 점검합니다:
- frontmatter 유효성 (yaml 파싱 + extends 디렉토리 존재)
- 모든 `↳ component:` 참조가 실제 .md 파일에 매칭
- 모든 `color/...`, `spacing/...`, `radius/...` 등 토큰 참조가 베이스 DS의 foundations에 존재
- Bindings 섹션에 raw hex(`#xxxxxx`) 없음 (Figma Make 코드블록 / Custom 슬롯 제외)

**종료 코드 0**(전체 통과)이어야 Phase 3을 종료할 수 있습니다.

**3.2 실패 시 루프 동작**
- **컴포넌트 참조 실패**: 해당 컴포넌트가 실제로 누락 → DS에 컴포넌트 명세 추가 (`design-system-gen` 스킬 활용) 또는 `<Custom>` 마커로 명시적 표기
- **토큰 참조 실패**: 베이스 DS의 foundations에 정식 토큰으로 추가 → `design-systems/{brand}/foundations/00-color.md` 등에 정식 표 추가 후 재검증
- **raw 값 실패**: 토큰 환원이 안 된 raw 값을 Bindings에서 제거 → DS 토큰 사용 또는 `<Custom>` 처리
- **자동 점검 미통과 0건**이 될 때까지 반복

**3.3 수동 점검 (자동 도구가 못 잡는 항목)**
[references/validation_checklist.md](references/validation_checklist.md)에서 자동 점검 외 항목:
- viewport별 분기(responsive)가 frontmatter `responsive`와 일치
- Intent 섹션의 사용자 의도 / 진입·이탈 / 핵심 액션 우선순위 / 접근성 주석 채움
- 인터랙티브 슬롯에 on-tap/on-change 등 트리거 명시

### Phase 4: 인덱스 + 플로우
스크린이 여러 개면 `screens/00-INDEX.md`에 다음을 작성:
- 화면 목록과 흐름 다이어그램(Mermaid)
- 각 화면 간 전이(transition) 트리거
- 사용된 컴포넌트의 빈도 통계 (DS의 어느 부분이 가장 많이 쓰이는지 파악)

## 📜 주요 규칙 (Core Rules)

- **Framework-Neutral**: React/Flutter/Vue 같은 프레임워크 키워드를 결과물 본문에 사용하지 마세요. JSX 같은 코드 블록도 금지. 컴포넌트는 항상 디자인 시스템 .md 경로로 참조합니다.
- **DS 참조 원칙**: 모든 컴포넌트 슬롯은 `design-systems/{brand}/components/NN-xxx.md`로 직접 링크. 슬롯 안에서 인라인 스타일 정의 금지.
- **Semantic Token Only**: Bindings의 모든 값은 Semantic Token. raw 값을 못 환원하면 *디자인 시스템 보강이 먼저*입니다 (스크린 명세보다 우선순위 높음).
- **Custom 영역 명시**: DS에 없는 요소는 `<Custom>`으로 명시 — 추후 DS에 합류 후보 트래킹.
- **Mix Discipline**: 여러 DS를 섞을 땐 frontmatter `imports`에 명시. 인라인으로 다른 DS 토큰 참조 금지.
- **명세는 코드가 아니다**: `.md` 안에 React/Flutter 코드 작성 금지. 구조 위계는 들여쓰기 트리 또는 YAML 블록으로 표현.
