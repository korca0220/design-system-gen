# 파운데이션: 타이포그래피 (Typography)

## 개요

Pretendard 기반 타이포그래피 시스템. 16px을 기본 베이스로 하며 Display, Heading, Body, Label, Caption 5개 카테고리로 구성됨. 한글과 영문 모두 최적화된 자간과 줄 높이를 적용.

| 항목 | 값 |
|---|---|
| 기본 폰트 | Pretendard |
| 폴백 폰트 | -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif |
| 베이스 크기 | 16px (body/md) |
| 라이트/다크 | 동일 (색상 토큰으로 대응) |

---

## 디자인 토큰 — Primitive

### 폰트 패밀리

| 토큰 | 값 |
|---|---|
| `fontFamily/sans` | 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif |

### 폰트 크기

| 토큰 | 값 |
|---|---|
| `fontSize/11` | 11px |
| `fontSize/12` | 12px |
| `fontSize/13` | 13px |
| `fontSize/14` | 14px |
| `fontSize/16` | 16px |
| `fontSize/18` | 18px |
| `fontSize/20` | 20px |
| `fontSize/24` | 24px |
| `fontSize/28` | 28px |
| `fontSize/32` | 32px |
| `fontSize/40` | 40px |
| `fontSize/48` | 48px |

### 폰트 굵기

| 토큰 | 값 |
|---|---|
| `fontWeight/regular` | 400 |
| `fontWeight/medium` | 500 |
| `fontWeight/semibold` | 600 |
| `fontWeight/bold` | 700 |

### 줄 높이 (Line Height)

| 토큰 | 값 |
|---|---|
| `lineHeight/tight` | 1.2 |
| `lineHeight/snug` | 1.35 |
| `lineHeight/normal` | 1.5 |
| `lineHeight/relaxed` | 1.6 |
| `lineHeight/loose` | 1.75 |

### 자간 (Letter Spacing)

| 토큰 | 값 |
|---|---|
| `letterSpacing/tighter` | -0.03em |
| `letterSpacing/tight` | -0.02em |
| `letterSpacing/snug` | -0.01em |
| `letterSpacing/normal` | 0em |
| `letterSpacing/wide` | 0.01em |

---

## 디자인 토큰 — Semantic

### Display (랜딩/히어로 전용)

| 토큰 | 크기 | 굵기 | 줄 높이 | 자간 | 사용처 |
|---|---|---|---|---|---|
| `text/display-2xl` | 48px | Bold 700 | 1.15 | -0.03em | 랜딩 히어로 메인 카피 |
| `text/display-xl` | 40px | Bold 700 | 1.2 (tight) | -0.02em | 랜딩 섹션 헤드라인 |
| `text/display-lg` | 32px | Bold 700 | 1.2 (tight) | -0.02em | 페이지 메인 타이틀 |
| `text/display-md` | 28px | Bold 700 | 1.25 | -0.02em | 서브 페이지 타이틀 |
| `text/display-sm` | 24px | SemiBold 600 | 1.3 | -0.01em | 섹션 대표 타이틀 |

### Heading (UI 내부 제목)

| 토큰 | 크기 | 굵기 | 줄 높이 | 자간 | 사용처 |
|---|---|---|---|---|---|
| `text/heading-xl` | 20px | SemiBold 600 | 1.35 | -0.01em | 카드 그룹 헤더 |
| `text/heading-lg` | 18px | SemiBold 600 | 1.35 | -0.01em | 사이드바 섹션 |
| `text/heading-md` | 16px | SemiBold 600 | 1.4 | -0.01em | 카드 타이틀 |
| `text/heading-sm` | 14px | SemiBold 600 | 1.4 | 0em | 리스트 항목 제목 |
| `text/heading-xs` | 13px | SemiBold 600 | 1.4 | 0em | 소형 카드 타이틀 |

### Body (본문 텍스트)

| 토큰 | 크기 | 굵기 | 줄 높이 | 자간 | 사용처 |
|---|---|---|---|---|---|
| `text/body-xl` | 20px | Regular 400 | 1.75 | -0.01em | 랜딩 히어로 서브카피 |
| `text/body-lg` | 18px | Regular 400 | 1.7 | -0.01em | 랜딩 섹션 설명 |
| `text/body-md` | 16px | Regular 400 | 1.6 | -0.01em | **기본 본문 — BASE** |
| `text/body-sm` | 14px | Regular 400 | 1.5 | 0em | 보조 설명, 테이블 셀 |
| `text/body-xs` | 13px | Regular 400 | 1.5 | 0em | 고밀도 테이블 |

### Label (버튼, 탭, UI 레이블)

| 토큰 | 크기 | 굵기 | 줄 높이 | 자간 | 사용처 |
|---|---|---|---|---|---|
| `text/label-lg` | 16px | Medium 500 | 1.35 | 0em | Large 버튼, 주요 CTA |
| `text/label-md` | 14px | Medium 500 | 1.35 | 0em | Medium 버튼, 탭, 네비게이션 |
| `text/label-sm` | 13px | Medium 500 | 1.35 | 0em | Small 버튼, 드롭다운 항목 |
| `text/label-xs` | 12px | Medium 500 | 1.3 | 0.01em | 테이블 컬럼명, 폼 레이블 |

### Caption

| 토큰 | 크기 | 굵기 | 줄 높이 | 자간 | 사용처 |
|---|---|---|---|---|---|
| `text/caption` | 12px | Regular 400 | 1.5 | 0em | 타임스탬프, 이미지 캡션, 폼 힌트 |

---

## 사용 원칙

- 컴포넌트는 반드시 Semantic 토큰(`text/body-md` 등)만 참조. Primitive(`fontSize/16`) 직접 사용 금지.
- 한글 본문은 `body/md` 기준 `lineHeight/relaxed` (1.6) 사용을 권장.
- 영문 헤딩은 `letterSpacing/tight` 이하 적용으로 시각적 밀도를 높임.
- 다크 모드는 색상 토큰으로 대응. 폰트 크기/굵기 변경 없음.

---

## Figma Make 프롬프트

```
다음 스펙으로 타이포그래피 시스템을 Figma에 구성해줘:

폰트: Pretendard (없으면 -apple-system 폴백)
베이스: 16px

Text Style 목록:
- Display 2xl: 48px Bold 700, 줄높이 1.15, 자간 -0.03em
- Display xl: 40px Bold 700, 줄높이 1.2, 자간 -0.02em
- Display lg: 32px Bold 700, 줄높이 1.2, 자간 -0.02em
- Display md: 28px Bold 700, 줄높이 1.25, 자간 -0.02em
- Display sm: 24px SemiBold 600, 줄높이 1.3, 자간 -0.01em
- Heading xl: 20px SemiBold 600, 줄높이 1.35, 자간 -0.01em
- Heading lg: 18px SemiBold 600, 줄높이 1.35, 자간 -0.01em
- Heading md: 16px SemiBold 600, 줄높이 1.4, 자간 -0.01em
- Heading sm: 14px SemiBold 600, 줄높이 1.4, 자간 0em
- Heading xs: 13px SemiBold 600, 줄높이 1.4, 자간 0em
- Body xl: 20px Regular 400, 줄높이 1.75, 자간 -0.01em
- Body lg: 18px Regular 400, 줄높이 1.7, 자간 -0.01em
- Body md: 16px Regular 400, 줄높이 1.6, 자간 -0.01em (BASE)
- Body sm: 14px Regular 400, 줄높이 1.5, 자간 0em
- Body xs: 13px Regular 400, 줄높이 1.5, 자간 0em
- Label lg: 16px Medium 500, 줄높이 1.35, 자간 0em
- Label md: 14px Medium 500, 줄높이 1.35, 자간 0em
- Label sm: 13px Medium 500, 줄높이 1.35, 자간 0em
- Label xs: 12px Medium 500, 줄높이 1.3, 자간 0.01em
- Caption: 12px Regular 400, 줄높이 1.5, 자간 0em

Figma Text Styles로 등록. 네이밍: {카테고리}/{크기} (예: Body/md, Heading/xl)
```
