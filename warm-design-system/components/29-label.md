# 컴포넌트: 폼 레이블 (Form Label)

## 개요
폼 인풋과 연결된 텍스트 레이블. 선택적 필수 표시와 힌트 텍스트 포함.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 폰트 | `text/label-md` = 13px / Medium 500 |
| 색상 | `color/text/secondary` |
| 필수 표시 | `*` → `color/error/default` |
| 인풋과의 간격 | 5px |
| 힌트 폰트 | 12px / Regular |
| 힌트 색상 | `color/text/tertiary` |
| 오류 색상 | `color/text/error` |
| 성공 색상 | `color/text/success` |

---

## 구조
- 레이블 텍스트 + 선택적 필수 표시 (*)
- 인풋 아래 (선택): 힌트/오류/성공 메시지

---

## Figma Make 프롬프트

```
다음 스펙으로 폼 레이블(Form Label) 컴포넌트를 만들어줘:

레이블 텍스트: 13px Medium, 회색 (#66635B)
필수 표시: 레이블 텍스트 바로 뒤에 * (빨간색 #E8321E)

보조 텍스트 변형 (인풋 아래):
- 힌트: 12px Regular, 연한 회색
- 오류: 12px Regular, 빨간색 (#C0220F)
- 성공: 12px Regular, 초록색 (#077235)

간격: 레이블과 인풋 사이 5px, 인풋과 보조 텍스트 사이 4px

네이밍: Label / Default, Label / Required, Label / With Hint, Label / With Error, Label / With Success
```
