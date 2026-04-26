# Component Index

이 문서는 [component_checklist.md](../../../skills/design-system-gen/references/component_checklist.md)의 표준 카탈로그에 대한 본 인스턴스의 결정 결과 보고입니다. 모든 항목은 ✅ Documented / ⏭️ Skipped(reason) / ⛔ N/A 중 하나로 결정되어야 하며, Tier 1은 N/A 불가입니다.

## 📊 요약
- **Tier 1 (필수)**: 18 / 18 ✅
- **Tier 2 (권장)**: 8 Documented / 4 Skipped
- **Tier 3 (선택)**: 모두 N/A (현재 도메인 무관)

---

## Tier 1 — 필수

| # | Component | Tier | Status | File / Reason |
|---|---|---|---|---|
| 01 | Button | 1 | ✅ Documented | [01-button.md](01-button.md) |
| 02 | Icon Button | 1 | ✅ Documented | [02-icon-button.md](02-icon-button.md) |
| 08 | Input | 1 | ✅ Documented | [08-input.md](08-input.md) |
| 09 | Textarea | 1 | ✅ Documented | [09-textarea.md](09-textarea.md) |
| 10 | Select / Dropdown | 1 | ✅ Documented | [10-select.md](10-select.md) |
| 11 | Checkbox | 1 | ✅ Documented | [11-checkbox.md](11-checkbox.md) |
| 12 | Radio | 1 | ✅ Documented | [12-radio.md](12-radio.md) |
| 13 | Toggle / Switch | 1 | ✅ Documented | [13-toggle.md](13-toggle.md) |
| 03 | Badge / Tag | 1 | ✅ Documented | [03-badge-tag.md](03-badge-tag.md) |
| 04 | Avatar | 1 | ✅ Documented | [04-avatar.md](04-avatar.md) |
| 29 | Label | 1 | ✅ Documented | [29-label.md](29-label.md) |
| 06 | Divider | 1 | ✅ Documented | [06-divider.md](06-divider.md) |
| 14 | Alert | 1 | ✅ Documented | [14-alert.md](14-alert.md) |
| 15 | Toast / Snackbar | 1 | ✅ Documented | [15-toast.md](15-toast.md) |
| 05 | Spinner | 1 | ✅ Documented | [05-spinner.md](05-spinner.md) |
| 16 | Progress Bar | 1 | ✅ Documented | [16-progress-bar.md](16-progress-bar.md) |
| 17 | Skeleton | 1 | ✅ Documented | [17-skeleton.md](17-skeleton.md) |
| 18 | Empty State | 1 | ✅ Documented | [18-empty-state.md](18-empty-state.md) |
| 19 | Card | 1 | ✅ Documented | [19-card.md](19-card.md) |
| 20 | Modal / Dialog | 1 | ✅ Documented | [20-modal.md](20-modal.md) |
| 07 | Tooltip | 1 | ✅ Documented | [07-tooltip.md](07-tooltip.md) |

---

## Tier 2 — 권장

| Component | Status | File / Reason |
|---|---|---|
| Drawer / Sheet | ✅ Documented | [21-drawer.md](21-drawer.md) |
| Tabs | ✅ Documented | [22-tabs.md](22-tabs.md) |
| Accordion / Disclosure | ⏭️ Skipped | warm v1 범위 외 — 빠른 전환이 필요한 짧은 콘텐츠 패턴이 현 도메인에 없음. 향후 FAQ/설정 화면 도입 시 추가 예정. |
| Popover | ⏭️ Skipped | Tooltip(07)과 Modal(20)이 1차 보조 정보 패턴을 커버. 클릭 트리거 보조 패널 수요가 발생하면 추가. |
| Breadcrumb | ✅ Documented | [23-breadcrumb.md](23-breadcrumb.md) |
| Pagination | ✅ Documented | [24-pagination.md](24-pagination.md) |
| Menu / Dropdown Menu | ⏭️ Skipped | Select(10)이 옵션 선택을 커버하고 컨텍스트 메뉴 패턴이 현 v1에 없음. 우클릭/툴바 메뉴 도입 시 추가. |
| Nav Item / Sidebar Item | ⏭️ Skipped | warm v1은 사이드 내비게이션이 없는 단일 페이지 제품 가정. 다중 페이지/관리자 콘솔 확장 시 추가. |
| Table | ✅ Documented | [25-table.md](25-table.md) |
| List Item | ✅ Documented | [26-list-item.md](26-list-item.md) |
| Stat Card | ✅ Documented | [27-stat-card.md](27-stat-card.md) |
| Chip | ✅ Documented | [28-chip.md](28-chip.md) |

---

## Tier 3 — 선택

| Component | Status | Reason |
|---|---|---|
| Date Picker | ⛔ N/A | 도메인 무관 (v1) |
| Time Picker | ⛔ N/A | 도메인 무관 (v1) |
| File Uploader | ⛔ N/A | 도메인 무관 (v1) |
| Slider | ⛔ N/A | 도메인 무관 (v1) |
| Stepper | ⛔ N/A | 도메인 무관 (v1) |
| Command Palette | ⛔ N/A | 도메인 무관 (v1) |
| Code Block | ⛔ N/A | 도메인 무관 (v1) |
| Kbd | ⛔ N/A | 도메인 무관 (v1) |
| Tree View | ⛔ N/A | 도메인 무관 (v1) |
| Calendar | ⛔ N/A | 도메인 무관 (v1) |

---

## 🔄 다음 마이그레이션 후보
도입을 검토 중인 컴포넌트는 위 ⏭️ Skipped 항목 중에서 사유가 해소된 시점에 다시 이 인덱스를 갱신하여 ✅로 전환합니다.
