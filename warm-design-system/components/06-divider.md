# 컴포넌트: 구분선 (Divider)

## 개요
콘텐츠 섹션을 구분하는 얇은 선. 가로 또는 세로 방향.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 기본 색상 | `color/border/default` |
| 강조 색상 | `color/border/strong` |
| 미묘 색상 | `color/border/subtle` |
| 두께 | 1px |

---

## 변형

### 가로 — 기본 (Default)
- 너비: 부모 100%, 높이: 1px
- 색상: `color/border/default`

### 가로 — 강조 (Strong)
- 색상: `color/border/strong`
- 사용처: 강한 섹션 구분

### 가로 — 미묘 (Subtle)
- 색상: `color/border/subtle`
- 사용처: 목록 항목 구분, 저강조

### 가로 — 레이블 포함
- 가운데 텍스트 레이블 좌우로 선 연장
- 레이블: 12px / Regular, `color/text/tertiary`
- 선과 레이블 사이 12px 간격
- 사용처: "또는", "OR" 구분선

### 세로 (Vertical)
- 너비: 1px, 높이: 부모에 맞춤
- 좌우 여백: 각 8px
- 사용처: 인라인 요소 구분

---

## 접근성
- `role="separator"` 또는 `<hr>` 요소 사용
- 장식용 구분선: `aria-hidden="true"`

---

## Figma Make 프롬프트

```
다음 스펙으로 구분선(Divider) 컴포넌트를 만들어줘:

가로 구분선:
- 기본: 1px, #E8E6E1(라이트) / rgba(255,255,255,0.10)(다크)
- 강조: 1px, 더 진한 색상
- 미묘: 1px, 매우 연한 색상
- 레이블 포함: 선 + 가운데 텍스트 레이블(12px 회색), 양쪽으로 선 연장

세로 구분선:
- 1px 너비, 부모 높이 전체, 좌우 여백 8px

두께 1px, 가로는 100% 너비, 세로는 100% 높이

네이밍: Divider / Horizontal / {변형}, Divider / Vertical
```
