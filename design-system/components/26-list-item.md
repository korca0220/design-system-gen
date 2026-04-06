# 컴포넌트: 목록 항목 (List Item)

## 개요
목록의 단일 행. 아이콘, 주요 텍스트, 보조 텍스트, 후행 메타 정보를 결합.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 패딩 | 12px 16px |
| 하단 보더 | 1px solid `color/border/subtle` |
| 호버 배경 | `color/surface/2` |
| 모션 | `motion/hover` = 100ms |
| 아이콘 컨테이너 | 36×36px, `radius/button` = 8px, `color/primary/subtle` |
| 제목 폰트 | `text/label-md` = 14px / Medium |
| 설명 폰트 | 12px / Regular, `color/text/tertiary` |
| 메타 폰트 | 12px / Regular, `color/text/tertiary` |

---

## 구조 (좌측에서 우측)
1. **아이콘 컨테이너** (선택): 36×36px 둥근 정사각형
2. **콘텐츠** (flex-1):
   - 제목: 14px / Medium, `color/text/primary`
   - 설명 (선택): 12px / Regular, `color/text/tertiary`, 제목 아래 2px
3. **메타** (선택): 12px / Regular, `color/text/tertiary`, 우측 정렬

---

## Figma Make 프롬프트

```
다음 스펙으로 목록 항목(List Item) 컴포넌트를 만들어줘:

레이아웃: 가로 플렉스, 패딩 12px 16px, 미세한 하단 보더
호버: 연한 회색 배경

좌측: 선택적 36×36px 아이콘 컨테이너 (오렌지 틴트 배경, 8px 반경)
중앙: 제목 (14px Medium) + 선택적 설명 (12px 회색) 아래
우측: 선택적 메타 텍스트 (12px 회색)

모든 요소 세로 중앙 정렬

목록 컨테이너에서 반복 행으로 사용

네이밍: List Item / Default, List Item / With Icon, List Item / With Description
```
