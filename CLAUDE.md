# 슬라이드덱 — 2026 교사 해커톤 기조강연 「우리가 만드는 학습자료는 포용적인가」

이 파일은 Claude Code(claude.ai/code)가 이 저장소에서 작업할 때 참고하는 가이드다.

## 저장소 정보

- **GitHub**: https://github.com/Engccer/260523-keynote
- **배포 URL**: https://engccer.github.io/260523-keynote/
- **GitHub Pages**: main 브랜치 루트(`/`) · legacy build · HTTPS enforced
- **라이선스**: 미설정 (사용자 결정 대기)

## 행사 컨텍스트

- **행사명**: 2026 교사 AI·데이터 활용 「AX시대, 누구나 개발자」 해커톤
- **주최**: 서울특별시교육청 창의미래교육과 AI·미래교육팀
- **일시**: 2026년 5월 23일(토)
- **사용자 역할**: 기조강연자 (초청)
- **강연 시간**: 20분
- **청중**: 입문형·도전형 트랙 참여 초·중등 교사 100여 명 (대부분 노코드·바이브 코딩 워크숍 직전)
- **교육청 요청**: "디지털 포용 및 다양한 학습자를 고려한 학습자료 개발과 연결지어 본 행사 취지에 맞게 20분 발표"

## 슬라이드덱 메시지·톤 원칙

### Throughline
> 우리가 만드는 학습자료는 포용적인가 — 설계 단계부터 접근성을 내장하면 모든 학습자에게 진입로가 열린다.

### 디자인 원칙 (2026-05-22 확정 · 1차 재설계 후)
- **슬라이드 = 시각 매체** · 발표자 = 내러티브 (역할 분리)
- 텍스트는 키워드·구절·한 문장 헤드라인 위주 (블로그 톤 옮기지 않음)
- 시각 70% / 텍스트 30% 비율
- 한국어 어법: **"닿다/가닿다" 사용 금지** (한국어에서 부자연스러움 · 슬라이드에서 치명적). "들어오다", "이어지다", "다가가다", "여러 갈래의 길"로 대체

### 핵심 키워드 묶음 (오디오 큐용)
각 슬라이드 `<section>` 태그에 `data-keywords` 속성으로 보존. 화면에는 표시하지 않음. 추후 TTS 생성 시 `document.querySelectorAll('.slide')`로 일괄 추출 가능.

## 슬라이드 구성 (총 20장 · 평균 60초)

| # | 슬라이드 | 시각 요소 |
|---|---------|----------|
| 1 | 표지 | hero-text 타이포 + 발표자 byline |
| 2 | 19c·20c·21c 격언 | 3열 era 비교 타이포 |
| 3 | 21c 학습자 양면성 | dual-split (자기 주도 ↔ 15초 자극) |
| 4 | 두 단어: 포용성·몰입감 | duo-words 거대 타이포 |
| 5 | 교사의 두 역할 | duo-words (콘텐츠 기획자·환경 설계자) |
| 6 | 자연어 한 문장의 시대 | hero-text + 자기소개 |
| 7 | 첫 질문 | huge-question 화면 가득 |
| 8 | UDL 3원칙 | pillar-row 컬러 코딩 카드 3장 |
| 9 | 멀티모달 5감각 | sense-row 이모지 아이콘 5종 |
| 10 | 설계 단계부터 | big-quote 인용 |
| 11 | Word Bomb | SVG 폭탄 일러스트 + key-chip 6 |
| 12 | laugh 해프닝 | 오디오 버튼 2종 + 학생 반응 |
| 13 | Story Detective | SVG 돋보기 일러스트 + key-chip 5 |
| 14 | Grammar Potion Lab | SVG 마법 솥 일러스트 + key-chip 5 |
| 15 | AI의 한계 | warn-box 경고 슬라이드 |
| 16 | Pick Me | big-quote + key-chip 6 (Three.js·ARIA·Web Audio API) |
| 17 | 학생 평가 ① 평균 점수 | 가로 막대 인포그래픽 SVG (4.35·4.17·3.94) |
| 18 | 학생 평가 ② 활용 희망 + 도움 영역 | 도넛 차트 + 가로 막대 SVG (줄였으면 0명 강조) |
| 19 | 학생 자유 의견 | student-card 2종 (오기·마물) |
| 20 | 클로징 | huge-question 회귀 + 라이브 링크 4종 + 감사 |

## 파일 구조

```
260523-keynote/
├── CLAUDE.md           ← 이 파일
├── .gitignore
├── index.html          ← 슬라이드덱 본체 (단일 파일)
└── sfx/
    ├── page-turn.mp3   ← 슬라이드 전환 효과음 (story-detective-L1/sfx에서 복사)
    ├── laugh-correct.wav ← S12 laugh 해프닝 · 수정된 발음
    └── laugh-wrong.wav  ← S12 laugh 해프닝 · AI가 잘못 생성한 웃음소리
```

## 기술 스택

- 단일 HTML 파일 (CDN 폰트 Noto Sans KR 외 외부 의존 없음)
- particles 효과 · 진행률 바 · 키보드 네비게이션(Arrow/Home/End/PageUp/PageDown)
- ARIA live region · aria-label · aria-hidden 토글
- SVG 인포그래픽 (학생 평가 차트) + SVG 분위기 일러스트 (게임 사례)
- 다크 테마: #0d1117 배경, #f5c842 gold / #5de6c8 cyan / #a78bfa purple / #ff6b8a coral
- 효과음: `<audio>` Web Audio (page-turn 0.35 볼륨, laugh는 버튼 클릭 시)

## 로컬 확인

```powershell
cd "C:\Users\pc\Windows-Projects\education\blindusingai\260523 교사 개발자 해커톤 기조 강연"
python -m http.server 8765
# http://localhost:8765/
```

## 관련 자산

- **상위 강연 폴더**: `G:\내 드라이브\KHY\Lectures\260523 교사 개발자 해커톤 기조 강연\`
  - 발제 구성안 · 블로그 글 · 학생 설문 보고서 · 참고자료
- **블로그 풀어쓰기**: `G:\내 드라이브\KHY\Lectures\260523 교사 개발자 해커톤 기조 강연\[블로그] 우리가 만드는 학습자료는 포용적인가.md`
  - khudt.posthaven.com 게시 예정
- **게임 라이브 URL**:
  - https://engccer.github.io/word-bomb-L1/
  - https://engccer.github.io/story-detective-L1/
  - https://engccer.github.io/grammar-potion-L1/
  - https://aro-deeply.github.io/pickme/
- **이전 발표 슬라이드 패턴 (재사용 가능)**:
  - 260403 한국시각장애교육재활학회: `C:\Users\pc\Windows-Projects\education\blindusingai\260403 ...`
  - 260420 시민기술네트워크 웨비나: `C:\Users\pc\Windows-Projects\education\blindusingai\260420 ...`

## 향후 작업 (다음 세션 예정)

- 슬라이드덱 추가 수정 (사용자 검토 후)
- 슬라이드별 핵심 키워드 오디오 큐 생성 (data-keywords 속성 기반 TTS)
  - 사용자가 발표 중 키워드 묶음을 음성으로 받는 용도
  - 별도 폴더(예: `narration/`)에 슬라이드 번호별 mp3 저장 검토
- 강연 시간 측정 리허설
- 발표장 환경 점검

## 작업 메모

- **음성 내레이션은 명시적 지시 전까지 생성 금지** (2026-05-22 사용자 명시: "아직 음성 내레이션은 생성하지 말자")
- **슬라이드덱 톤 ≠ 블로그 톤**: 블로그 글은 풀어쓰기 형식이므로 슬라이드는 시각 큐만 추출. 블로그 문장을 그대로 옮기지 말 것.
- **Pick Me 3일 만에 구축은 사실** — 그 부분은 절대 수정하지 말 것 (이전 세션 사용자 명시)
- **em dash(—) 금지 · 화살표(→) 금지 · "본 글" 자기 지시 금지** (블로그·슬라이드 공통)
- 슬라이드 변경 후 항상 로컬에서 키보드 네비게이션 + 오디오 버튼 동작 확인
