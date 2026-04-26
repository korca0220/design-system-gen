# 컴포넌트: 뱃지 / 태그 (Badge / Tag)

## 개요
뱃지는 상태를 나타내는 비인터랙티브 표시자. 태그는 카테고리 분류를 위한 제거 가능한 레이블.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 보더 반경 | `radius/badge` = 9999px (필 형태) |
| 폰트 굵기 | Medium 500 |

---

## 뱃지 크기

| 크기 | 폰트 | 패딩 |
|---|---|---|
| Large (lg) | 13px | 4px 12px |
| Medium (md) | 12px | 3px 10px |
| Small (sm) | 11px | 2px 8px |

---

## 뱃지 색상 변형

| 변형 | 배경 | 텍스트 |
|---|---|---|
| Primary | `color/primary/tint` | `color/primary/default` |
| 성공 (Success) | `color/success/tint` | `color/success/text` |
| 경고 (Warning) | `color/warning/tint` | `color/warning/text` |
| 오류 (Error) | `color/error/tint` | `color/error/text` |
| 정보 (Info) | `color/info/tint` | `color/info/text` |
| 중립 (Neutral) | `color/surface/3` | `color/text/secondary` |

---

## 상태 점 포함 변형
- 텍스트 좌측에 6px 원형 점
- 점 색상은 해당 변형의 메인 색상
- 점과 텍스트 사이 4px 간격

---

## 태그 (제거 가능)

### 구조
- 레이블 텍스트 (12px / 500)
- 우측에 제거 버튼 (✕) — 14×14px 원형
- 패딩: 3px 8px 3px 10px

### 외형
- 배경: `color/surface/3`
- 보더: 1px solid `color/border/default`
- 텍스트: `color/text/secondary`
- 제거 버튼 호버: `color/error/default` 배경, 흰색 아이콘

---

## 접근성
- 뱃지: `role="status"` 또는 설명적 `aria-label`
- 태그 제거 버튼: `aria-label="[태그명] 제거"`

---

## Figma Make 프롬프트

```
다음 스펙으로 뱃지(Badge)와 태그(Tag) 컴포넌트를 만들어줘:

뱃지:
크기: Large (13px, 4px 12px), Medium (12px, 3px 10px), Small (11px, 2px 8px)
보더 반경: 9999px (필 형태)
폰트: Pretendard Medium 500

색상 변형:
- Primary: 오렌지 틴트 배경(#FFE4C8), 오렌지 텍스트(#F26A00)
- 성공: 초록 틴트 배경(#C6F0D6), 초록 텍스트(#077235)
- 경고: 앰버 틴트 배경(#FEF3C7), 앰버 텍스트(#B45309)
- 오류: 빨간 틴트 배경(#FFD6D3), 빨간 텍스트(#C0220F)
- 정보: 파란 틴트 배경(#D1E5FF), 파란 텍스트(#0D5DCC)
- 중립: 회색 배경, 보조 텍스트

선택: 좌측에 6px 상태 점 (해당 변형 색상)

태그(제거 가능):
- 12px Medium 텍스트, 필 형태, 연한 회색 배경과 보더
- 우측에 ✕ 제거 버튼(14px 원형), 호버 시 빨간색으로 변경

네이밍: Badge / {변형} / {크기}, Tag / Default
```
