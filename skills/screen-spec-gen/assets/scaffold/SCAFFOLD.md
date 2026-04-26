# Screen Spec Scaffold

이 디렉토리는 **결과물이 아니라 스캐폴드**입니다. SKILL의 Phase 0.5에서 새로운 스크린 명세 프로젝트를 만들 때 결과 디렉토리로 그대로 복사되는 베이스 템플릿입니다.

## 📦 포함된 파일

- `README.md` — 결과물 루트 README (베이스 DS, 출처 요약)
- `screens/TEMPLATE.md` — 스크린 명세 작성 템플릿 (3-layer: Skeleton/Bindings/Intent)

## 🔤 플레이스홀더

복사 후 SKILL이 다음 토큰을 실제 값으로 치환합니다:

| 플레이스홀더 | 의미 |
|---|---|
| `{{Project Name}}` | 프로젝트 이름 (예: "DailyPiece") |
| `{{base-design-system}}` | 베이스 DS 인스턴스 이름 (예: "wanted") |
| `{{Source URL}}` | Figma URL 또는 코드 출처 |

`TEMPLATE.md`는 **그대로 복사**합니다 — 새 스크린 작성 시 참조하는 형식 기준.

## ⚠️ 결과물에 SCAFFOLD.md 포함하지 마세요
이 파일은 스캐폴드 자체의 사용법 문서이므로 복사 시 제외(`--exclude='SCAFFOLD.md'`).
