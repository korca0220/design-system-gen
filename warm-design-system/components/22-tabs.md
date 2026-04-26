# 컴포넌트: 탭 (Tabs)

## 개요
관련 콘텐츠 섹션 간 전환을 위한 네비게이션 컴포넌트.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 활성 인디케이터 | 2px solid `color/primary/default` |
| 활성 텍스트 | `color/text/primary` |
| 비활성 텍스트 | `color/text/tertiary` |
| 호버 텍스트 | `color/text/secondary` |
| 폰트 | 14px / Medium 500 |
| 패딩 | 탭당 10px 16px |
| 하단 보더 | 1px solid `color/border/default` |
| 모션 | 150ms ease-out |

---

## 변형

### 언더라인 (기본)
- 콘텐츠 위 가로 탭 배열
- 활성 탭: 2px 하단 보더 인디케이터 (Primary 색상)
- 하단 보더가 전체 너비에 걸쳐 있음

### 필 (Pills)
- 둥근 컨테이너 안의 탭
- 컨테이너: `color/surface/3`, 보더 반경 8px, 패딩 4px
- 활성 필: `color/surface/1` 배경, 박스 섀도우, 보더 반경 6px
- 폰트: 13px / Medium

---

## Figma Make 프롬프트

```
다음 스펙으로 탭(Tabs) 네비게이션 컴포넌트를 만들어줘:

언더라인 변형 (기본):
- 탭 항목들을 가로로 배열
- 활성: Primary 텍스트 색상, 2px 오렌지 하단 보더 인디케이터
- 비활성: 회색 텍스트, 인디케이터 없음
- 호버: 약간 진한 텍스트
- 연한 회색의 전체 너비 하단 보더
- 폰트: 14px Medium, 패딩 10px 16px

필 변형:
- 필 컨테이너: 둥근 회색 배경 (8px 반경), 4px 패딩
- 활성 필: 흰색 배경, 미세한 그림자, 6px 반경
- 비활성: 배경 없음
- 폰트: 13px Medium, 패딩 6px 14px

아래 탭 콘텐츠 영역 (빈 프레임)

네이밍: Tabs / Underline, Tabs / Pills
```
