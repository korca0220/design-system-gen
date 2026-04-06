# 컴포넌트: 알림 / 배너 (Alert / Banner)

## 개요
사용자에게 상태, 피드백 또는 중요 정보를 전달하는 인라인 메시지.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 보더 반경 | `radius/button` = 8px |
| 패딩 | 12px 14px |
| 폰트 | 13px / Regular, 줄 높이 1.5 |
| 제목 폰트 | 13px / SemiBold 600 |
| 보더 | 1px solid 틴트 색상 |

---

## 변형

| 변형 | 배경 | 보더 | 텍스트 | 아이콘 |
|---|---|---|---|---|
| 성공 | `color/success/subtle` | `color/success/tint` | `color/success/text` | ✓ |
| 경고 | `color/warning/subtle` | `color/warning/tint` | `color/warning/text` | ! |
| 오류 | `color/error/subtle` | `color/error/tint` | `color/error/text` | ✕ |
| 정보 | `color/info/subtle` | `color/info/tint` | `color/info/text` | i |
| 중립 | `color/surface/2` | `color/border/default` | `color/text/secondary` | ⋯ |

---

## 구조
- 아이콘 (14px) — 좌측 정렬, 첫 줄 상단 정렬
- 콘텐츠 영역 (flex-1) — 선택적 제목 + 본문 텍스트
- 닫기 버튼 (선택) — 우측 상단, 16px ✕

---

## Figma Make 프롬프트

```
다음 스펙으로 알림/배너(Alert/Banner) 컴포넌트를 만들어줘:

5가지 변형: 성공, 경고, 오류, 정보, 중립

성공: 초록 틴트 배경, 초록 보더, 초록 텍스트, ✓ 아이콘
경고: 앰버 틴트 배경, 앰버 보더, 앰버 텍스트, ! 아이콘
오류: 빨간 틴트 배경, 빨간 보더, 빨간 텍스트, ✕ 아이콘
정보: 파란 틴트 배경, 파란 보더, 파란 텍스트, i 아이콘
중립: 회색 배경, 회색 보더, 보조 텍스트

구조: 좌측 아이콘 + 텍스트 콘텐츠 + 선택적 닫기 버튼 (✕) 우측
선택적 굵은 제목 본문 텍스트 위
패딩: 12px 14px, 보더 반경 8px

네이밍: Alert / {변형}
```
