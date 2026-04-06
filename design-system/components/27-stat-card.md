# 컴포넌트: 스탯 카드 (Stat Card)

## 개요
레이블과 트렌드 인디케이터가 포함된 핵심 지표 표시 카드.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 배경 | `color/surface/1` |
| 보더 | 1px solid `color/border/default` |
| 보더 반경 | `radius/card` = 12px |
| 패딩 | 18px 20px |
| 레이블 폰트 | 12px / Medium 500, `color/text/tertiary`, 대문자 |
| 값 폰트 | 28px / Bold 700, 자간 -0.02em |
| 변화 폰트 | 12px / Regular |

---

## 구조
1. **레이블**: 12px Medium 대문자, `color/text/tertiary`
   - 하단 여백: 8px
2. **값**: 28px Bold, `color/text/primary`
   - 하단 여백: 6px
3. **변화 인디케이터**: 트렌드 화살표 + 퍼센트 텍스트
   - 증가: ↑ + `color/success/text` 텍스트
   - 감소: ↓ + `color/error/text` 텍스트
   - 중립: — + `color/text/tertiary` 텍스트

---

## 그리드 레이아웃
- 일반적으로 2~4열 그리드에서 사용
- 각 카드: 최소 너비 180px

---

## Figma Make 프롬프트

```
다음 스펙으로 스탯 카드/KPI 카드(Stat Card) 컴포넌트를 만들어줘:

배경: 흰색 / 다크 서피스
보더: 1px 연한 회색, 보더 반경 12px
패딩: 18px 20px

콘텐츠:
1. 레이블: 12px Medium 대문자 회색 텍스트 (예: "총 사용자")
2. 값: 28px Bold 대형 숫자 (예: "12,482")
3. 변화: 트렌드 화살표가 있는 소형 텍스트
   - ↑ 초록 텍스트 증가 (예: "↑ 12.5% 지난 달 대비")
   - ↓ 빨간 텍스트 감소
   - — 회색 텍스트 중립

그리드: 4개 카드로 구성된 4열 레이아웃 예시

네이밍: Stat Card / Positive, Stat Card / Negative, Stat Card / Neutral
```
