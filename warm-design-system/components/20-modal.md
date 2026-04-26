# 컴포넌트: 모달 / 다이얼로그 (Modal)

## 개요
특정 작업이나 확인에 사용자 집중을 유도하는 오버레이 패널.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 배경 | `color/surface/1` |
| 보더 반경 | `radius/modal` = 16px |
| 그림자 | `shadow/modal` |
| 최대 너비 | 480px |
| 여백 | 16px (뷰포트 가장자리) |
| 오버레이 | `color/surface/overlay` = rgba(26,25,22,0.48) |
| 등장 모션 | `motion/scale` = 200ms spring, scale(0.95)+translateY(8px) → scale(1) |
| 퇴장 모션 | `motion/fade` = 200ms ease-out |

---

## 구조
- **헤더**: 제목 (18px / SemiBold) + 닫기 버튼 (✕, 우측 상단)
  - 패딩: 20px 24px 16px
  - 하단 보더: `color/border/subtle`
- **본문**: 콘텐츠, 14px / Regular, `color/text/secondary`
  - 패딩: 20px 24px
- **푸터**: 액션 버튼, 우측 정렬
  - 패딩: 16px 24px 20px
  - 상단 보더: `color/border/subtle`

---

## 동작
- 오버레이 클릭으로 모달 닫기
- Escape 키로 닫기
- 모달이 열린 동안 포커스 트랩
- 모달 열릴 때 본문 스크롤 잠금

---

## Figma Make 프롬프트

```
다음 스펙으로 모달/다이얼로그(Modal) 컴포넌트를 만들어줘:

크기: 최대 너비 480px, 뷰포트 중앙 정렬
배경: 흰색 / 다크 서피스
보더 반경: 16px
강한 드롭 섀도우
모달 뒤 반투명 어두운 오버레이

구조:
- 헤더: 제목 (18px SemiBold) + ✕ 닫기 버튼, 하단 보더
- 본문: 콘텐츠 영역 (14px 회색 텍스트), 패딩 20px 24px
- 푸터: 우측 정렬 액션 버튼 (취소 + 확인), 상단 보더

동작:
- 팝인 애니메이션: 0.95에서 스케일 + 약간 위로 슬라이드
- 오버레이 동시 페이드인

변형:
- 확인 (위험 버튼 포함)
- 정보 (Primary 버튼만)

네이밍: Modal / Default, Modal / Danger
```
