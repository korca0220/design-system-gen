# 🔗 토큰/컴포넌트 바인딩 규칙 (Binding Rules)

Skeleton의 각 슬롯에 구체값(props/variant/state/content)을 결합할 때 따르는 규칙입니다. 본 규칙을 따르면 코드 생성기가 `.md` 만으로 정확한 코드를 출력할 수 있습니다.

---

## 🎯 핵심 원칙

1. **Semantic Token Only** — 색상·간격·반경·텍스트는 베이스 DS의 Semantic Token만 참조 (`color/...`, `spacing/...` 등). raw 값(`#xxxxxx`, `Npx`) 금지.
2. **Variant 우선** — DS 컴포넌트의 prop schema(예: Button의 `variant`/`color`/`size`)를 직접 사용. 예외 처리는 가능한 한 피하고, 안 맞으면 DS 보강 PR 먼저.
3. **데이터 바인딩 표기** — 동적 값은 `{{path.to.field}}`로 표기. 정적 텍스트는 따옴표 없이 평문.
4. **이벤트는 화살표 표기** — `on-tap: <action>`, `on-change: <action>`. 화살표 우측은 자유 형식 (다음 화면 / API 호출 / state 변경 등).

---

## 📋 Binding 표준 키

각 Slot의 Bindings 섹션에서 사용하는 키 일람:

### 공통
| 키 | 의미 | 예시 |
|---|---|---|
| `ref` | 참조하는 DS 컴포넌트 .md 경로 | `design-systems/wanted/components/01-button.md` |
| `variant` | DS 컴포넌트의 variant prop | `solid`, `outlined` |
| `size` | size prop | `small`, `medium`, `large` |
| `color` | color prop (Button 등) | `primary`, `assistive` |
| `state` | 초기 상태 | `default`, `loading`, `disabled` |
| `disabled` | boolean | `true`, `false`, `{{!user.canEdit}}` |

### 콘텐츠
| 키 | 의미 | 예시 |
|---|---|---|
| `content` | 텍스트 또는 자식 노드 | `저장하기`, `{{user.name}}` |
| `text-variant` | 텍스트 스타일 (Typography 토큰) | `text/headline2` |
| `placeholder` | 입력 필드 placeholder | `이메일을 입력하세요` |
| `value` / `default-value` | 폼 필드 값 | `{{form.email}}` |
| `icon` | 아이콘 ID (DS 아이콘 시스템) | `chevron-right`, `plus` |
| `src` | 이미지 URL | `{{post.thumbnail}}` |
| `alt` | 이미지 alt | `{{post.title}}` |

### 토큰 참조
| 키 | 의미 | 예시 |
|---|---|---|
| `bg-color` | 배경 색 토큰 | `color/surface/1` |
| `text-color` | 텍스트 색 토큰 | `color/label/normal` |
| `border-color` | 보더 색 토큰 | `color/line/normal/neutral` |
| `padding` | 패딩 토큰 | `spacing/16` |
| `gap` | 자식 간 간격 | `spacing/8` |
| `radius` | 보더 반경 | `radius/lg` |
| `shadow` | 그림자 | `shadow/normal/medium` |

### 인터랙션
| 키 | 의미 | 예시 |
|---|---|---|
| `on-tap` | 탭/클릭 트리거 | `screen-flow → 02-detail.md`, `api: POST /save`, `state: showModal=true` |
| `on-change` | 값 변경 | `state: form.email = $value` |
| `on-submit` | 폼 제출 | `api: POST /signup → screen-flow → 03-welcome.md` |
| `aria-label` | 접근성 라벨 | `더 보기` |

### 슬롯 (합성 컴포넌트 내부)
| 키 | 의미 | 예시 |
|---|---|---|
| `leading` | 좌측 슬롯 | `icon: search` 또는 인라인 sub-slot 트리 |
| `trailing` | 우측 슬롯 | 동일 |
| `header` / `body` / `footer` | Card/Modal 영역 | sub-slot 트리 |

---

## 🧩 데이터 바인딩 컨벤션

동적 데이터는 `{{path}}` 표기. path는:
- **데이터 모델 필드**: `{{user.name}}`, `{{post[0].title}}`
- **반복 컨텍스트**: `{{item.field}}` (반복 슬롯 내부)
- **상태 변수**: `{{state.isOpen}}`
- **컴퓨티드**: `{{user.fullName}}` (모델 측 메서드)

> **데이터 모델은 본 스킬의 범위 외**. screen .md는 *구조 + 토큰 참조*만 담당하며, `{{user.name}}` 같은 바인딩 path는 placeholder로만 의미가 있습니다. 실제 데이터 스키마는 코드 생성 단계에서 framework-specific하게 주입(예: Flutter의 model class, React의 props/store)되며, 본 명세에 포함하지 않습니다.

---

## 🔀 조건부 / 반복

### 조건부 노출
```markdown
**Slot: errorMessage** (조건: form.email.invalid)
- ref: `design-systems/wanted/components/14-content-badge.md`
- variant: outlined
- color: accent
- accentColor: status/negative
- content: `{{form.email.error}}`
```

### 반복 (배열 → 슬롯 인스턴스 N개)
```markdown
**Slot: postList** (반복: posts)
- ref: `design-systems/wanted/components/06-card.md`
- variant: default
- bindings (per item):
  - title: `{{item.title}}`
  - description: `{{item.summary}}`
  - thumbnail src: `{{item.image}}`
  - on-tap: `screen-flow → 02-detail.md (postId: item.id)`
```

> 반복은 Skeleton의 `(반복) Item × N` 마커와 1:1 대응.

---

## 🚦 State 표현

3가지 state 카테고리:

1. **로컬 UI state** — 컴포넌트 내부 (Button hover 등). DS 컴포넌트 명세에서 자동 처리되므로 Bindings에서 다루지 않음.
2. **화면 state** — 화면 전체 상태 (loading/empty/error). Skeleton에 `(조건: ...)`로, Bindings에 해당 조건의 변형 명시.
3. **글로벌 state** — 인증/네트워크/테마 등. 본 명세 범위 외이지만 `{{auth.isLoggedIn}}` 같이 참조 가능.

### 화면 state 표준
| State | 표기 | 일반 처리 |
|---|---|---|
| Initial | (조건 없음 = default) | 정상 렌더 |
| Loading | (조건: state.loading) | Skeleton 컴포넌트로 슬롯 대체 |
| Empty | (조건: data.length === 0) | FallbackView로 영역 대체 |
| Error | (조건: state.error) | Snackbar variant=error 또는 인라인 메시지 |

---

## 🌍 i18n / Localization

텍스트는 두 가지 표기:

- **인라인 텍스트** — `content: 저장하기` (영어/한국어 자유)
- **번역 키** — `content: {{i18n.actions.save}}`

번역 키 사용을 권장하지만, 시범/프로토타이핑 단계엔 인라인 OK.

---

## ✅ 환원 못 한 raw 값 처리

베이스 DS에 매핑할 토큰이 없을 때:

1. **DS 보강이 우선** — 새 토큰을 DS의 foundations에 추가하는 PR을 먼저 만들고 그 토큰을 참조.
2. **임시 인라인 (비권장)** — 정 급하면 `<Custom>` 슬롯 안에서만 raw 값 허용. 단 검증 체크리스트의 "Bindings에 raw 값 없음"이 ❌가 되므로 명세 미완으로 마킹.

---

## 🔍 imports 사용 (멀티 DS 믹스)

frontmatter의 `imports`에 등록된 다른 DS 컴포넌트는 다음 표기:

```yaml
imports:
  - cool/components/chart-line
```

```markdown
**Slot: chart**
- ref: `imports/cool/components/chart-line.md`
- ...
```

> `imports/`는 가상 경로 prefix. 실제 파일은 `design-systems/cool/components/chart-line.md`. 코드 생성기는 frontmatter의 `imports`를 참조해 해석합니다.
