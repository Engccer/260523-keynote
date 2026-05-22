# 슬라이드덱 — 2026 교사 해커톤 기조강연 「우리가 만드는 학습자료는 포용적인가」

이 파일은 Claude Code(claude.ai/code)가 이 저장소에서 작업할 때 참고하는 가이드다.

## 저장소 정보

- **GitHub**: https://github.com/Engccer/260523-keynote
- **배포 URL**: https://engccer.github.io/260523-keynote/
- **GitHub Pages**: main 브랜치 루트(`/`) · legacy build · HTTPS enforced
- **공개 여부**: Public
- **라이선스**: 미설정 (사용자 결정 대기)
- **협력자**: aro-deeply (이미화 선생, 신명중학교 수업 보조) — 디자인·시각 효과·접근성 PR로 협업

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

### 디자인 원칙
- **슬라이드 = 시각 매체** · 발표자 = 내러티브 (역할 분리)
- 텍스트는 키워드·구절·한 문장 헤드라인 위주 (블로그 톤 옮기지 않음)
- 시각 70% / 텍스트 30% 비율
- **한국어 어법**: "닿다/가닿다" 사용 금지 (한국어에서 부자연스러움 · 슬라이드에서 치명적). "들어오다", "이어지다", "다가가다", "여러 갈래의 길"로 대체
- **em dash(—) 전면 금지** · 가운뎃점(·)으로 대체
- **"두 단어"/"두 가지 단어" 같은 메타 표현 금지** · 슬라이드 본문에서는 개념 자체("포용성과 몰입감")가 직접 노출되도록
- **세기 표기는 한국어로** (19세기·20세기·21세기). 영어 표기(19th 등) 안 함
- **자기 소개는 슬라이드에 넣지 않음** · S1 표지에서 발표자가 구두로 진행

### 본문 톤 (2026-05-23 직전 사용자 수정 사이클 반영)
직전까지의 추상·시적 톤("두 얼굴", "그날 교실은 웃음바다", "둘이 함께 일어날 때")을 **구체·기능 중심**으로 교체. 발표 직전 사이클에서 사용자가 직접 미세 조정한 결과:
- 추상 → 구체: "두 얼굴" → "두 가지 모습", "그날 교실은 웃음바다" → "AI의 어처구니없는 실수"
- 개념어 교체: 자기 주도/15초 자극 → 디지털 네이티브/숏폼 문화
- S6 hero 전면 교체: "키보드 대신 말로 / 자연어 한 문장으로" → "수업 도구 확장 / 학습지가 학습 앱으로"
- 슬라이드 본문 헤딩에서 "포용성/몰입감" 같은 추상 축이 빠지고, 학생이 보는 **앱·도구·기능**으로 표현 무게 이동

### 마크업 패턴 (em vs strong)
CSS가 `.duo-coda-final` 같은 컨텍스트에서 두 마크업을 색상까지 분기:
- `<em>` = 코랄(붉은 톤) · 임팩트 키워드 · 짧은 한 단어/구
  - 예: `<em>3대 원칙</em>`, `<em>만족도</em>`, `<em>오기</em>`, `<em>NO</em>`, `<em>Word Bomb</em>`
- `<strong>` = 그린 형광펜 · 문장 단위 강조 · 결론 메시지
  - 예: "**모두가 즐겁게 참여할 때**", "**선택이 아닌 필수 조건**"
- `<b>`는 사용 안 함 (시맨틱 의미 없음 + 스크린리더 인지 약함)

## 슬라이드 구성 (총 20장 · 평균 60초)

| # | 슬라이드 h2 | 시각 요소 |
|---|----------|----------|
| 1 | 우리가 만드는 학습자료는 포용적인가 | hero-text 타이포 + 발표자 byline (김헌용·이미화) |
| 2 | 지금 우리의 교실은? | 3열 era 카드 (19세기 교실·20세기 교사·21세기 학생) |
| 3 | 21세기 학생의 특성 | dual-split (디지털 네이티브 ↔ 숏폼 문화) |
| 4 | 포용성과 몰입감 | duo-tiles 거대 타이포 |
| 5 | 교사의 두 역할 | duo-tiles (콘텐츠 기획자·환경 설계자) · 코다 "전달자 NO" |
| 6 | 수업 도구 확장 · 학습지가 학습 앱으로 | hero-text + 수식형 tagline |
| 7 | 우리가 만드는 학습자료는 포용적인가? | huge-question 화면 가득 |
| 8 | UDL 3대 원칙 | pillar-row 컬러 코딩 카드 3장 |
| 9 | 다중 감각, 다중 접근 | sense-row 5감각 아이콘 |
| 10 | 설계 단계부터 접근성을 내장하라 | big-quote 인용 |
| 11 | Word Bomb · 영영풀이를 박진감 넘치는 게임으로 | SVG 폭탄 일러스트 + key-chip 6 |
| 12 | laugh 해프닝 · AI의 어처구니없는 실수 | 오디오 버튼 2종 + 학생 반응 |
| 13 | Story Detective · 교과서 본문을 추리 서사로 | SVG 돋보기 + key-chip 5 |
| 14 | Grammar Potion Lab · 문법을 마법의 물약으로 | SVG 마법 솥 + key-chip 5 |
| 15 | AI의 한계 · 최종 검수는 아직 사람의 몫 | warn-box 경고 슬라이드 |
| 16 | Pick Me · 소소한 학생 추첨 도구 | big-quote + key-chip 6 |
| 17 | 학생들의 미니게임 앱 만족도 | 가로 막대 인포그래픽 SVG (4.35·4.17·3.94) · fragment 등장 |
| 18 | 학생들이 뽑은 강점 | 도넛 차트 + 가로 막대 (줄였으면 0명 강조) |
| 19 | 학생들의 평가 한마디 | student-card 2종 (오기·마물) |
| 20 | 학습용 앱 개발의 핵심 가치 | closing-grid 2x2 (4가지 핵심 가치) + 라이브 링크 4종 |

## 파일 구조

```
260523-keynote/
├── CLAUDE.md                 ← 이 파일
├── .gitignore
├── index.html                ← 슬라이드덱 본체 (단일 파일)
├── _generate_narration.py    ← 슬라이드별 h2 내레이션 MP3 생성 스크립트 (Gemini TTS · Kore · ko-KR)
├── sfx/
│   ├── page-turn.mp3         ← 슬라이드 전환 효과음
│   ├── laugh-correct.wav     ← S12 laugh 해프닝 · 수정된 발음
│   └── laugh-wrong.wav       ← S12 laugh 해프닝 · AI가 잘못 생성한 웃음소리
└── narration/
    └── slide-01.mp3 ~ slide-20.mp3
                              ← 슬라이드 h2 기반 내레이션 (2~5초/파일, 총 880KB)
```

## 기술 스택

### 디자인 시스템 (Bright Inclusive Studio · 2026-05-22 PR #2 적용)
- **라이트 페이퍼 테마**: 배경 #F7F4ED · 잉크색 본문 · 워크숍 카드 느낌의 부드러운 그림자
- **컬러 팔레트**: 코랄 #FF7A6B · 그린 #36B37E · 블루 #5E8CFF · 샌드 #D9C7A3
- **폰트**: Noto Sans KR (본문) + DM Sans (eyebrow) + Noto Serif KR (인용)
- 다크 테마(#0d1117)에서 전면 전환 (PR #2 머지 시점)

### 인터랙션
- 단일 HTML 파일 (CDN 폰트만 외부 의존)
- 키보드 네비게이션: Arrow/Home/End/PageUp/PageDown
- **터치 스와이프**: 좌우 스와이프로 슬라이드 전환 (threshold 60px · max 800ms · 링크·버튼 위 무시 · `touch-action: pan-y`로 세로 스크롤 보존)
- **모바일 반응형**: 480px·700px·800px 3단 미디어 쿼리. 작은 화면에서 nav-btn·game-link·laugh-btn·closing-links에 min-height 44px (Apple HIG·WCAG 권장 터치 타깃)

### 단계별 등장 시스템 (PR #1)
- 슬라이드 내 다중 항목을 **fragment 클래스**로 마킹 → 클릭(Space/Enter/↓)할 때마다 하나씩 등장
- 등장 시 짧은 **tick 효과음**(Web Audio 880Hz, 외부 파일 없음)으로 청각 피드백
- 슬라이드 전환은 **page-turn**(긴 하강 톤)으로 청각 구분
- 미등장 fragment는 키보드 포커스·SR 접근 차단 → 인터랙티브 요소 탭 순서 보존 (커밋 `1ba9560` a11y fix)

### 차트 시스템 (PR #1·#2)
- S17·S18 차트는 `SURVEY` 데이터 객체 + 렌더 함수로 데이터화
- 진입 시 grow·count-up 애니메이션 + fragment 연동
- 색·수치는 CSS(`.frag-visible`)로 관리 (이전엔 JS 인라인 리셋 사용 시 앞뒤 이동 시 색 사라짐 버그 있었음 · PR #2에서 수정)

### 접근성
- **라벨 최소주의**: section·nav·progressbar의 aria-label과 announcer(aria-live) 모두 제거. 짧은 슬라이드에서 region 라벨이 본문으로 오인되는 문제 회피. 스크린리더는 헤딩 + 버튼 + 차트 alt만 읽음
- 헤딩 없는 슬라이드(S2/S3/S4/S5/S10/S15/S18)에는 `<h2 class="sr-only">`로 위계만 보장
- **스크린리더 포커스 자동 이동**: 슬라이드 전환 시 `h1, h2, h3, .hero-text, .huge-question, .big-quote, .game-headline, .warn-key, .deck-h2, .deck-h1` 중 첫 매칭에 포커스 (없으면 section 자체로 fallback)

### 오디오 시스템
- **오디오 토글**: pill 버튼 · "소리 켬/소리 끔" 상태 표시 패턴 · aria-pressed
- **fragment tick**: Web Audio 880Hz 짧은 음 (외부 파일 없음)
- **page-turn**: `sfx/page-turn.mp3` 우선, 실패 시 Web Audio fallback (440→240Hz 하강 톤)
- **laugh 버튼**: `sfx/laugh-correct.wav` / `laugh-wrong.wav` · 실패 시 console.warn 조용한 처리
- **h2 내레이션**: 슬라이드 진입 시 `narration/slide-NN.mp3` 자동 재생 (page-turn 후 ~450ms 딜레이)
- **AudioContext resume**: 첫 키 입력에서 자동재생 정책 우회

### 내레이션 정책 (2026-05-23 h2 축약 적용)
직전까지는 슬라이드별 핵심 키워드 4~8초 발화였으나, 발표 시간 한정과 구두 부연 전제를 고려해 **h2 한 줄**로 축약:
- 길이: 2~5초/슬라이드 (총 880KB, 이전 약 1.4MB에서 -37%)
- 내용: 각 슬라이드 h2 텍스트 그대로 (이전: 키워드 나열)
- 영문 고유명사·약어는 한국어 발음 표기 (UDL → "유 디 엘", Word Bomb → "워드 봄", AI → "에이아이", laugh → "래프")
- **정본**: `_generate_narration.py`의 `NARRATIONS` dict
- **재생성**: dict 수정 → 해당 mp3 삭제 → `python _generate_narration.py` 실행 (skip 로직: 미존재 파일만 재생성)
- `data-keywords` 속성은 음성과 어긋남이 누적되어 **전면 제거** (2026-05-23)

## 로컬 확인

```powershell
cd "C:\Users\pc\Windows-Projects\education\blindusingai\260523 교사 개발자 해커톤 기조 강연"
python -m http.server 8765
# http://localhost:8765/
```

## 관련 자산

- **상위 강연 폴더**: `G:\내 드라이브\KHY\Lectures\260523 교사 개발자 해커톤 기조 강연\`
  - 발제 구성안 · 블로그 글 · 학생 설문 보고서 · 참고자료
- **블로그 풀어쓰기**: `G:\내 드라이브\KHY\Lectures\260523 교사 개발자 해커톤 기조 강연\[블로그] 우리가 만드는 학습자료는 포용적인가.md` · khudt.posthaven.com 게시 예정
- **학생 설문 데이터**: 같은 폴더 `학생 설문/_survey_report.md` (130명 응답, 자유 의견 83건)
- **게임 라이브 URL**:
  - https://engccer.github.io/word-bomb-L1/
  - https://engccer.github.io/story-detective-L1/
  - https://engccer.github.io/grammar-potion-L1/
  - https://aro-deeply.github.io/pickme/
- **이전 발표 슬라이드 패턴 (재사용 가능)**:
  - 260403 한국시각장애교육재활학회: `C:\Users\pc\Windows-Projects\education\blindusingai\260403 ...`
  - 260420 시민기술네트워크 웨비나: `C:\Users\pc\Windows-Projects\education\blindusingai\260420 ...`

## Git 커밋 author 메모

- 현재 git config: `Engccer <engccer@gmail.com>` (개인 계정)
- 작업 환경은 학교 계정(`engccer@sinmyung.sen.ms.kr`)일 때도 있지만 동일인(김헌용)
- 협력자 aro-deeply (이미화 선생, `naminimiya@gmail.com`)와의 협업은 PR 기반

## 협업 PR 이력

| # | 제목 | 머지일 | 주요 내용 |
|---|------|--------|----------|
| 1 | 단계별 등장 · 차트 데이터화 · 시각 효과 (접근성 보존) | 2026-05-22 | fragment 시스템 · S17·S18 차트 데이터 객체화 · grow/count-up 애니메이션 |
| 2 | 디자인: Bright Inclusive Studio 라이트 테마 + 발표 진행 사운드 복구 + S17/S18 차트 수정 | 2026-05-23 | 다크 → 라이트 페이퍼 전환 · fragment tick + page-turn 분리 · 차트 색 사라짐 버그 fix |

## 작업 메모

- **2026-05-23 발표 직전 사용자 수정 사이클**: S2~S19 16개 슬라이드 헤딩·eyebrow·캡션·코다 본문 톤 정리. 추상·시적 표현을 구체·기능 중심으로 교체. 사용자가 직접 수정 후 Claude가 점검·자동 수정(`(strong>NO</strong>` 마크업 오타 → `<em>NO</em>`)
- **2026-05-23 내레이션 h2 축약**: 사용자 명시 지시로 NARRATIONS dict를 키워드 나열에서 h2 한 줄로 전면 교체. 20개 mp3 재생성. 발표 시간 한정 + 구두 부연 전제
- **2026-05-23 data-keywords 제거**: 본문 변경 누적으로 키워드 메타데이터가 어긋나 전면 삭제. JS에서 참조하지 않으므로 안전
- **2026-05-22 4차 함정**: Gemini TTS 무료 티어 한도 10 req/min. 20개 일괄 생성 시 throttle 필수 (`_generate_narration.py`에 `THROTTLE_SECONDS = 7`)
- **슬라이드덱 톤 ≠ 블로그 톤**: 블로그 글은 풀어쓰기, 슬라이드는 시각 큐만 추출
- **Pick Me 3일 만에 구축은 사실** · 그 부분은 절대 수정하지 말 것 (사용자 명시)
- **모바일 검증 체크리스트**: 1) 좌우 스와이프 전환 2) 세로 스크롤 가능 3) 라이브 링크 버튼 탭(44px) 4) iOS Safari 회전 시 레이아웃 5) 자동재생 차단 환경에서 SFX 무음 fallback
- 슬라이드 변경 후 항상 로컬에서 키보드 네비게이션 + 오디오 토글 동작 + 모바일 뷰포트(DevTools 360x640) 시각 확인
