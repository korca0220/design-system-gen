# 컴포넌트: 툴팁 (Tooltip)

## 개요
호버 또는 포커스 시 나타나 요소에 대한 추가 맥락을 제공하는 작은 플로팅 레이블.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 배경 | `color/text/primary` (반전 색상) |
| 텍스트 색상 | `color/surface/1` (반전) |
| 폰트 | 12px / Regular 400 |
| 패딩 | 6px 10px |
| 보더 반경 | `radius/tooltip` = 6px |
| 그림자 | `shadow/dropdown` |
| 트리거와의 간격 | 8px |
| 모션 | `motion/fade` = 200ms ease-out |

---

## 위치

### 상단 (기본)
- 트리거 요소 위에 나타남
- 아래 방향 화살표(▼) 하단 중앙
- 등장: opacity 0→1, translateY(4px)→0, 200ms ease-out

### 하단
- 트리거 요소 아래에 나타남
- 위 방향 화살표(▲) 상단 중앙

---

## 화살표
- 크기: 5px 정삼각형
- 색상: 툴팁 배경색과 동일
- 트리거 방향 가장자리에 중앙 정렬

---

## 접근성
- 툴팁 요소에 `role="tooltip"` 사용
- 트리거는 `aria-describedby`로 툴팁 ID 참조
- 키보드 접근성 필수 (포커스 시 표시)

---

## Figma Make 프롬프트

```
다음 스펙으로 툴팁(Tooltip) 컴포넌트를 만들어줘:

외형:
- 배경: 어두운 색상(#1A1916 라이트 / #FAFAF8 다크) — 페이지 배경 반전
- 텍스트: 흰색/밝은 색상 (12px Regular)
- 패딩: 6px 10px, 보더 반경: 6px
- 엘리베이션용 드롭 섀도우

위치: 상단(기본), 하단
- 트리거를 향하는 5px 삼각형 화살표
- 툴팁과 트리거 사이 8px 간격

동작:
- 호버/포커스 시 표시
- 페이드 인: opacity 0→1 + 약간의 translateY, 200ms
- 최대 너비 240px

네이밍: Tooltip / Top, Tooltip / Bottom
```
