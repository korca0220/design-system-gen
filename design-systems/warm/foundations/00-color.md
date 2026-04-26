# 파운데이션: 컬러 (Color)

## 개요

Warm Orange(#F26A00) 브랜드 컬러 기반의 컬러 시스템. Primitive → Semantic 2레이어 구조로 설계. 라이트/다크 모드를 Semantic 토큰 하나로 대응.

| 항목 | 값 |
|---|---|
| 브랜드 컬러 | #F26A00 (Warm Orange) |
| 컬러 스케일 | Orange / Neutral / Green / Amber / Red / Blue |
| 모드 | 라이트 / 다크 |
| 구조 | Primitive → Semantic |

---

## 디자인 원칙

- **컴포넌트는 Semantic 토큰만 참조.** `color/primary/default` 사용. `#F26A00` 하드코딩 금지.
- **Primitive는 Semantic의 원재료.** Figma Variables에서 Alias로 연결.
- **라이트/다크 모드는 Semantic 레이어에서 Mode로 분기.** Primitive 값은 동일.

---

## 디자인 토큰 — Primitive

### Orange (브랜드 원색)

| 토큰 | 값 (Hex) |
|---|---|
| `color/orange/50` | #FFF5ED |
| `color/orange/100` | #FFE4C8 |
| `color/orange/200` | #FFC98A |
| `color/orange/300` | #FFA84D |
| `color/orange/400` | #FF8A1E |
| `color/orange/500` | #F26A00 ← 브랜드 메인 |
| `color/orange/600` | #C75200 |
| `color/orange/700` | #9C3D00 |
| `color/orange/800` | #702B00 |
| `color/orange/900` | #451A00 |

### Neutral (Warm Gray 계열)

| 토큰 | 값 (Hex) |
|---|---|
| `color/neutral/0` | #FFFFFF |
| `color/neutral/50` | #FAFAF8 |
| `color/neutral/100` | #F4F3F0 |
| `color/neutral/200` | #E8E6E1 |
| `color/neutral/300` | #D4D1CA |
| `color/neutral/400` | #B0ADA4 |
| `color/neutral/500` | #8A877E |
| `color/neutral/600` | #66635B |
| `color/neutral/700` | #47443E |
| `color/neutral/800` | #2E2C27 |
| `color/neutral/900` | #1A1916 |
| `color/neutral/950` | #0F0E0C |

### Semantic Colors (상태별 원색)

| 색상 | 500 (라이트 기본) | 400 (다크 기본) |
|---|---|---|
| Green | #0D9144 | #22AD58 |
| Amber | #F59E0B | #FBBF24 |
| Red | #E8321E | #FF4D3A |
| Blue | #1A78F2 | #3D93FF |

---

## 디자인 토큰 — Semantic

### Primary (브랜드 인터랙션)

| 토큰 | 라이트 | 다크 | 사용처 |
|---|---|---|---|
| `color/primary/default` | orange/500 | orange/400 | CTA 버튼, 링크, 포커스 링 |
| `color/primary/hover` | orange/600 | orange/300 | 버튼 hover |
| `color/primary/active` | orange/700 | orange/200 | 버튼 pressed |
| `color/primary/subtle` | orange/50 | rgba(242,106,0,0.12) | 선택 항목 bg, 포커스 bg |
| `color/primary/tint` | orange/100 | rgba(242,106,0,0.20) | 뱃지 bg, 태그 bg |
| `color/primary/on-primary` | #FFFFFF | neutral/950 | Primary 배경 위 텍스트 |

### Background (페이지 배경)

| 토큰 | 라이트 | 다크 | 사용처 |
|---|---|---|---|
| `color/background/base` | neutral/50 | neutral/950 | 페이지 최하단 배경 |
| `color/background/subtle` | neutral/100 | neutral/900 | 사이드바, 섹션 구분 |
| `color/background/muted` | neutral/200 | neutral/800 | 비활성 bg |

### Surface (카드/패널 배경)

| 토큰 | 라이트 | 다크 | 사용처 |
|---|---|---|---|
| `color/surface/1` | neutral/0 | neutral/900 | 카드, 패널, 기본 컨테이너 |
| `color/surface/2` | neutral/50 | neutral/800 | 카드 헤더, 테이블 헤더 |
| `color/surface/3` | neutral/100 | neutral/700 | 드롭다운, 툴팁 bg |
| `color/surface/overlay` | rgba(26,25,22,0.48) | rgba(0,0,0,0.64) | 모달 딤 배경 |

### Border (테두리)

| 토큰 | 라이트 | 다크 | 사용처 |
|---|---|---|---|
| `color/border/subtle` | neutral/100 | rgba(255,255,255,0.06) | 테이블 구분선 |
| `color/border/default` | neutral/200 | rgba(255,255,255,0.10) | 카드, 인풋 기본 보더 |
| `color/border/strong` | neutral/300 | rgba(255,255,255,0.18) | 인풋 hover, 강조 보더 |

### Text (텍스트)

| 토큰 | 라이트 | 다크 | 사용처 |
|---|---|---|---|
| `color/text/primary` | neutral/900 | neutral/50 | 헤딩, 주요 본문 |
| `color/text/secondary` | neutral/600 | neutral/400 | 보조 설명, 메타 정보 |
| `color/text/tertiary` | neutral/400 | neutral/600 | 플레이스홀더, 힌트 |
| `color/text/disabled` | neutral/300 | neutral/700 | 비활성 텍스트 |
| `color/text/inverse` | neutral/0 | neutral/900 | 어두운 배경 위 텍스트 |

### 상태 색상 (Success / Warning / Error / Info)

각 색상은 동일한 4가지 토큰 구조를 가짐:

| 토큰 구조 | 라이트 | 다크 | 사용처 |
|---|---|---|---|
| `color/{상태}/default` | 해당 색상 500 | 해당 색상 400 | 아이콘, 테두리 |
| `color/{상태}/subtle` | 해당 색상 50 | rgba(..., 0.12) | 알림/뱃지 배경 |
| `color/{상태}/tint` | 해당 색상 100 | rgba(..., 0.20) | 뱃지 배경 |
| `color/{상태}/text` | 해당 색상 600 | 해당 색상 300 | 상태 텍스트 |

**Success**: green/500 (#0D9144) 기반
**Warning**: amber/500 (#F59E0B) 기반
**Error**: red/500 (#E8321E) 기반
**Info**: blue/500 (#1A78F2) 기반

---

## Figma Make 프롬프트

```
다음 스펙으로 컬러 시스템을 Figma Variables로 구성해줘:

Collection 1 — Color / Primitives (Mode 없음):
Orange: 50(#FFF5ED), 100(#FFE4C8), 200(#FFC98A), 300(#FFA84D), 400(#FF8A1E), 500(#F26A00), 600(#C75200), 700(#9C3D00), 800(#702B00), 900(#451A00)
Neutral: 0(#FFFFFF), 50(#FAFAF8), 100(#F4F3F0), 200(#E8E6E1), 300(#D4D1CA), 400(#B0ADA4), 500(#8A877E), 600(#66635B), 700(#47443E), 800(#2E2C27), 900(#1A1916), 950(#0F0E0C)
Green: 50~600 / Amber: 50~700 / Red: 50~600 / Blue: 50~600

Collection 2 — Color / Semantic (Mode: Light / Dark):
Primitive 값을 Alias로 연결.

Primary:
- default: orange/500(Light) / orange/400(Dark)
- hover: orange/600 / orange/300
- active: orange/700 / orange/200
- subtle: orange/50 / rgba(242,106,0,0.12)
- tint: orange/100 / rgba(242,106,0,0.20)
- on-primary: #FFFFFF / neutral/950

Surface: 1/2/3/overlay
Border: subtle/default/strong
Text: primary/secondary/tertiary/disabled/inverse
Success/Warning/Error/Info: default/subtle/tint/text

모든 Semantic 토큰에서 Primitive를 Alias로 연결.
```
