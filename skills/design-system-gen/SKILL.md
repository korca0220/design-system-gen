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
- **(C) Source Code Repository** (GitHub 레포 URL 또는 로컬 클론) → Phase 1C로 진행 — 토큰/컴포넌트가 코드로 정의된 가장 정확한 입력

> **사전 확인 (Optional)**: 사용자가 (A) 또는 (B)를 제시했더라도, 해당 디자인 시스템이 **OSS로 공개된 코드 레포가 있는지 한 번 물어보세요**. 있다면 (C)로 전환하는 게 압도적으로 효율적입니다 (Figma 호출 한도 무시, 100% 정확). 한국 사례: wanted/montage-web, toss/slash, daangn-design-system 등. 사용자가 모르면 "GitHub에서 회사명 + design-system 검색해보시겠어요?" 정도만 제안하고 없으면 원래 분기로 진행.

### Phase 0.5: 스캐폴드 생성 (Scaffold)
Phase 1로 들어가기 전에, 결과물 디렉토리의 베이스 구조를 [`assets/scaffold/`](assets/scaffold/)에서 복사하여 만듭니다. 이 단계는 모든 인스턴스가 동일한 디렉토리 구조와 운영 문서(README/AGENTS/docs)를 갖도록 보장합니다.

**복사 절차:**
1. `assets/scaffold/`의 모든 파일/디렉토리를 `design-systems/{brand-name}/`로 복사합니다 (단, `SCAFFOLD.md`는 제외 — 스캐폴드 자체의 사용법 문서이므로 결과물에 포함하지 않음).
2. `README.md`와 `AGENTS.md` 안의 `{{...}}` 플레이스홀더를 Phase 1에서 결정한 값으로 치환합니다:
   - `{{Brand Name}}`, `{{Brand Color}}`, `{{Primary Typeface}}`, 디자인 무드, 입력 종류, Figma URL 등.
3. `TEMPLATE.md`로 끝나는 파일은 **치환하지 않고 그대로** 둡니다 (사용자가 새 컴포넌트를 추가할 때 참조하는 형식 기준).

**필수 산출 파일 (스캐폴드 복사 후 모두 존재해야 함):**
- `README.md`, `AGENTS.md`
- `foundations/TEMPLATE.md`, `components/TEMPLATE.md`
- `docs/README.md`, `docs/adr/TEMPLATE.md`, `docs/exec-plans/TEMPLATE.md`

이후 Phase 2/3에서 실제 `foundations/00-*.md`와 `components/NN-*.md`를 채워 넣습니다.

### Phase 1A: HTML/CSS 기반 브랜드 아이덴티티 및 토큰 분석 (Discovery)
입력된 HTML/CSS나 디자인 설명에서 고유한 브랜드 아이덴티티와 디자인 패턴을 식별합니다. **구체적 추출 규칙은 [references/heuristics_html_css.md](references/heuristics_html_css.md)에 정의되어 있으며, Phase 1A는 그 문서를 따라 진행합니다.**

요약:
- **브랜드 키 컬러 식별**: 빈도 + 채도 + 위치(CTA/링크/활성) 가중치로 단 하나의 키 컬러 결정
- **색상 군집화**: 6개 카테고리(Brand/Neutral/Surface/Success/Warning/Danger), ΔE < 5 또는 HSL 거리 기준으로 통합
- **간격 그리드 추정**: 모든 padding/margin/gap의 GCD로 base unit(보통 4 or 8) 결정 후 표준 스케일로 환원
- **타이포 스케일**: 폰트 사이즈 비율 분석 → 모듈러 스케일 또는 표준 단계로 환원
- **보더 반경 / 그림자 / 모션**: 각각 4~5단계로 elevation/intensity 단계화

산출 후 **[quality_rubric.md](references/quality_rubric.md)의 자동 점검 항목**과 정합한지 곧바로 확인합니다 (예: 폰트 패밀리 ≤ 2개, 그리드 정합 등).

### Phase 1B: Figma 기반 토큰 및 컴포넌트 추출 (Discovery — Figma MCP)
Figma URL이 주어진 경우, Figma MCP의 도구를 사용해 디자인 시스템을 직접 읽어옵니다. 자세한 절차는 [references/figma_extraction.md](references/figma_extraction.md)를 따릅니다.

순서:
1. **URL 파싱**: `fileKey`, `nodeId` 추출 (`node-id`의 `-`를 `:`로 변환).
2. **변수 우선 추출** — `mcp__claude_ai_Figma__get_variable_defs`로 Variables(Color/Number/String 등)를 먼저 가져옵니다. 토큰이 변수화되어 있다면 이 결과가 그대로 `foundations/`의 Primitive/Semantic 매핑이 됩니다 (가장 큰 레버리지).
3. **컴포넌트 인덱스** — `mcp__claude_ai_Figma__search_design_system` 또는 `get_metadata`로 컴포넌트/세트 목록을 가져옵니다. 컴포넌트 수가 많으면 사용자에게 어떤 항목을 문서화할지 **반드시 확인**하세요 (한 번에 전체 처리는 비효율).
4. **컴포넌트별 컨텍스트** — 선택된 각 컴포넌트에 대해 `mcp__claude_ai_Figma__get_design_context` + `get_screenshot`을 호출하여 variants/states/anatomy를 추출합니다.
5. **토큰 폴백** — Variables가 없거나 raw hex/absolute layout이 다수면, 스크린샷 + Phase 1A의 휴리스틱으로 폴백합니다. 이 경우 환원율이 낮음을 사용자에게 명시적으로 경고하세요.

### Phase 1C: 코드 레포 기반 추출 (Discovery — Source Repository)
GitHub URL 또는 로컬 경로가 주어진 경우, 코드를 직접 읽어 토큰과 컴포넌트를 추출합니다. 디자이너 의도가 코드로 박제된 상태이므로 휴리스틱이 거의 필요 없습니다.

**클론**:
- 공개 레포: `git clone --depth 1 <url> /tmp/<repo-name>` (얕은 클론으로 충분)
- 작업 종료 후 정리 (`rm -rf`) 권장 — 결과물에 소스 코드 포함하지 않음

**탐색 순서**:
1. **README / package.json** — 모노레포 여부, 패키지 구조 파악
2. **테마/토큰 패키지 식별** — `theme`, `tokens`, `design-tokens`, `foundations` 키워드로 디렉토리 탐색
3. **토큰 파일 분석** — TS/JS export, JSON, CSS 변수, Tailwind config 등 형식별로 직접 매핑
4. **컴포넌트 패키지 식별** — `components`, `ui`, `lib` 등에서 카탈로그 추출
5. **`types.ts` / Props 타입** — variant/size/state를 가장 정확하게 알려주는 1차 소스
6. **`style.ts` / CSS-in-JS / className** — 실제 토큰 참조 패턴 추출

**휴리스틱 폴백**: 토큰이 코드로 명시적이지 않은 부분(예: inline `border-radius: 12px`)은 [heuristics_html_css.md](references/heuristics_html_css.md)의 군집화 규칙으로 표준 단계로 환원합니다. 추정 토큰은 foundations 명세에 "Inferred" 라벨 명시.

**출처 기록**: README.md "출처" 섹션에 레포 URL, 라이선스, 분석 패키지 경로를 명시합니다 (재현성 확보).

### Phase 2: 파운데이션 수립 (Foundations)
추출된 토큰을 `foundations/` 디렉토리에 명세화합니다.
- `foundations/TEMPLATE.md` 형식을 엄격히 준수하세요.
- **Primitive vs Semantic**: 값 그 자체(Primitive)와 역할 기반 이름(Semantic)을 분리하여 정의합니다.
- **토큰 명명 규칙**: [references/token_naming.md](references/token_naming.md) 가이드를 따릅니다.

### Phase 3: 컴포넌트 명세 작성 (Components)

> ⚠️ **이 단계는 단발성 작업이 아니라 체크리스트 루프입니다.** 모든 항목이 결정될 때까지 반복합니다.

**3.1 표준 카탈로그 순회 — 체크리스트 루프**
[references/component_checklist.md](references/component_checklist.md)의 표준 카탈로그(Tier 1 → Tier 2 → Tier 3)를 위에서부터 끝까지 순회합니다. 각 항목에 대해 반드시 다음 셋 중 하나로 결정을 내리고, **미결정 항목이 단 하나라도 있으면 Phase 3을 종료할 수 없습니다**:
- ✅ **Documented** — `components/NN-xxx.md` 작성 완료
- ⏭️ **Skipped (reason)** — 의도적 제외, 사유 명시
- ⛔ **N/A** — 도메인 무관 (단 Tier 1은 N/A 불가)

**3.2 컴포넌트별 명세 작성**
각 Documented 항목을 작성할 때:
- `components/TEMPLATE.md` 형식을 엄격히 준수합니다.
- [references/state_matrix.md](references/state_matrix.md)의 해당 카테고리 행에서 ■(필수) 표시된 모든 상태를 누락 없이 명세합니다. 누락된 ■ 항목이 있으면 컴포넌트 작성을 끝내지 않습니다.
- **변형(Variants)**: Primary, Secondary, Ghost 등 디자인 옵션을 분류합니다.
- **모션 토큰**: 상태 전환에 `motion/*` 토큰 참조를 명시합니다.
- ⚠️ **컨테이너 컴포넌트 가드 (Modal/Drawer/Popover/Tooltip/Accordion/Tabs)**: "헤더/본문/푸터" 같은 구조 설명이나 동작 산문(prose)으로 상태를 갈음하지 마세요. 반드시 `components/TEMPLATE.md`의 **상태 표 형식**(`| 상태 | 시각 표현 / 변경 토큰 | 모션 토큰 |`)으로 Closed/Open/Focus Trap/Backdrop/Motion 등 [state_matrix.md](references/state_matrix.md)의 해당 행을 그대로 표 한 줄씩 채워야 합니다. 동작 설명은 표와 별개의 **접근성 섹션**으로 분리합니다.

**3.3 인덱스 보고**
Phase 3을 닫기 전에 `components/00-INDEX.md`에 체크리스트 결과를 표로 보고합니다 (형식은 [component_checklist.md](references/component_checklist.md#-결과-보고-형식) 참조). 이 인덱스는 결과물 완결성의 증거이자 후속 작업자의 진입점입니다.

### Phase 4: 품질 검증 및 브릿지 (Validation & Bridge)

**4.1 자가 채점 (Self-Scoring)**
[references/quality_rubric.md](references/quality_rubric.md)의 4대 기준 × 0~3점 척도로 채점하고, 각 기준의 자동 점검 항목을 체크합니다. 결과는 `design-systems/{brand}/quality_report.md`에 루브릭의 템플릿 형식으로 작성합니다.

**4.2 체크리스트 완결성**
`components/00-INDEX.md`의 모든 행이 ✅/⏭️/⛔로 결정되어 있는지 확인합니다. 빈 행이 있으면 Phase 3로 되돌아갑니다.

**4.3 상태 매트릭스 준수**
각 컴포넌트가 [state_matrix.md](references/state_matrix.md)의 ■(필수) 항목을 모두 다뤘는지 점검합니다. 컨테이너 컴포넌트는 산문이 아닌 명시적 상태 표 형식이어야 합니다 (Phase 3.2 가드).

**4.4 토큰 환원율 (Token Coverage) — 계산식**
다음 공식으로 계산하고 `quality_report.md`에 기록합니다:

```
환원율 = (Semantic 토큰 참조 수) / (Semantic 토큰 참조 수 + raw 값 등장 수)
```

- **분자 (Semantic 토큰 참조 수)**: 모든 `components/*.md`에서 `color/...`, `spacing/...`, `radius/...`, `text/...`, `motion/...`, `shadow/...` 형식으로 참조된 토큰 등장 횟수의 총합
- **분모의 raw 값 등장 수**: 컴포넌트 명세 본문에서 `#xxxxxx` hex, `Npx` 픽셀 리터럴, `rgba(...)` 등 토큰화되지 않은 값의 등장 횟수
  - 예외: `Figma Make 프롬프트` 코드 블록 안의 값은 제외 (디자이너용 산문이라 raw가 자연스러움)
  - 예외: foundations 파일의 Primitive 정의 자체는 분모에 포함하지 않음 (raw 값이 *정의되는* 위치이지 *사용되는* 위치가 아님)

**임계값:**
- ≥ 80%: 권장 합격선
- 60 ~ 79%: 양호하나 개선 여지 (어떤 컴포넌트에 raw 값이 남아있는지 보고)
- < 60%: ⚠️ **경고** — 사용자에게 입력 품질 문제를 즉시 보고하고, 결과물을 "검수 필요"로 분류

**4.5 명암비 자동 검증**
핵심 색상 페어를 `design-systems/{brand}/contrast_pairs.txt`에 적고 [scripts/check_contrast.py](scripts/check_contrast.py)로 검증합니다:
```
python3 skills/design-system-gen/scripts/check_contrast.py design-systems/{brand}/contrast_pairs.txt
```
종료 코드 0 (모두 통과)이어야 합격선 통과입니다. 결과를 `quality_report.md`에 기록.

**4.6 Completeness 등급**
부분 처리 인스턴스는 [quality_rubric.md의 Completeness](references/quality_rubric.md#-completeness-점수-부분-처리-인스턴스용) 비율로 등급(Full/High/Mid/Pilot/Skeleton)을 산정해 보고합니다. 4대 기준 점수와 별개의 차원입니다.

**4.7 합격선 판정**
[quality_rubric.md의 합격선](references/quality_rubric.md#-합격선)을 모두 통과하면 결과물을 "production-ready"로 분류합니다. 하나라도 위배되면 "검수 필요"로 표기하고 사용자에게 우선순위 개선 항목을 제안합니다.

**4.8 Figma Make 프롬프트**
각 컴포넌트 하단에 디자이너가 바로 활용할 수 있는 상세한 Figma 생성 프롬프트를 포함합니다.

## 📜 주요 규칙 (Core Rules)
- **Output Path**: 결과물은 항상 `design-systems/{brand-name}/` 하위에 작성합니다. 레포 루트에 직접 작성하지 마세요.
- **Semantic Token Only**: 컴포넌트 명세 작성 시 반드시 Semantic Token만을 참조해야 합니다.
- **No Magic Numbers**: 모든 수치는 `foundations`의 스페이싱/폰트 시스템 내의 값으로 치환하십시오.
- **Accessible Design**: 명암비 및 키보드 접근성(Focus Ring) 명세를 반드시 포함하세요.
- **Figma 우선순위**: Figma 입력의 경우 Variables → Component metadata → Screenshot 휴리스틱 순으로 신뢰합니다. Variables로 환원 가능한 값을 절대 raw hex로 적지 마세요.
- **체크리스트 우선**: Phase 3는 [component_checklist.md](references/component_checklist.md)의 모든 항목이 결정될 때까지 종료할 수 없습니다. 단발 추출이 아닌 루프로 동작합니다.
- **상태 매트릭스 강제**: 컴포넌트 명세는 [state_matrix.md](references/state_matrix.md)의 ■ 표시 상태를 모두 포함해야 합니다.
