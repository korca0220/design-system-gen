# 컴포넌트: 프로그레스 바 (Progress Bar)

## 개요
작업 완료율 또는 진행 상태를 시각적으로 표시하는 인디케이터.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 트랙 배경 | `color/surface/3` |
| 보더 반경 | `radius/badge` = 9999px (필 형태) |
| 모션 | 너비 변화 시 600ms cubic-bezier(0,0,0.2,1) |

---

## 크기

| 크기 | 높이 |
|---|---|
| Small (sm) | 4px |
| Medium (md, 기본) | 8px |
| Large (lg) | 12px |

---

## 색상 변형

| 변형 | 채움 색상 | 사용처 |
|---|---|---|
| Primary | `color/primary/default` | 일반 진행 상태 |
| 성공 | `color/success/default` | 완료 상태 |
| 경고 | `color/warning/default` | 한계 근접 경고 |
| 오류 | `color/error/default` | 실패 또는 초과 |

---

## 확정형 (퍼센트 값 있음)
- 헤더 행: 레이블 좌측 + 퍼센트 우측 (13px / Medium)
- 트랙 아래
- 채움 너비 = 트랙 너비의 퍼센트

## 비확정형 (소요 시간 미정)
- 퍼센트 표시 없음
- 채움 애니메이션: translateX(-100%) → translateX(350%) 무한 반복
- 채움 너비 고정 40%

---

## Figma Make 프롬프트

```
다음 스펙으로 프로그레스 바(Progress Bar) 컴포넌트를 만들어줘:

트랙: 연한 회색 배경 (#F4F3F0), 필 형태 (전체 보더 반경)
채움: 트랙 내부 컬러 필 형태

크기: Small (4px), Medium (8px), Large (12px)

색상 변형:
- Primary: 오렌지 (#F26A00)
- 성공: 초록 (#0D9144)
- 경고: 앰버 (#F59E0B)
- 오류: 빨간색 (#E8321E)

헤더 포함: 레이블 텍스트 좌측, "72%" 퍼센트 우측 (13px Medium)

비확정형 변형: 슬라이딩 채움 애니메이션, 퍼센트 없음

네이밍: Progress / {변형} / {크기}
```
