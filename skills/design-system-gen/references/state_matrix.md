# 🎚️ 컴포넌트 상태 매트릭스 (State Matrix)

각 컴포넌트가 필수로 다뤄야 하는 **상태(State)와 인터랙션 패턴**의 표준 매트릭스입니다. SKILL.md Phase 3에서 컴포넌트별 명세를 작성할 때 이 표를 따라 누락 없이 채워야 합니다.

> 카테고리 분류는 [component_checklist.md](component_checklist.md)와 동일합니다.

---

## 📐 상태 키 정의

| 키 | 의미 | 시각 신호 |
|---|---|---|
| **Default** | 기본 렌더링 상태 | — (기준점) |
| **Hover** | 포인터 진입 | 배경/색상 변화 |
| **Focus** | 키보드 포커스 | `shadow/focus` 또는 outline (필수) |
| **Active / Pressed** | 클릭 중 / 탭 다운 | 배경/색상 더 짙게 |
| **Disabled** | 비활성 | 불투명도 또는 회색조 |
| **Loading** | 비동기 처리 중 | 스피너 또는 Skeleton |
| **Error** | 검증/입력 오류 | 에러 보더 + 메시지 |
| **Success** | 검증/처리 완료 | 성공 보더 또는 체크 |
| **Selected / Active** | 선택됨 / 활성 탭 | 강조 보더 또는 배경 |
| **Open / Expanded** | 열림 / 펼쳐짐 | 컨텐츠 노출 + 화살표 회전 등 |
| **Closed / Collapsed** | 닫힘 / 접힘 | 컨텐츠 숨김 |
| **Indeterminate** | 부분 선택 / 진행률 미상 | 중간 표시 (예: Checkbox `-`) |

`■` = 필수 / `●` = 권장 / `○` = 해당 없음

---

## 🅰️ Actions / Inputs (인터랙티브)

| 컴포넌트 | Default | Hover | Focus | Active | Disabled | Loading | Error |
|---|---|---|---|---|---|---|---|
| Button | ■ | ■ | ■ | ■ | ■ | ■ | ○ |
| Icon Button | ■ | ■ | ■ | ■ | ■ | ● | ○ |
| Input | ■ | ● | ■ | ○ | ■ | ● | ■ |
| Textarea | ■ | ● | ■ | ○ | ■ | ● | ■ |
| Select | ■ | ■ | ■ | ■ (Open) | ■ | ● | ■ |
| Checkbox | ■ | ■ | ■ | ○ | ■ | ○ | ■ |
| Radio | ■ | ■ | ■ | ○ | ■ | ○ | ■ |
| Toggle / Switch | ■ | ■ | ■ | ○ | ■ | ● | ○ |

**추가 규칙:**
- 모든 Input/Textarea/Select/Checkbox/Radio: `Selected` 또는 `Filled` 상태도 별도로 명시.
- Checkbox/Radio는 `Indeterminate`(체크박스만), `Selected` 변형 필수.
- Select는 `Open` 상태에서 옵션 리스트의 Hover/Selected 상태도 함께 명세.

---

## 🅱️ Display / Status (정적 표시)

| 컴포넌트 | Default | Hover | Focus | Disabled | Variants 필수 |
|---|---|---|---|---|---|
| Badge / Tag | ■ | ○ | ○ | ○ | ■ (info/success/warning/error/neutral 최소 5종) |
| Avatar | ■ | ● | ○ | ○ | ■ (size 최소 3종 + 이미지 없음 폴백) |
| Label | ■ | ○ | ○ | ■ | ● (required 표시) |
| Divider | ■ | ○ | ○ | ○ | ● (가로/세로) |

---

## 🆎 Feedback (피드백)

| 컴포넌트 | Default | Variants 필수 | 모션 필수 |
|---|---|---|---|
| Alert | ■ | ■ (info/success/warning/error) | ● (등장) |
| Toast / Snackbar | ■ | ■ (info/success/warning/error) | ■ (slide/fade in-out) |
| Spinner | ■ | ● (size 최소 2종) | ■ (회전) |
| Progress Bar | ■ + Indeterminate | ● (값 0/50/100% 예시) | ■ (값 변화) |
| Skeleton | ■ | ● (text/circle/rect 형태) | ■ (shimmer 또는 pulse) |
| Empty State | ■ | ● (illustration/icon 변형) | ○ |

---

## 🅳 Containers (컨테이너)

| 컴포넌트 | Closed | Open | Focus Trap | Backdrop | 모션 필수 |
|---|---|---|---|---|---|
| Card | ■ Default | — | ○ | ○ | ● (Hover lift 등) |
| Modal / Dialog | ■ | ■ | ■ (필수) | ■ | ■ (등장/퇴장) |
| Drawer / Sheet | ■ | ■ | ■ | ■ | ■ (slide) |
| Tabs | — | ■ Selected/Unselected | ■ | ○ | ● (전환) |
| Accordion | ■ Collapsed | ■ Expanded | ■ | ○ | ■ (높이) |
| Popover | ■ Closed | ■ Open | ● | ○ | ● (fade/scale) |
| Tooltip | ■ Hidden | ■ Visible | ● (키보드 진입 시) | ○ | ● (delay + fade) |

**추가 규칙:**
- Modal/Drawer는 **Focus Trap, Esc 닫기, 배경 스크롤 락** 행동을 접근성 섹션에 반드시 명세.
- Tabs는 `Selected` 상태가 시각적으로 명확히 구분되어야 함 (보더 또는 배경).

---

## 🅴 Navigation (탐색)

| 컴포넌트 | Default | Hover | Focus | Active / Current | Disabled |
|---|---|---|---|---|---|
| Breadcrumb item | ■ | ■ | ■ | ■ (current page) | ○ |
| Pagination button | ■ | ■ | ■ | ■ (current page) | ■ (prev/next 끝) |
| Menu Item | ■ | ■ | ■ | ■ (selected) | ■ |
| Nav Item / Sidebar Item | ■ | ■ | ■ | ■ (current route) | ● |

---

## 🅵 Data Display (데이터)

| 컴포넌트 | Default | Hover | Focus | Selected | Variants 필수 |
|---|---|---|---|---|---|
| Table row | ■ | ■ | ● | ■ (선택형 테이블 시) | ● (striped/borderless) |
| Table cell | ■ | ○ | ○ | ○ | ● (정렬 헤더 / 데이터) |
| List Item | ■ | ■ | ■ | ■ | ● (with leading / trailing) |
| Stat Card | ■ | ● | ○ | ○ | ● (positive/negative trend) |
| Chip | ■ | ■ | ■ | ■ | ■ (removable / selectable) |

---

## 📜 공통 규칙 (Cross-Cutting)

1. **Focus Ring 필수**: 키보드 포커스가 가능한 모든 컴포넌트는 `shadow/focus` 또는 동등한 outline을 명세에 포함합니다 (WCAG 2.1).
2. **모션 토큰**: Hover/Active/Loading 등 상태 변화에는 `motion/*` 토큰을 참조해 transition을 명세합니다. 미모션은 명시적으로 "no transition"이라고 적습니다.
3. **명암비**: Default/Hover/Active의 텍스트–배경 명암비가 모두 WCAG AA 이상이어야 합니다 (큰 텍스트는 3:1, 본문은 4.5:1).
4. **Touch Target**: 인터랙티브 컴포넌트는 최소 터치 영역 44×44px를 충족합니다 (모바일 고려).
5. **상태 누락 검증**: 컴포넌트 명세에서 위 매트릭스의 ■(필수) 항목 중 누락된 것이 있으면 작성을 끝내지 않습니다.
