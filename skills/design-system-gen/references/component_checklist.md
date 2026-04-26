# 🧩 표준 컴포넌트 체크리스트 (Component Checklist)

이 문서는 디자인 시스템이 일관되게 다뤄야 하는 **표준 컴포넌트 카탈로그**입니다. SKILL.md Phase 3에서 이 체크리스트를 끝까지 순회하며 각 항목을 처리합니다.

## 🔁 운영 규칙 (Loop Protocol)

Phase 3에서 에이전트는 다음 루프를 따릅니다:

1. 입력(HTML/CSS or Figma)에서 발견된 모든 UI 요소를 이 체크리스트에 매핑합니다.
2. 각 카테고리를 위에서부터 순회하며, **모든 항목**에 대해 다음 셋 중 하나로 결정을 내립니다:
   - **✅ Documented** — `components/NN-xxx.md`로 작성 완료
   - **⏭️ Skipped (reason)** — 이 디자인 시스템 범위에서 의도적으로 제외 (이유 명시)
   - **⛔ N/A** — 입력에 해당 요소가 전혀 없고 디자인 시스템 무드와도 무관
3. 단, **Tier 1(필수) 카테고리의 항목은 N/A 불가**입니다 — 입력에 명시적으로 없더라도 시스템의 무드에 맞춰 디폴트로 정의해야 합니다 (디자인 시스템의 "기본 가구").
4. 루프 종료 조건: **모든 항목이 위 셋 중 하나로 결정**되어야 합니다. 미결정 항목이 있으면 다시 1단계로.
5. 최종 산출물 상단(예: `components/00-INDEX.md`)에 체크리스트 결과를 표로 보고합니다.

---

## 📋 표준 카탈로그

### Tier 1 — 필수 (Must Document)

> 이 항목들은 거의 모든 제품 UI에 등장하므로, 입력에 없더라도 시스템 무드에 맞춰 정의합니다.

#### A. Actions / Inputs (인터랙티브)
- [ ] Button — 기본 액션
- [ ] Icon Button — 아이콘 전용 버튼
- [ ] Input — 텍스트 입력 (single-line)
- [ ] Textarea — 텍스트 입력 (multi-line)
- [ ] Select / Dropdown — 옵션 선택
- [ ] Checkbox — 다중 선택
- [ ] Radio — 단일 선택
- [ ] Toggle / Switch — 이진 토글

#### B. Display / Status (정적 표시)
- [ ] Badge / Tag — 상태·카테고리 라벨
- [ ] Avatar — 사용자/엔티티 아바타
- [ ] Label — 폼 라벨, 작은 헬퍼 텍스트
- [ ] Divider — 구분선

#### C. Feedback (사용자 피드백)
- [ ] Alert — 인라인 메시지 (info/success/warning/error)
- [ ] Toast / Snackbar — 일시적 알림
- [ ] Spinner — 로딩 스피너
- [ ] Progress Bar — 진행률 표시
- [ ] Skeleton — 로딩 플레이스홀더
- [ ] Empty State — 빈 상태 안내

#### D. Containers (구성 컨테이너)
- [ ] Card — 카드 컨테이너
- [ ] Modal / Dialog — 중앙 오버레이
- [ ] Tooltip — 호버 보조 정보

---

### Tier 2 — 권장 (Strongly Recommended)

> 제품 종류에 따라 빠질 수 있지만, 빠질 경우 명시적 Skip 사유 필요.

#### E. Containers (확장)
- [ ] Drawer / Sheet — 사이드 오버레이
- [ ] Tabs — 탭 전환
- [ ] Accordion / Disclosure — 접기/펼치기
- [ ] Popover — 호버/클릭 보조 패널

#### F. Navigation (탐색)
- [ ] Breadcrumb — 경로 표시
- [ ] Pagination — 페이지 이동
- [ ] Menu / Dropdown Menu — 컨텍스트 메뉴
- [ ] Nav Item / Sidebar Item — 사이드 내비게이션 항목

#### G. Data Display (데이터)
- [ ] Table — 데이터 테이블
- [ ] List Item — 리스트 행 단일 단위
- [ ] Stat Card — 지표 강조 카드
- [ ] Chip — 인터랙티브 태그 (제거 가능)

---

### Tier 3 — 선택 (Optional, Domain-Specific)

> 제품 도메인에 따라 필요한 경우만 추가. N/A 처리 자유롭게 가능.

- [ ] Date Picker — 날짜 선택
- [ ] Time Picker — 시간 선택
- [ ] File Uploader — 파일 업로드
- [ ] Slider — 범위 슬라이더
- [ ] Stepper — 단계형 진행 표시
- [ ] Command Palette — 명령 검색 인터페이스
- [ ] Code Block — 코드 표시
- [ ] Kbd — 키보드 키 표시
- [ ] Tree View — 트리 구조 표시
- [ ] Calendar — 달력 뷰

---

## 📑 결과 보고 형식

Phase 3 완료 시 `components/00-INDEX.md`에 다음 형식으로 보고합니다:

```markdown
# Component Index

| # | Component | Tier | Status | File / Reason |
|---|---|---|---|---|
| 01 | Button | 1 | ✅ Documented | [01-button.md](01-button.md) |
| 02 | Icon Button | 1 | ✅ Documented | [02-icon-button.md](02-icon-button.md) |
| .. | Drawer | 2 | ⏭️ Skipped | 모바일 전용 제품으로 사이드 오버레이 미사용 |
| .. | Date Picker | 3 | ⛔ N/A | 도메인 무관 |
```

이 인덱스는 결과물의 **완결성 증거**이자 후속 작업자의 진입점이 됩니다.

---

## 🔗 관련 문서
- 각 컴포넌트의 필수 state는 [state_matrix.md](state_matrix.md)를 따릅니다.
- 작성 형식은 `components/TEMPLATE.md`를 엄격히 준수합니다.
