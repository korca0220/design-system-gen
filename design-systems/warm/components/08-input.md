# 컴포넌트: 인풋 (Input)

## 개요
사용자 데이터 입력을 위한 단일 행 텍스트 입력 필드. 가장 일반적인 폼 요소.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 폰트 | 14px / Regular 400 → `text/body-sm` |
| 배경 | `color/surface/1` |
| 보더 | 1px solid `color/border/default` |
| 보더 반경 | `radius/input` = 8px |
| 패딩 | 9px 12px |
| 플레이스홀더 | `color/text/tertiary` |
| 포커스 링 | `shadow/focus` = 0 0 0 3px rgba(242,106,0,0.20) |
| 모션 | 100ms ease-out |

---

## 크기

| 크기 | 폰트 | 패딩 |
|---|---|---|
| Large (lg) | 16px | 11px 14px |
| Medium (md) | 14px | 9px 12px |
| Small (sm) | 13px | 6px 10px |

---

## 상태

| 상태 | 보더 | 그림자 | 배경 |
|---|---|---|---|
| 기본 | `color/border/default` | — | `color/surface/1` |
| 호버 | `color/border/strong` | — | `color/surface/1` |
| 포커스 | `color/primary/default` | `shadow/focus` | `color/surface/1` |
| 오류 | `color/error/default` | 빨간 링 | `color/surface/1` |
| 성공 | `color/success/default` | — | `color/surface/1` |
| 비활성 | `color/border/subtle` | — | `color/surface/2` |
| 읽기전용 | `color/border/default` | — | `color/surface/2` |

---

## 종류
- **텍스트**: 표준 텍스트 입력
- **비밀번호**: 마스킹 처리, 우측에 표시/숨기기 토글 아이콘
- **검색**: 좌측 검색 아이콘 (⌕), 선택적 지우기 버튼

---

## 폼 필드 패턴 (전체)
- **레이블**: 13px / Medium 500, `color/text/secondary`, 인풋 위, 5px 간격
- **필수 표시**: `*` → `color/error/default`
- **힌트 텍스트**: 12px / Regular, `color/text/tertiary`, 인풋 아래 4px
- **오류 텍스트**: 12px / Regular, `color/text/error`, 인풋 아래 4px
- **성공 텍스트**: 12px / Regular, `color/text/success`, 인풋 아래 4px

---

## 접근성
- `<label>`을 `for`/`id`로 인풋과 연결 필수
- 오류 상태: `aria-invalid="true"`, `aria-describedby`로 오류 메시지 연결
- 필수 필드: `aria-required="true"`

---

## Figma Make 프롬프트

```
다음 스펙으로 인풋(Input) 폼 컴포넌트를 만들어줘:

기본 스타일:
- 폰트: 14px Regular (Pretendard)
- 패딩: 9px 12px
- 보더 반경: 8px
- 보더: 1px solid #E8E6E1 (라이트) / rgba(255,255,255,0.10) (다크)
- 배경: 흰색 / 다크 서피스

크기:
- Large: 16px, 패딩 11px 14px
- Medium: 14px, 패딩 9px 12px (기본)
- Small: 13px, 패딩 6px 10px

상태:
- 기본: 회색 보더
- 호버: 약간 진한 보더
- 포커스: 오렌지 보더 + 3px 오렌지 글로우 링
- 오류: 빨간 보더 + 빨간 글로우 링
- 성공: 초록 보더
- 비활성: 흐린 배경, 상호작용 없음
- 읽기전용: 흐린 배경, 텍스트 선택 가능

변형:
- 텍스트 전용
- 좌측 아이콘 포함 (검색 아이콘)
- 우측 아이콘 포함 (비밀번호 토글)

폼 필드 패턴:
- 레이블 (13px Medium) 인풋 위
- 필수 표시 * 빨간색
- 힌트/오류/성공 텍스트 (12px) 아래

네이밍: Input / {상태} / {크기}
```
