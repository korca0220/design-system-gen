# 🔍 HTML/CSS 휴리스틱 추출 가이드

이 문서는 SKILL.md **Phase 1A**에서 토큰화되지 않은 raw HTML/CSS 입력을 표준 디자인 시스템으로 환원할 때 사용하는 구체적 규칙입니다. Figma Variables처럼 명시적 토큰이 없는 입력에서 "잘 추정된 토큰 시스템"을 만들기 위한 결정 트리.

---

## 1. 색상 (Color)

### 1.1 수집 단계
입력 CSS에서 다음 위치의 모든 색상 값을 수집합니다:
- `color`, `background`, `background-color`, `border-color`, `outline-color`, `fill`, `stroke`
- 그라데이션 stop 색상
- 박스 섀도우의 색상 채널

수집한 값은 hex 6자리로 정규화하고 (`#fff` → `#ffffff`, `rgb(...)` → hex), 알파를 가진 값은 별도 그룹으로 분리합니다.

### 1.2 브랜드 키 컬러 식별 (Key Color)
다음 셋 중 **하나라도** 만족하는 색상이 후보:
- 등장 빈도 상위 3 안에 들면서 **채도 ≥ 40%** (HSL 기준)
- CTA 버튼, 링크, 활성 상태 같은 **강조 위치**에서 등장
- 회색조(채도 < 10%)가 아닌 색 중 **가장 채도가 높은 것**

후보가 여러 개면 사용자에게 확인합니다. **단 하나만 키 컬러로 선언**합니다 — 두 개 이상 키 컬러는 디자인 시스템 응집력을 깎습니다.

### 1.3 색상 군집화 (Clustering)
수집한 색상을 다음 6개 카테고리로 분류합니다:

| 카테고리 | 판별 기준 | Primitive 단계 |
|---|---|---|
| **Brand / Primary** | 키 컬러 및 그 명도 변형 | 50, 100, 200, 300, 400, **500**(키), 600, 700, 800, 900 |
| **Neutral / Gray** | 채도 < 10% | 동일 10단계, 50(거의 흰색)~900(거의 검정) |
| **Surface** | 배경 위치(`background`)에서 등장하는 거의-흰색/거의-검정 | 1, 2, 3 (밝기 단계) + overlay |
| **Semantic — Success** | 녹색 계열 (Hue 100~160) | 50/500/700 |
| **Semantic — Warning** | 노랑/주황 계열 (Hue 30~60) | 50/500/700 |
| **Semantic — Danger / Error** | 빨강 계열 (Hue 350~10) | 50/500/700 |

**ΔE 군집화 규칙**: 같은 hue 범위 내 색상 중 **ΔE < 5**인 것은 동일 단계로 통합합니다 (사람 눈에 거의 구분되지 않는 색은 합칠 것). ΔE 계산이 어려우면 HSL 거리(lightness 차이 < 5% AND saturation 차이 < 8%)로 근사.

### 1.4 Semantic 매핑
다음은 Primitive에서 Semantic으로의 표준 매핑 시작점입니다 ([token_naming.md](token_naming.md) 참조):

```
color/text/primary    ← neutral/900 (light) / neutral/50 (dark)
color/text/secondary  ← neutral/700 / neutral/200
color/text/tertiary   ← neutral/500 / neutral/400
color/text/disabled   ← neutral/300 / neutral/600
color/text/inverse    ← neutral/50 / neutral/900

color/surface/1       ← #ffffff (light) / neutral/900 (dark)
color/surface/2       ← neutral/50 / neutral/800
color/surface/3       ← neutral/100 / neutral/700
color/surface/overlay ← rgba(0,0,0,0.48)

color/border/default  ← neutral/200 / neutral/700
color/border/subtle   ← neutral/100 / neutral/800
color/border/strong   ← neutral/400 / neutral/500

color/primary/default ← brand/500
color/primary/hover   ← brand/600
color/primary/active  ← brand/700
color/primary/subtle  ← brand/50
```

각 매핑은 키 컬러와 brand 톤에 따라 조정합니다. 따뜻한 톤이면 neutral도 미세한 따뜻한 hue를 부여하는 게 일반적(예: 순수 회색 대신 yellow-tinted gray).

---

## 2. 간격 (Spacing)

### 2.1 기본 단위 추정
입력 CSS의 모든 `padding`, `margin`, `gap` 값을 픽셀로 정규화하여 수집한 후, **GCD(최대공약수) 기반 추정**:

- 수집된 값 집합의 GCD가 4 또는 8이면 → 그것이 base unit
- GCD가 1~3이면 → 입력이 노이즈 많음. 4px를 default base로 가정하고 가까운 값으로 반올림

### 2.2 표준 스케일
base unit이 결정되면 다음 스케일을 Primitive로 정의합니다 (base = 4px 가정):

| Primitive | 값 | 의미 |
|---|---|---|
| `spacing/0` | 0px | 없음 |
| `spacing/1` | 4px | 미세 |
| `spacing/2` | 8px | 좁음 |
| `spacing/3` | 12px | 컴포넌트 내부 sm |
| `spacing/4` | 16px | 컴포넌트 내부 md (기본) |
| `spacing/5` | 20px | 컴포넌트 내부 lg |
| `spacing/6` | 24px | 컴포넌트 사이 sm |
| `spacing/8` | 32px | 컴포넌트 사이 md |
| `spacing/10` | 40px | 섹션 sm |
| `spacing/12` | 48px | 섹션 md |
| `spacing/16` | 64px | 섹션 lg |

### 2.3 매그닉 넘버 환원
입력의 모든 spacing 값을 위 스케일의 **가장 가까운 단계**로 반올림합니다. 차이가 ≤ 2px이면 환원 가능, 그 이상이면:
- 디자이너 의도일 가능성 → 별도 카테고리(`spacing/component-xs` 등)로 추가
- 또는 사용자에게 보고하고 결정 위임

**Semantic 권장 매핑:**
```
spacing/component-xs  ← spacing/2 (8px)
spacing/component-sm  ← spacing/3 (12px)
spacing/component-md  ← spacing/4 (16px)
spacing/component-lg  ← spacing/5 (20px)
spacing/layout-sm     ← spacing/8 (32px)
spacing/layout-md     ← spacing/12 (48px)
spacing/layout-lg     ← spacing/16 (64px)
```

---

## 3. 타이포그래피 (Typography)

### 3.1 폰트 패밀리 군집화
모든 `font-family` 값을 수집합니다. **2개 이상이면 사용자에게 알림** — 디자인 시스템은 보통 1~2개 패밀리(본문 + 모노)만 갖습니다.

### 3.2 사이즈 스케일 추정
수집한 `font-size` 값을 정렬한 후, 인접 비율을 봅니다:
- 비율이 일정(예: 1.125 / 1.2 / 1.25 / 1.333)하면 → 모듈러 스케일
- 들쭉날쭉하면 → 가장 가까운 표준 단계로 환원

**표준 스케일 (1.125 비율 가정):**

| Primitive | 값 | 권장 Semantic |
|---|---|---|
| `fontSize/12` | 12px | `text/caption` |
| `fontSize/14` | 14px | `text/body-sm` |
| `fontSize/16` | 16px | `text/body-md` (기본) |
| `fontSize/18` | 18px | `text/body-lg` / `text/heading-sm` |
| `fontSize/20` | 20px | `text/heading-md` |
| `fontSize/24` | 24px | `text/heading-lg` |
| `fontSize/32` | 32px | `text/heading-xl` |
| `fontSize/40` | 40px | `text/display-sm` |
| `fontSize/48` | 48px | `text/display-md` |

### 3.3 굵기 (Weight)
보통 3~5단계로 줄입니다: 400(Regular), 500(Medium), 600(SemiBold), 700(Bold). 그 외 등장 weight는 가장 가까운 단계로 환원하고 보고합니다.

### 3.4 라인 하이트
`line-height`는 **상대값**(1.0 ~ 1.6)으로 정규화합니다. 절대값(예: 24px)이면 해당 폰트 사이즈로 나눠 비율로 표기합니다. 표준:
- Heading: 1.2 ~ 1.3
- Body: 1.5 ~ 1.6
- Caption: 1.4

---

## 4. 보더 반경 (Border Radius)

수집한 `border-radius` 값을 군집화합니다. 보통 4~5단계로 환원:

| Primitive | 값 | 권장 Semantic |
|---|---|---|
| `radius/none` | 0px | — |
| `radius/sm` | 4px | `radius/input`, `radius/badge` |
| `radius/md` | 8px | `radius/button`, `radius/card` |
| `radius/lg` | 12px | `radius/modal-sm` |
| `radius/xl` | 16px | `radius/modal` |
| `radius/full` | 9999px | `radius/avatar`, `radius/pill` |

군집 임계값: 차이 ≤ 2px이면 같은 단계. 5단계를 초과하면 시스템 일관성이 약함을 경고합니다.

---

## 5. 그림자 (Shadow)

`box-shadow` 값을 수집해 elevation 단계로 환원합니다. 보통 3~4단계:

| Primitive | 권장 사용처 |
|---|---|
| `shadow/sm` | Card, Button hover |
| `shadow/md` | Dropdown, Tooltip |
| `shadow/lg` | Modal, Drawer |
| `shadow/focus` | 키보드 포커스 링 (필수) |

각 단계는 다음 형식으로 명세: `[offset-x] [offset-y] [blur] [spread] [color-with-alpha]`. 알파는 0.04 ~ 0.16 범위 내가 일반적.

**색상**: 그림자 색은 순수 검정(#000)보다 브랜드 톤이 약간 섞인 색이 자연스럽습니다 (예: 따뜻한 디자인엔 미세한 갈색 톤).

---

## 6. 모션 (Motion)

`transition`, `animation` 값에서 duration과 easing을 수집합니다. 일반적인 환원:

| Primitive | duration | easing | 용도 |
|---|---|---|---|
| `motion/instant` | 0ms | — | 변화 없음 |
| `motion/fast` | 100ms | ease-out | 호버, 미세 변화 |
| `motion/base` | 150ms | ease-out | 기본 (버튼 등) |
| `motion/slow` | 250ms | ease-out | 패널 등장 |
| `motion/page` | 300ms | ease-out | 라우트 전환, 드로어 |

200ms 이상의 등장/퇴장은 **easing 곡선을 명확히 지정**해야 자연스럽습니다. 모달은 `cubic-bezier(0.16, 1, 0.3, 1)` 같은 spring-like 곡선이 일반적.

---

## 7. 우선순위와 폴백

여러 휴리스틱이 충돌하면 다음 순서를 따릅니다:

1. **명시적 CSS 변수**(`--*`) > 산출 휴리스틱 (이미 토큰화된 신호)
2. **빈도 + 위치 가중치** > 단순 빈도 (CTA 위치 색상이 일반 텍스트보다 의미가 큼)
3. **사용자 확인** > 자동 결정 (애매하면 묻기)

산출이 끝나면 [quality_rubric.md](quality_rubric.md)에 따라 자가 채점하고, 환원율이 60% 미만이면 **사용자에게 입력 품질 문제를 즉시 보고**합니다.
