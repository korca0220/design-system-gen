# 컴포넌트: 테이블 (Table)

## 개요
행과 열로 구성된 구조적 데이터 표시. 정렬, 선택, 밀도 옵션 지원.

---

## 디자인 토큰

| 토큰 | 값 |
|---|---|
| 헤더 폰트 | 12px / Medium 500, `color/text/tertiary`, 대문자 |
| 헤더 배경 | `color/surface/2` |
| 헤더 보더 | 1px solid `color/border/default` |
| 셀 폰트 | 14px / Regular, `color/text/primary` |
| 셀 패딩 (기본) | 10px 12px |
| 셀 패딩 (컴팩트) | 6px 12px |
| 행 보더 | 1px solid `color/border/subtle` |
| 행 호버 | `color/surface/2` |
| 행 선택됨 | `color/primary/subtle` |

---

## 기능

### 정렬
- 컬럼 헤더: 클릭 가능
- 정렬 표시: ↑ (오름차순) / ↓ (내림차순) 헤더 텍스트 뒤에 추가
- 기본: 표시 없음

### 행 선택
- 좌측에 체크박스 컬럼 (40px 너비)
- 전체 선택: 헤더 체크박스
- 선택된 행: `color/primary/subtle` 배경

### 밀도
- 기본: 10px 12px 셀 패딩
- 컴팩트: 6px 12px 셀 패딩

---

## 셀 종류
- **텍스트 셀**: 표준 텍스트
- **이름 셀**: 굵은 이름 + 아래 회색 부제 (12px)
- **날짜 셀**: 13px / Regular, `color/text/secondary`
- **뱃지 셀**: 상태 뱃지 컴포넌트
- **액션 셀**: 아이콘 버튼 (편집, 삭제 등)

---

## Figma Make 프롬프트

```
다음 스펙으로 데이터 테이블(Table) 컴포넌트를 만들어줘:

헤더 행:
- 12px Medium 대문자 회색 텍스트
- 행보다 약간 어두운 배경
- 정렬 가능한 컬럼 (↑↓ 인디케이터)
- 선택 전체 체크박스 (선택적)

데이터 행:
- 14px Regular 텍스트
- 행 사이 미세한 하단 보더
- 호버: 연한 회색 배경
- 선택됨: 연한 오렌지 배경

셀 종류:
- 텍스트, 이름+부제, 날짜, 상태 뱃지, 액션 버튼

밀도: 기본 (넓게) 및 컴팩트 변형

네이밍: Table / Default, Table / Compact
```
