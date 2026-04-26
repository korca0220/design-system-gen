# ✅ 스크린 명세 검증 체크리스트 (Validation Checklist)

각 스크린 .md 작성 후 Phase 3에서 점검합니다. 모든 항목 통과해야 "framework-neutral consumable"로 분류.

---

## 📋 Frontmatter

- [ ] `name` 채워짐
- [ ] `extends` 가 유효한 디자인 시스템 인스턴스 (해당 디렉토리 존재 확인)
- [ ] `imports`에 적힌 모든 경로가 실제 .md 파일에 매칭
- [ ] `source.type` ∈ {figma, screenshot, code}
- [ ] `viewport.primary` ∈ `viewport.responsive`

## 📐 Skeleton

- [ ] 트리가 5단계 위계(Page→Region→Section→Slot→Component)를 따름
- [ ] 모든 Slot이 Component 또는 `<Custom>` 마커로 끝남
- [ ] 컴포넌트 참조 경로가 실제 .md 파일 존재 (예: `design-systems/wanted/components/01-button.md`)
- [ ] `<Custom name="...">` 영역의 name이 비어있지 않음
- [ ] viewport별 분기가 frontmatter `responsive`와 일치

## 🔗 Bindings

- [ ] 모든 색상/패딩/반경/그림자가 Semantic Token (`color/...`, `spacing/...`, `radius/...`, `shadow/...`)
- [ ] **raw hex (`#xxxxxx`) 가 Bindings 섹션에 없음**
- [ ] **raw 픽셀 리터럴 (`Npx`) 이 Bindings 섹션에 없음** (예외: `<Custom>` 내부)
- [ ] 모든 `text-variant`가 베이스 DS의 typography variant와 매칭
- [ ] 인터랙티브 슬롯에 `on-tap` / `on-change` / `on-submit` 중 하나는 명시 (장식 요소면 명시 안 해도 됨)
- [ ] 데이터 바인딩 `{{path}}`의 path가 일관성 있음 (오타 검증은 데이터 모델이 있을 때)

## 🎯 Intent

- [ ] **사용자 의도** 1~2문장 작성됨
- [ ] **진입 / 이탈** 트리거 명시
- [ ] **핵심 액션 우선순위** 최소 1개 작성
- [ ] **포커스 순서** 명시 (인터랙티브 요소 ≥ 2개일 때)
- [ ] **터치 타겟** 가이드 명시 (최소 44×44px 또는 명시적 예외)
- [ ] **Reactive Behavior** — 적어도 Loading/Empty 둘 중 하나는 명시 (정적 화면 제외)

## 🧪 자동 점검 (스크립트로 검증 가능한 항목)

스크립트(`scripts/validate_screen.py`, 향후 추가)로 자동 검증할 항목들:

- [ ] 모든 `↳ component:` 참조가 파일 시스템에 존재
- [ ] 모든 `color/...` / `spacing/...` 등 토큰이 베이스 DS의 foundations 파일 본문에 존재
- [ ] frontmatter 파싱 성공 (yaml 유효)
- [ ] Bindings 본문에서 hex/px 정규식 매칭 시 모두 코드 블록 또는 `<Custom>` 안

> **자동 검증 스크립트는 후속 작업 — 우선은 사람이 체크리스트 따라 점검**.

---

## 🚨 합격선

- 모든 frontmatter / Skeleton / Bindings 체크박스 ✅
- Intent 체크박스 중 ≥ 4/5 ✅ (한두 개 누락은 허용 — 시범 단계)
- 미충족 항목 있으면 `quality_report.md`에 명시하고 "검수 필요"로 분류
