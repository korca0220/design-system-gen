# 컴포넌트: 스피너 (Spinner)

## 개요
처리 중인 상태를 나타내는 로딩 인디케이터.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 주요 색상 | `color/primary/default` |
| 트랙 색상 | `color/border/default` |
| 애니메이션 | spin 700ms linear infinite |

---

## 원형 스피너 크기

| 크기 | 가로 × 세로 | 보더 두께 |
|---|---|---|
| XL | 40 × 40px | 3px |
| Large (lg) | 32 × 32px | 3px |
| Medium (md) | 24 × 24px | 2.5px |
| Small (sm) | 18 × 18px | 2px |
| XS | 14 × 14px | 2px |

---

## 색상 변형

| 변형 | 호 색상 | 사용처 |
|---|---|---|
| Primary | `color/primary/default` (오렌지) | 기본 |
| 무채색 (Muted) | `color/text/secondary` (회색) | 저강조 |
| 흰색 (White) | #FFFFFF | 어두운/컬러 배경 위 |

---

## 점 스피너
- 3개 점 가로 배열, 각 7×7px, `color/primary/default`
- 간격: 5px
- 순차적 바운스 애니메이션 (딜레이: -0.32s, -0.16s, 0s)

---

## 사용 지침
- 전체 페이지/섹션 로딩 → 원형 스피너
- 인라인/최소 로딩 → 점 스피너
- 버튼 로딩 상태 내부 → 흰색 변형
- `aria-busy="true"`, `aria-label="로딩 중"` 함께 사용

---

## Figma Make 프롬프트

```
다음 스펙으로 스피너(Spinner) 로딩 인디케이터 컴포넌트를 만들어줘:

원형 스피너:
크기: XL(40px), Large(32px), Medium(24px), Small(18px), XS(14px)
구조: 회색 트랙 + 오렌지 활성 호(상단), 700ms linear 무한 회전

색상 변형:
- Primary: 오렌지 호(#F26A00 라이트 / #FF8A1E 다크)
- 무채색: 회색 호
- 흰색: 흰색 호(어두운 배경 위)

점 스피너:
오렌지 7px 원형 3개, 5px 간격, 순차적 바운스 애니메이션

네이밍: Spinner / Circle / {크기}, Spinner / Dots
```
