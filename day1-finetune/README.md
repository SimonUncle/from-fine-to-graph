# Day 1: EXAONE 3.5 Fine-Tuning 실습

EXAONE 3.5 모델을 활용한 RAG 성능 향상을 위한 RAFT(Retrieval Augmented Fine Tuning) 실습 자료입니다.

## 📚 실습 구성 (총 4시간)

### 1️⃣ 세션 1: 데이터 전처리 및 검증 (13:10-14:00, 50분)
- **01_data_preprocessing_and_validation.ipynb**: 한국어 RAG 데이터셋 로드 및 RAFT 전처리
- **02_data_quality_check.ipynb**: 데이터 품질 검증 및 시각화

### 2️⃣ 세션 2: 모델 파인튜닝 (14:40-16:10, 90분) 
- **03_fine_tuning_with_lora.ipynb**: EXAONE 3.5 모델 QLoRA 파인튜닝

### 3️⃣ 세션 3: 평가 및 비교 (16:20-17:00, 40분)
- **04_evaluation_and_comparison.ipynb**: 다양한 메트릭을 활용한 모델 성능 평가

## 🚀 빠른 시작

### Google Colab에서 실행
1. 각 노트북을 Google Colab에 업로드
2. GPU 런타임 설정 (런타임 > 런타임 유형 변경 > GPU)
3. 노트북을 순서대로 실행

### 로컬 환경 설정
```bash
# Python 환경 생성 (권장: Python 3.8+)
conda create -n exaone-finetune python=3.8
conda activate exaone-finetune

# 필수 패키지 설치
pip install torch==2.0.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers==4.36.0
pip install peft==0.7.1
pip install datasets==2.14.0
pip install accelerate==0.24.0
pip install bitsandbytes==0.41.1
pip install rouge-score==0.1.2
pip install nltk==3.8.1
pip install scikit-learn==1.3.0
pip install matplotlib==3.7.2
pip install seaborn==0.12.2
pip install pandas==2.0.3
pip install numpy==1.24.3
pip install tqdm==4.65.0

# Jupyter 설치
pip install jupyter ipywidgets
```

## 📖 노트북별 상세 가이드
### 노트북 실행 참고 (다이어그램 렌더링)
- `main-practice/00-concepts.ipynb`의 비교 다이어그램은 HTML 카드로 표시되어 별도 설치 없이 즉시 확인할 수 있습니다.

- `main-practice/00-concepts.ipynb` 다이어그램은 Graphviz로 생성됩니다.
  ```bash
  # Colab
  apt-get install -qq graphviz
  pip install graphviz
  ```
  설치 후 노트북의 렌더링 셀을 실행하면 SVG로 출력됩니다.

- `main-practice/00-concepts.ipynb`에서 파인튜닝 전략 비교 그래프를 확인하려면 아래 확장을 한 번만 설치/로딩하세요.
  ```bash
  pip install mermaid-magic
  ```
  노트북 셀에서 `%load_ext mermaid_magic` 실행 후 `%%mermaid` 셀을 실행하면 그래프가 렌더링됩니다.


### 01_data_preprocessing_and_validation.ipynb
**목표**: 한국어 RAG 데이터셋 준비 및 RAFT 방법론 적용
- neural-bridge/rag-dataset-12000 데이터셋 로드
- RAFT(Retrieval Augmented Fine Tuning) 전처리 구현
- Positive/Negative 샘플 생성
- 데이터 포맷 변환 및 검증

**핵심 개념**:
- RAFT 방법론: RAG 성능 향상을 위한 파인튜닝 기법
- Positive/Negative 샘플링: 관련/비관련 문서 구분 학습

### 02_data_quality_check.ipynb  
**목표**: 전처리된 데이터의 품질 검증 및 시각화
- 토큰 분포 분석
- 텍스트 길이 통계
- RAFT 구조 검증
- 데이터 품질 지표 계산

**핵심 개념**:
- 데이터 품질 메트릭
- 토큰화 및 길이 분석
- 시각화를 통한 데이터 이해

### 03_fine_tuning_with_lora.ipynb
**목표**: EXAONE 3.5 모델 QLoRA 파인튜닝
- 4비트 양자화를 통한 메모리 최적화
- LoRA(Low-Rank Adaptation) 적용
- 효율적인 파인튜닝 실행
- GPU 메모리 모니터링

**핵심 개념**:
- QLoRA: 4비트 양자화 + LoRA의 결합
- Parameter-Efficient Fine-Tuning
- 메모리 효율적 학습 전략

### 04_evaluation_and_comparison.ipynb
**목표**: 파인튜닝 전후 모델 성능 비교 평가
- ROUGE, BLEU, 코사인 유사도, Perplexity 계산
- 정량적/정성적 평가
- 오류 사례 분석
- 모델 패키징 및 배포 준비

**핵심 개념**:
- 다양한 NLG 평가 메트릭
- 모델 성능 벤치마킹
- 배포를 위한 모델 최적화

## 🔧 주요 기술 스택

- **모델**: LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct
- **데이터셋**: neural-bridge/rag-dataset-12000 
- **파인튜닝**: QLoRA (4-bit + LoRA)
- **평가**: ROUGE, BLEU, 코사인 유사도, Perplexity
- **환경**: Google Colab (무료 GPU 지원)

## 🎯 학습 목표

이 실습을 통해 다음을 학습합니다:

1. **RAFT 방법론 이해**: RAG 시스템 성능 향상을 위한 파인튜닝 전략
2. **효율적 파인튜닝**: QLoRA를 활용한 메모리 효율적 학습
3. **포괄적 평가**: 다양한 메트릭을 통한 모델 성능 측정
4. **실무 적용**: 파인튜닝된 모델의 패키징 및 배포 준비

## 📊 예상 성능

RAFT 파인튜닝 후 예상되는 개선 효과:
- **ROUGE-L**: 15-25% 향상
- **BLEU 점수**: 10-20% 향상  
- **코사인 유사도**: 5-15% 향상
- **응답 일관성**: 현저한 개선

## ⚠️ 주의사항

### Google Colab 사용 시
- GPU 런타임 필수 설정
- 세션 타임아웃에 주의 (12시간 제한)
- 중간 결과물 정기적으로 Drive에 저장
- 메모리 사용량 모니터링 필수

### 로컬 환경 사용 시  
- CUDA 11.8+ 필요 (GPU 사용 시)
- 최소 16GB RAM, 8GB VRAM 권장
- PyTorch 2.0+ 호환성 확인

## 🔍 트러블슈팅

### 자주 발생하는 문제들

**1. GPU 메모리 부족**
```python
# 해결책: 배치 크기 줄이기
per_device_train_batch_size=1
gradient_accumulation_steps=8
```

**2. 토크나이저 오류**
```python
# 해결책: pad_token 설정
tokenizer.pad_token = tokenizer.eos_token
```

**3. 모델 로드 실패**
```python
# 해결책: device_map 설정
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto"
)
```

## 🤝 기여하기

이 실습 자료에 대한 개선 사항이나 오류 발견 시:
1. 이슈 등록을 통한 문제 보고
2. Pull Request를 통한 개선 사항 제안
3. 피드백 및 제안사항 공유

## 📞 문의사항

실습 중 문제가 발생하거나 추가 질문이 있으시면:
- 강의 중: 직접 질문
- 강의 후: 이메일 또는 GitHub 이슈 활용

## 📜 라이선스

이 실습 자료는 교육 목적으로 제작되었으며, 자유롭게 활용하실 수 있습니다.

---

**Happy Fine-tuning! 🚀**

*본 실습을 통해 여러분만의 고성능 RAG 시스템을 구축해보세요!*