# 컴포넌트: 토글 / 스위치 (Toggle)

## 개요
설정 및 기능 플래그를 위한 이진 ON/OFF 컨트롤.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 트랙 (OFF) | `color/border/strong` |
| 트랙 (ON) | `color/primary/default` |
| 썸 | #FFFFFF |
| 썸 그림자 | 0 1px 3px rgba(0,0,0,0.15) |
| 모션 | 100ms ease-out (썸 슬라이드) |

---

## 크기

| 크기 | 트랙 너비 | 트랙 높이 | 썸 크기 | 이동 거리 |
|---|---|---|---|---|
| Medium (기본) | 40px | 24px | 18×18px | 16px |
| Large | 52px | 30px | 24×24px | 22px |

---

## 상태

| 상태 | 트랙 | 썸 위치 |
|---|---|---|
| OFF | 회색 (`color/border/strong`) | 좌측 (3px 여백) |
| ON | 오렌지 (`color/primary/default`) | 우측 (3px 여백) |
| 비활성 OFF | 40% 불투명도, 회색 | 좌측 |
| 비활성 ON | 40% 불투명도, 오렌지 | 우측 |
| 포커스 | 트랙에 `shadow/focus` |

---

## 레이블 포함 패턴
- 토글 좌측, 레이블 우측, 10px 간격
- 레이블: 14px / Regular

## 설정 목록 패턴
- 전체 너비 행: 레이블+설명 좌측, 토글 우측
- 레이블: 14px / Medium
- 설명: 12px / Regular, `color/text/tertiary`
- 행 패딩: 14px 20px
- 하단 보더: 1px `color/border/subtle`

---

## Figma Make 프롬프트

```
다음 스펙으로 토글/스위치(Toggle) 컴포넌트를 만들어줘:

Medium 크기: 트랙 40×24px, 썸 18×18px
Large 크기: 트랙 52×30px, 썸 24×24px

트랙 색상:
- OFF: 회색 (#D4D1CA 라이트 / #47443E 다크)
- ON: 오렌지 (#F26A00 라이트 / #FF8A1E 다크)

썸: 흰색 원형, 미세한 그림자
썸이 좌측 (OFF)에서 우측 (ON)으로 슬라이드

상태: OFF, ON, 비활성 OFF, 비활성 ON
포커스: 트랙에 3px 오렌지 링

레이블 포함 변형: 토글 + 텍스트 레이블 나란히

설정 목록 패턴:
- 제목 + 설명 좌측, 토글 우측의 행
- 미세한 하단 보더로 구분

네이밍: Toggle / {크기} / {상태}
```
