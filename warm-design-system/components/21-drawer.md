# 컴포넌트: 드로어 / 시트 (Drawer)

## 개요
보조 콘텐츠나 액션을 위해 화면 가장자리에서 슬라이드 인하는 사이드 패널.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 배경 | `color/surface/1` |
| 그림자 | `shadow/modal` |
| 너비 | 360px (최대 90vw) |
| 오버레이 | `color/surface/overlay` |
| 모션 | `motion/page` = 300ms ease-out (translateX) |

---

## 구조
- **헤더**: 제목 (18px / SemiBold) + 닫기 버튼
  - 패딩: 20px 24px
  - 하단 보더: `color/border/subtle`
  - flex-shrink: 0
- **본문**: 스크롤 가능한 콘텐츠 영역
  - 패딩: 20px 24px
  - flex: 1, overflow-y: auto
- **푸터**: 액션 버튼 (전체 너비)
  - 패딩: 16px 24px
  - 상단 보더: `color/border/subtle`
  - flex-shrink: 0

---

## 위치
- **우측** (기본): 우측 가장자리에서 슬라이드 인
- **하단** (모바일): 하단에서 슬라이드 업 (바텀 시트)

---

## Figma Make 프롬프트

```
다음 스펙으로 드로어/사이드 패널(Drawer) 컴포넌트를 만들어줘:

너비: 360px, 전체 뷰포트 높이
위치: 우측 가장자리 고정
배경: 흰색 / 다크 서피스
좌측 가장자리에 강한 그림자

구조 (전체 높이 flex 컬럼):
- 헤더: 제목 (18px SemiBold) + ✕ 닫기 버튼, 하단 보더
- 본문: 스크롤 가능한 콘텐츠, 패딩 20px 24px
- 푸터: 나란한 두 버튼 (취소 + 저장), 상단 보더

슬라이드인 애니메이션: 우측에서 300ms ease-out

모바일 변형: 바텀 시트
- 전체 너비, 하단 고정
- 상단 모서리 둥글게 (24px)
- 하단에서 슬라이드 업

네이밍: Drawer / Right, Drawer / Bottom Sheet
```
