# Day 2: Advanced RAG Systems - SVG 강의 슬라이드

이쁘게 디자인된 SVG 기반 강의 슬라이드 63개 (총 9개 Section)

## 🎨 특징

- **파스텔 컬러 디자인**: 깨끗하고 현대적인 UI
- **SVG 벡터 그래픽**: 어떤 해상도에서도 선명함
- **인터랙티브 뷰어**: 웹 브라우저에서 슬라이드쇼처럼 탐색
- **키보드 단축키**: 좌우 화살표로 빠른 이동

## 📁 구조

```
presentation/
├── svg/                          # 63개 SVG 슬라이드 파일
│   ├── slide_001.svg            # 표지
│   ├── slide_002.svg            # 학습 목표
│   ├── ...
│   └── slide_063.svg            # 마무리
├── index.html                    # 슬라이드 뷰어 (메인)
├── generate_remaining_slides.py  # 템플릿 자동 생성 스크립트
└── README.md                     # 이 파일
```

## 🚀 사용 방법

### 1. 슬라이드 보기

```bash
# 웹 브라우저로 열기
open index.html

# 또는 직접 경로 입력
# file:///Users/gim-yujin/workspace/lecture_cj/day2-RAG/presentation/index.html
```

### 2. 키보드 단축키

- **← (왼쪽 화살표)**: 이전 슬라이드
- **→ (오른쪽 화살표)**: 다음 슬라이드
- **ESC**: 그리드 보기 / 슬라이드쇼 전환

### 3. 슬라이드 수정하기

#### 핵심 슬라이드 (완성됨, 그대로 사용)

```
001-003: 인트로
004-008: Naive RAG
009: 실패 분석
019: Multi-Query
026: Quiz 샘플
033: Hybrid Search
048: RAGAS
063: 마무리
```

#### 템플릿 슬라이드 (내용 채우기 필요)

나머지 슬라이드는 템플릿으로 생성되어 있습니다. 핵심 슬라이드를 복사하여 수정하세요.

**예시: slide_010.svg 수정하기**

```bash
# 1. 핵심 슬라이드(009)를 템플릿으로 복사
cp svg/slide_009.svg svg/slide_010.svg

# 2. 텍스트 에디터로 열어서 내용 수정
# - 제목: "5가지 실패 패턴" → "실패 1: Semantic Gap"
# - 본문 내용 수정
# - 페이지 번호: "9 / 63" → "10 / 63"
```

### 4. 새로운 슬라이드 추가하기

`generate_remaining_slides.py` 스크립트를 수정하여 새로운 슬라이드를 생성할 수 있습니다.

```python
# SLIDES_TO_GENERATE 딕셔너리에 추가
64: ("Section 11: Bonus", "#FF6B6B", "보너스 내용", "추가 학습 자료"),
```

그 다음 스크립트 실행:

```bash
python3 generate_remaining_slides.py
```

## 📊 슬라이드 구성

### Section 1: Naive RAG (001-008)
- 001-003: 인트로, 학습 목표, 로드맵
- 004: Naive RAG 개념
- 005: 작동 방식 플로우차트
- 006: 코드 예시
- 007: 실제 테스트 결과
- 008: 성능 지표 차트

### Section 2: 실패 분석 (009-014)
- 009: 5가지 실패 패턴 개요
- 010-014: 각 실패 패턴 상세

### Section 3: 프롬프트 엔지니어링 (015-018)
- 프롬프트 개선 전략 및 실습

### Section 4: Query Refinement (019-026)
- 019: Multi-Query Retrieval
- 020-023: HyDE, Step-Back 기법
- 024-025: 성능 비교 및 사용 시나리오
- 026: Quiz (샘플)

### Section 5: Metadata Filtering (027-032)
- 메타데이터 활용 및 실전 예시

### Section 6: Hybrid Search (033-040)
- 033: Hybrid Search 개념
- 034-039: RRF, Reranking, 코드
- 040: Quiz

### Section 7: Corrective RAG (041-047)
- CRAG 개념 및 3가지 액션

### Section 8: RAGAS Evaluation (048-055)
- 048: 4가지 메트릭 개요
- 049-055: 각 메트릭 상세 및 Quiz

### Section 9: Tuning (056-060)
- 파라미터 튜닝 실험

### Section 10: 마무리 (061-063)
- 063: 최종 요약 및 성과

## 🎯 활용 팁

### 강의 진행 시

1. **index.html 풀스크린**으로 프로젝터에 띄우기
2. **키보드 화살표**로 슬라이드 넘기기
3. 필요시 **ESC**로 그리드 보기 → 특정 슬라이드 점프

### 학생 자습용

1. **URL 공유**: `?slide=19` 파라미터로 특정 슬라이드 링크 공유
   ```
   file:///.../index.html?slide=19
   ```
2. **그리드 보기**로 전체 슬라이드 한눈에 확인
3. ✅ 표시된 슬라이드 = 핵심 내용 완성

### 커스터마이징

**색상 변경**:
```svg
<!-- 섹션 컬러 -->
#FF6B6B  (빨강/핑크) - Section 1,2
#4ECDC4  (청록) - Section 3,4,5
#45B7D1  (파랑) - Section 6
#96CEB4  (연두) - Section 7,8
#FFEAA7  (노랑) - Section 9
```

**폰트 변경**:
```svg
<text font-family="system-ui, -apple-system, sans-serif">
```
→ 원하는 폰트로 변경

## 🔧 문제 해결

### Q: 슬라이드가 표시되지 않아요
**A**: 브라우저 콘솔(F12)에서 오류 확인. 파일 경로가 올바른지 체크.

### Q: SVG 편집 프로그램?
**A**:
- **Figma** (웹): 무료, 협업 가능
- **Adobe Illustrator**: 프로페셔널
- **Inkscape**: 무료 오픈소스
- **VSCode**: 텍스트로 직접 수정

### Q: 슬라이드를 PDF로 변환하고 싶어요
**A**:
```bash
# Chrome 브라우저에서 인쇄 (Cmd+P)
# → "PDF로 저장" 선택
# → 각 슬라이드마다 반복

# 또는 자동화 스크립트 (추후 제공 예정)
```

### Q: 템플릿 내용을 어떻게 채우나요?
**A**:
1. Day 2 노트북(01-09) 내용 참고
2. 핵심 슬라이드 (001, 009, 019, 033, 048) 스타일 복사
3. 카드, 플로우차트, 코드 블록 등 재사용

## 📝 라이선스

교육용으로 자유롭게 사용 가능합니다.

## 🙏 기여

슬라이드 개선 아이디어나 버그 리포트는 환영합니다!

---

**제작**: Claude Code
**날짜**: 2025-10
**버전**: 1.0
