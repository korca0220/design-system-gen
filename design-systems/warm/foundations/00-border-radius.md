# 파운데이션: 보더 레디우스 (Border Radius)

## 개요

컴포넌트별 모서리 반경 시스템. 버튼, 인풋, 카드, 모달 등 컴포넌트 유형에 따라 일관된 반경 값을 적용.

| 항목 | 값 |
|---|---|
| 최소 | 0px (날카로운 모서리) |
| 최대 | 9999px (완전한 필 형태) |
| 라이트/다크 | 동일 |

---

## 디자인 토큰 — Primitive

| 토큰 | 값 |
|---|---|
| `radius/0` | 0px |
| `radius/2` | 2px |
| `radius/4` | 4px |
| `radius/6` | 6px |
| `radius/8` | 8px |
| `radius/10` | 10px |
| `radius/12` | 12px |
| `radius/16` | 16px |
| `radius/24` | 24px |
| `radius/full` | 9999px |

---

## 디자인 토큰 — Semantic

| 토큰 | 참조 | 값 | 적용 컴포넌트 |
|---|---|---|---|
| `radius/badge` | radius/full | 9999px | 뱃지, 태그, 칩, 필 버튼 |
| `radius/button` | radius/8 | 8px | 버튼, 아이콘 버튼 |
| `radius/input` | radius/8 | 8px | 인풋, 셀렉트, 텍스트에어리어 |
| `radius/card` | radius/12 | 12px | 카드, 패널, 드롭다운 컨테이너 |
| `radius/modal` | radius/16 | 16px | 모달, 다이얼로그, 드로어 상단 |
| `radius/tooltip` | radius/6 | 6px | 툴팁, 팝오버 |
| `radius/image-sm` | radius/4 | 4px | 소형 이미지, 아바타 (사각형) |
| `radius/image-lg` | radius/12 | 12px | 대형 이미지, 썸네일 |

---

## 사용 원칙

- 컴포넌트마다 정해진 Semantic 토큰만 사용.
- 임의 값(6px, 14px 등 정의되지 않은 값) 사용 금지.
- 아바타는 원형(`border-radius: 50%`) 사용 — 별도 토큰 불필요.
- 드로어 바텀 시트: 상단 모서리만 `radius/modal` (16px), 하단은 0.

---

## Figma Make 프롬프트

```
다음 스펙으로 보더 레디우스 시스템을 Figma Variables (Number 타입)로 구성해줘:

Collection — Border Radius (Mode 없음, Number 타입):

Primitive:
radius/0 = 0
radius/2 = 2
radius/4 = 4
radius/6 = 6
radius/8 = 8
radius/10 = 10
radius/12 = 12
radius/16 = 16
radius/24 = 24
radius/full = 9999

Semantic (Primitive를 Alias로 연결):
badge = radius/full (9999) — 뱃지, 태그, 칩
button = radius/8 (8) — 버튼
input = radius/8 (8) — 인풋, 셀렉트
card = radius/12 (12) — 카드, 패널
modal = radius/16 (16) — 모달, 다이얼로그
tooltip = radius/6 (6) — 툴팁
image-sm = radius/4 (4) — 소형 이미지
image-lg = radius/12 (12) — 대형 이미지
```
