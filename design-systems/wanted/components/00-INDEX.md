# Component Index

이 문서는 [component_checklist.md](../../../skills/design-system-gen/references/component_checklist.md)의 표준 카탈로그에 대한 본 인스턴스의 결정 결과 보고입니다.

> **Note**: 본 wanted 인스턴스는 **시범 처리(8개)** 단계의 결과입니다. 원본 wds 패키지에는 84개 컴포넌트가 있으나, 본 명세 작업은 Phase 3 흐름 검증을 위해 Tier 1 핵심 8개만 처리했습니다. 나머지는 후속 마이그레이션 대상.

## 📊 요약
- **Tier 1 (필수)**: 8 / 18 ✅ Documented · 10 ⏳ Pending (시범 단계라 보류)
- **Tier 2 (권장)**: 모두 ⏳ Pending
- **Tier 3 (선택)**: 일부 wds에 존재하나 본 시범 단계에서 미처리

---

## Tier 1 — 필수

| # | Component | Tier | Status | File / Reason | wds 원본 |
|---|---|---|---|---|---|
| 01 | Button | 1 | ✅ Documented | [01-button.md](01-button.md) | `components/button` |
| — | Icon Button | 1 | ⏳ Pending | wds의 `icon-button` 별도 존재 (Button의 iconOnly와 별개) | `components/icon-button` |
| 02 | Text Field (Input) | 1 | ✅ Documented | [02-text-field.md](02-text-field.md) | `components/text-field` |
| — | Textarea | 1 | ⏳ Pending | wds의 `text-area` 존재 | `components/text-area` |
| — | Select / Dropdown | 1 | ⏳ Pending | wds의 `select`, `select-multiple`, `autocomplete` 존재 | `components/select` |
| 03 | Checkbox | 1 | ✅ Documented | [03-checkbox.md](03-checkbox.md) | `components/checkbox` |
| — | Radio | 1 | ⏳ Pending | wds의 `radio`, `radio-group` 존재 | `components/radio` |
| — | Toggle / Switch | 1 | ⏳ Pending | wds의 `switch`, `toggle-icon` 존재 | `components/switch` |
| — | Badge / Tag | 1 | ⏳ Pending | wds의 `content-badge`, `play-badge`, `push-badge` 존재 | `components/content-badge` |
| — | Avatar | 1 | ⏳ Pending | wds의 `avatar`, `avatar-button`, `avatar-group` 존재 | `components/avatar` |
| — | Label | 1 | ⏳ Pending | wds의 `label` 존재 | `components/label` |
| — | Divider | 1 | ⏳ Pending | wds의 `divider` 존재 | `components/divider` |
| — | Alert | 1 | ⏳ Pending | wds의 `alert`, `section-message` 존재 | `components/alert` |
| 08 | Toast / Snackbar | 1 | ✅ Documented | [08-snackbar.md](08-snackbar.md) | `components/snackbar` |
| — | Spinner | 1 | ⏳ Pending | wds의 `loading`, `progress-indicator` 존재 | `components/loading` |
| — | Progress Bar | 1 | ⏳ Pending | wds의 `progress-tracker`, `progress-step-indicator` 존재 | `components/progress-tracker` |
| — | Skeleton | 1 | ⏳ Pending | wds의 `skeleton` 존재 (Card에서 부분 명세) | `components/skeleton` |
| — | Empty State | 1 | ⏳ Pending | wds의 `fallback-view` 존재 | `components/fallback-view` |
| 06 | Card | 1 | ✅ Documented | [06-card.md](06-card.md) | `components/card`, `card-list` |
| 07 | Modal / Dialog | 1 | ✅ Documented | [07-modal.md](07-modal.md) | `components/modal` |
| 05 | Tooltip | 1 | ✅ Documented | [05-tooltip.md](05-tooltip.md) | `components/tooltip` |

---

## Tier 2 — 권장

| Component | Status | wds 원본 | Note |
|---|---|---|---|
| Drawer / Sheet | ⏳ Pending | (Modal `bottom` variant로 일부 커버) | wds Modal의 bottom variant가 sheet 역할 — 별도 마이그레이션 가능 |
| Tabs | ⏳ Pending | `components/tab` | |
| Accordion / Disclosure | ⏳ Pending | `components/accordion` | |
| Popover | ⏳ Pending | `components/popover`, `popper` | |
| Breadcrumb | ⏳ Pending | (없음) | wds에 직접 컴포넌트 없음 — 추가 가능성 |
| Pagination | ⏳ Pending | `components/pagination`, `pagination-dots`, `page-counter` | |
| Menu / Dropdown Menu | ⏳ Pending | `components/menu` | |
| Nav Item / Sidebar Item | ⏳ Pending | `components/top-navigation`, `bottom-navigation` | |
| Table | ⏳ Pending | `components/table` | |
| List Item | ⏳ Pending | `components/list` | |
| Stat Card | ⏳ Pending | (없음) | Card 합성으로 표현 가능 |
| 04 | ✅ Documented | `components/chip` | [04-chip.md](04-chip.md) — Tier 2지만 시범 단계에 포함 |

---

## Tier 3 — 선택

wds 원본에 존재하는 도메인 특화 컴포넌트 (모두 ⏳ Pending):
- `date-calendar`, `date-picker`, `date-range-calendar`, `date-range-picker`
- `time-picker`, `time-view`
- `slider`
- `stepper`
- `segmented-control`
- `search-field`
- `category`
- `filter-button`
- `top-navigation`, `bottom-navigation` (Tier 2와 중복)

---

## 🔄 본 시범 단계의 의미

이 8개 컴포넌트로 다음을 검증했습니다:

1. **Phase 0 → 4 흐름 작동**: 입력(코드) → 스캐폴드 → foundations → 컴포넌트 → 인덱스
2. **Phase 0.5 스캐폴드**: 결과 디렉토리에 README/AGENTS/docs/TEMPLATE이 일관되게 생성됨
3. **Phase 2 토큰 매핑**: Atomic/Semantic 두 레이어 구조가 우리 스킬 가정과 정합
4. **Phase 3 컴포넌트 명세**: state_matrix.md의 ■ 필수 상태와 Container 가드(Modal/Tooltip 명시적 상태 표) 적용
5. **Tier 1 카탈로그 매핑**: 표준 카탈로그가 실제 production 디자인 시스템과 잘 맞아떨어짐 (84 컴포넌트가 거의 모두 매핑 가능)

**누락 발견**: wds에는 `breadcrumb`, `stat-card`가 직접 존재하지 않음 — 우리 카탈로그 Tier 2에서 정당한 ⏭️ Skipped 사유가 됨 (또는 유사 컴포넌트로 대체 가능 표시).

후속: 본 카탈로그를 모두 ✅로 채우려면 80여 컴포넌트를 더 명세화하면 됨. 본 시범 단계의 패턴을 따르면 1 컴포넌트당 ~5분 작업 견적.
