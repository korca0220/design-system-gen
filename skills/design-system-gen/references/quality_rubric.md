# 📊 품질 자가평가 루브릭 (Quality Rubric)

[quality_criteria.md](quality_criteria.md)의 4대 기준에 대해 **0~3점 척도로 객관 채점**하는 루브릭입니다. SKILL.md Phase 4에서 에이전트가 이 루브릭을 따라 자가 채점하고, 결과물 루트에 `quality_report.md`로 저장합니다.

---

## 🎯 채점 척도

| 점수 | 의미 |
|---|---|
| **3** | 우수 — 의도된 디자인 결정으로 보임 |
| **2** | 양호 — 표준 기준은 충족, 개선 여지 있음 |
| **1** | 부족 — 명확히 개선 필요 |
| **0** | 미달 — 핵심 기준 위반 |

---

## 1. 디자인 품질 (Design Quality)

> 응집력 있는 하나의 결과물로 느껴지는가?

| 점수 | 신호 |
|---|---|
| 3 | 핵심 컬러·타이포·간격이 한 무드로 통합. README의 "Design Philosophy" 한 줄이 결과물 전체에서 느껴짐 |
| 2 | 무드는 인지 가능하지만, 1~2개 컴포넌트가 톤에서 이탈 |
| 1 | 토큰은 정의돼 있으나 무드가 모호함. "범용 디자인 시스템"처럼 보임 |
| 0 | 컬러/타이포 결정이 충돌하거나 산만 |

**자동 점검 항목** (모두 통과해야 ≥2점):
- [ ] 키 컬러가 단 하나로 선언됨 (Brand color collision 없음)
- [ ] Surface tone이 키 컬러와 같은 hue family에 있음 (예: 따뜻한 brand → 따뜻한 neutral)
- [ ] README.md의 "Design Philosophy" 필드가 채워짐

---

## 2. 독창성 (Originality)

> 관습적 패턴을 탈피한 고유한 결정이 있는가?

| 점수 | 신호 |
|---|---|
| 3 | 최소 2개 이상의 의도적이고 비관습적인 디자인 결정 (예: 비대칭 보더 반경, 독특한 모션 곡선, 절제된 포커스 표현) |
| 2 | 1개의 비관습적 결정 또는 일관된 사소한 디테일들 |
| 1 | 라이브러리 기본값에 근접 (Tailwind defaults, Material defaults 등의 직접 차용) |
| 0 | "AI Slop" 패턴 — 흰 카드 + 보라 그라데이션 + Inter 폰트의 일반화 조합 |

**자동 점검 항목**:
- [ ] 폰트 패밀리가 Inter / SF Pro / Roboto 외 (or 의도적 선택 사유 명시)
- [ ] 키 컬러가 #3B82F6 (Tailwind blue-500) / #6366F1 (indigo-500) 외
- [ ] 그림자 색이 순수 검정이 아닌 brand-tinted

---

## 3. 크래프트 (Craft)

> 기술적 실행 완성도가 높은가?

| 점수 | 신호 |
|---|---|
| 3 | 모든 토큰이 4px/8px 그리드 정합. 폰트 위계 명확. 명암비 모두 WCAG AA+ |
| 2 | 그리드/위계 대체로 정합, 1~2개 예외 |
| 1 | 그리드 이탈 다수. 폰트 사이즈 단계가 5개 미만이거나 너무 촘촘 |
| 0 | 매그닉 넘버 다수, 명암비 미달 |

**자동 점검 항목**:
- [ ] 모든 spacing 값이 [heuristics_html_css.md](heuristics_html_css.md)의 표준 스케일에 포함됨 (또는 명시적 사유)
- [ ] 폰트 사이즈가 5~9단계 사이 (위계가 풍부한 시스템은 의도된 초과 허용 — 그 사유를 quality_report에 명시)
- [ ] **명암비 자동 검증** — [scripts/check_contrast.py](../scripts/check_contrast.py)를 실행하여 핵심 색상 페어를 검증:
  - `color/text/primary` × `color/surface/1` (Light/Dark 둘 다) ≥ 7:1 (AAA 권장)
  - `color/text/secondary` × `color/surface/1` (Light/Dark 둘 다) ≥ 4.5:1 (AA)
  - `color/primary/normal` 위 텍스트 (보통 white) ≥ 4.5:1
  - `color/text/disabled` × `color/surface/1` ≥ 3:1 (큰 텍스트 기준)
  - 검증 페어를 `design-systems/{brand}/contrast_pairs.txt`로 작성 후 `python3 skills/design-system-gen/scripts/check_contrast.py design-systems/{brand}/contrast_pairs.txt` 실행
  - 실패가 0이어야 ✅. 결과를 `quality_report.md`에 첨부.
- [ ] 모든 인터랙티브 컴포넌트에 `shadow/focus` 또는 동등 outline 명세

---

## 4. 기능성 (Functionality)

> 사용하기 편리한가?

| 점수 | 신호 |
|---|---|
| 3 | 모든 인터랙티브 컴포넌트가 [state_matrix.md](state_matrix.md)의 ■ 상태를 누락 없이 명세. 접근성 섹션 완비 |
| 2 | ≥ 95% 컴포넌트가 ■ 상태 충족, 일부 누락 |
| 1 | 절반 이상 컴포넌트가 상태 누락 또는 접근성 섹션 부재 |
| 0 | Hover/Focus/Disabled 같은 기본 상태가 거의 명세되지 않음 |

> **부분 처리 (Partial Instance) 보정 규칙**: 시범/단계적 작업으로 Tier 1 일부만 ✅ Documented이고 나머지가 ⏳ Pending인 경우, **"명세된 컴포넌트들 자체의 품질"로만 채점**합니다. 미명세 컴포넌트의 부재는 Functionality 점수가 아닌 **별도 "Completeness 점수"**로 분리해 보고합니다 (아래 합격선 섹션 참조). 이렇게 하면 "잘 만든 8개"가 "급하게 만든 18개"보다 점수가 낮아지는 역설을 방지합니다.

**자동 점검 항목**:
- [ ] `components/00-INDEX.md`의 모든 항목이 ✅/⏭️/⛔로 결정됨
- [ ] 컨테이너 컴포넌트(Modal/Drawer/Tooltip 등)가 명시적 **상태 표** 포함 (산문 설명만으로 갈음 ❌)
- [ ] 모든 폼 컴포넌트가 Error 상태 명세
- [ ] Modal/Drawer의 접근성 섹션에 Focus Trap, Esc, 스크롤 락 명시

---

## 📋 Phase 4 자가 리포트 템플릿

Phase 4 종료 시 다음 형식으로 `design-systems/{brand}/quality_report.md`를 작성합니다:

```markdown
# Quality Report — {{Brand Name}}

생성 일자: {{YYYY-MM-DD}}
입력 종류: {{html-css | figma | raw}}

## 점수 요약
| 기준 | 점수 | 비고 |
|---|---|---|
| Design Quality | _/3 | [한 줄 평가] |
| Originality | _/3 | [한 줄 평가] |
| Craft | _/3 | [한 줄 평가] |
| Functionality | _/3 | [한 줄 평가] |
| **합계** | **_/12** | |

## Completeness
- Tier 1: _ / _ ✅
- Tier 2: _ / _ ✅
- 환산 비율: _% → **{{Full | High | Mid | Pilot | Skeleton}}** 등급

## 자동 점검 결과
[각 기준의 자동 점검 체크박스 결과]

## 명암비 검증
- 검증 페어 파일: `contrast_pairs.txt`
- 통과 / 전체: _ / _
- 실패 페어: [없음 또는 목록]
- 실행 명령: `python3 skills/design-system-gen/scripts/check_contrast.py contrast_pairs.txt`

## 토큰 환원율
- Semantic 토큰 참조 수: _
- 컴포넌트 명세에서 raw hex/픽셀 등장 수 (Figma Make 블록 제외): _
- **환원율: _% ** (기준: ≥ 80% 권장, < 60%면 경고)

## 개선 권고
[1점 이하 항목에 대한 구체적 권고. 없으면 "없음"]

## 합격선 판정
[Production-ready / Production-ready (with caveats) / 검수 필요 — 사유와 함께]
```

---

## 🚨 합격선

다음 중 **하나라도 해당하면** 결과물을 사용자에게 "**검수 필요**"로 분류해 보고합니다:

- 4대 기준 합계 점수 < 8/12
- 어느 한 기준이라도 ≤ 1
- Functionality의 자동 점검 항목 중 미통과 존재
- **명암비 자동 검증 실패** ([check_contrast.py](../scripts/check_contrast.py) 종료 코드 ≠ 0)
- 토큰 환원율 < 60%

합격선을 통과해야 결과물이 "production-ready"로 분류됩니다.

---

## 📈 Completeness 점수 (부분 처리 인스턴스용)

부분 처리 인스턴스(Tier 1 일부만 ✅)는 합격선과는 별도로 **Completeness 점수**를 보고합니다 — *"이 시스템이 얼마나 완성됐는가"*를 별도 차원으로 추적.

```
Completeness = (✅ Documented 수) / (✅ + ⏳ Pending 수, ⛔ N/A는 분모 제외)
```

| 등급 | 비율 | 분류 |
|---|---|---|
| Full | 100% | "production-ready" 필수 조건 |
| High | ≥ 80% | "production-ready (with caveats)" |
| Mid | 50~79% | "preview" — 핵심은 됐으나 보강 필요 |
| Pilot | 25~49% | "시범 단계" — 흐름 검증 목적 |
| Skeleton | < 25% | "scaffold only" — 더 작업 필요 |

`quality_report.md`의 "합격선 판정" 섹션에 4대 기준 점수와 함께 Completeness 등급도 명시합니다.
