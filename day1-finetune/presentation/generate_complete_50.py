#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 1 Fine-tuning Presentation - Complete 50 Slides Generator
Theory-focused slides (NO step-by-step instructions)
"""

# Color palette
C = {'p':'#FFB6C1','m':'#98D8C8','pu':'#B19CD9','b':'#6C9BCF','y':'#F4D35E','o':'#FFB347'}

# SVG Header
H = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
<defs><style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&amp;display=swap');
.t{font-family:'Noto Sans KR';font-size:72px;font-weight:900;fill:#2C3E50}
.st{font-family:'Noto Sans KR';font-size:36px;font-weight:500;fill:#7F8C8D}
.h1{font-family:'Noto Sans KR';font-size:56px;font-weight:700;fill:#2C3E50}
.h2{font-family:'Noto Sans KR';font-size:42px;font-weight:700;fill:#2C3E50}
.bd{font-family:'Noto Sans KR';font-size:32px;font-weight:400;fill:#2C3E50}
.sm{font-family:'Noto Sans KR';font-size:26px;font-weight:400;fill:#2C3E50}
.tp{font-family:'Noto Sans KR';font-size:28px;font-weight:500;fill:#7F8C8D}
.code{font-family:'Courier New',monospace;font-size:24px;fill:#2C3E50}
</style></defs>
<rect width="1920" height="1080" fill="white"/>'''

def dots(x=885, y=180):
    return f'<circle cx="{x}" cy="{y}" r="12" fill="{C["p"]}"/><circle cx="{x+30}" cy="{y}" r="12" fill="{C["m"]}"/><circle cx="{x+60}" cy="{y}" r="12" fill="{C["pu"]}"/><circle cx="{x+90}" cy="{y}" r="12" fill="{C["b"]}"/><circle cx="{x+120}" cy="{y}" r="12" fill="{C["y"]}"/>'

def box(x, y, w, h, color, title, lines):
    """Create a styled box with title and content lines"""
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="25" fill="{color}" opacity="0.15"/>'
    s += f'<text x="{x+w//2}" y="{y+60}" class="h2" text-anchor="middle" font-weight="700">{title}</text>'
    for i, line in enumerate(lines):
        s += f'<text x="{x+w//2}" y="{y+120+i*50}" class="bd" text-anchor="middle">{line}</text>'
    return s

def tip(text):
    return f'<rect x="80" y="980" width="1760" height="80" rx="15" fill="#F8F9FA"/><text x="120" y="1035" class="tp">{text}</text>'

# ========== SLIDE GENERATION FUNCTIONS ==========

def slide_001():
    return H + f'''
{dots()}
<text x="960" y="380" class="t" text-anchor="middle">Day 1: LLM Fine-tuning</text>
<text x="960" y="480" class="st" text-anchor="middle">"작은 데이터로 거대 모델 길들이기"</text>
{box(300, 680, 450, 200, C['p'], 'LoRA', ['99.9% 절감'])}
{box(800, 680, 450, 200, C['m'], 'RAFT', ['RAG + FT'])}
{box(1300, 680, 300, 200, C['b'], 'QLoRA', ['4-bit'])}
{tip('💡 오늘은 거대 모델을 효율적으로 학습하는 방법을 배웁니다')}
</svg>'''

def slide_002():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">오늘의 여정</text>
<rect x="200" y="380" width="700" height="500" rx="30" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="450" class="h2" text-anchor="middle">1. Fine-tuning 기초</text>
<text x="550" y="520" class="bd" text-anchor="middle">• Full vs LoRA vs QLoRA</text>
<text x="550" y="580" class="bd" text-anchor="middle">• 파라미터 효율성</text>
<text x="550" y="640" class="bd" text-anchor="middle">• 메모리 최적화</text>
<rect x="1020" y="380" width="700" height="220" rx="30" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="450" class="h2" text-anchor="middle">2. RAFT 데이터</text>
<text x="1370" y="520" class="bd" text-anchor="middle">• Oracle + Distractors</text>
<rect x="1020" y="660" width="700" height="220" rx="30" fill="{C['b']}" opacity="0.1"/>
<text x="1370" y="730" class="h2" text-anchor="middle">3. 학습 & 평가</text>
<text x="1370" y="800" class="bd" text-anchor="middle">• Loss 곡선 이해</text>
{tip('💡 4개 섹션, 8개 실습 노트북으로 구성됩니다')}
</svg>'''

def slide_003():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">실습 노트북 구성</text>
<rect x="150" y="380" width="800" height="250" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="450" class="h2" text-anchor="middle">📚 Prerequisites (6개)</text>
<text x="550" y="520" class="sm" text-anchor="middle">00.01 환경설정 → 00.06 평가까지</text>
<text x="550" y="570" class="sm" text-anchor="middle">강사와 함께 기초 개념 학습</text>
<rect x="970" y="380" width="800" height="250" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="450" class="h2" text-anchor="middle">🔬 Main Practice (4개)</text>
<text x="1370" y="520" class="sm" text-anchor="middle">01 전처리 → 04 평가까지</text>
<text x="1370" y="570" class="sm" text-anchor="middle">실전 QLoRA Fine-tuning</text>
<text x="960" y="720" class="bd" text-anchor="middle" font-weight="700">오늘 강의는 이론 설명 → 실습은 노트북에서!</text>
{tip('💡 강의 슬라이드는 이론 중심, 코드는 Jupyter Notebook에서 실행')}
</svg>'''

def slide_004():
    return H + f'''
{dots()}
<text x="960" y="250" class="h1" text-anchor="middle">Section 1: Fine-tuning 기초</text>
{box(250, 400, 380, 280, C['p'], 'Full Fine-tuning', ['모든 파라미터 수정', '메모리 多', '성능 最高'])}
{box(770, 400, 380, 280, C['m'], 'LoRA', ['일부만 학습', '메모리 99%↓', '성능 유지'])}
{box(1290, 400, 380, 280, C['b'], 'QLoRA', ['4-bit 양자화', 'LoRA 결합', '메모리 最小'])}
<text x="960" y="780" class="h2" text-anchor="middle" fill="{C['pu']}">왜 LoRA를 사용할까?</text>
<text x="960" y="850" class="bd" text-anchor="middle">2.4B 모델도 Full Fine-tuning하면 96GB VRAM 필요!</text>
{tip('💡 LoRA는 학습 파라미터를 0.1%로 줄여도 성능을 유지합니다')}
</svg>'''

def slide_005():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Full Fine-tuning의 문제</text>
<rect x="200" y="320" width="1520" height="180" rx="20" fill="{C['p']}" opacity="0.15"/>
<text x="250" y="380" class="h2">EXAONE 3.5 2.4B 모델</text>
<text x="250" y="440" class="bd">• 24억개 파라미터 (2.4B parameters)</text>
<text x="250" y="490" class="bd">• 각 파라미터: 32-bit float → 4 bytes</text>
<rect x="200" y="540" width="740" height="300" rx="25" fill="{C['y']}" opacity="0.1"/>
<text x="570" y="610" class="h2" text-anchor="middle">필요 메모리 계산</text>
<text x="570" y="680" class="bd" text-anchor="middle">모델: 2.4B × 4 = 9.6GB</text>
<text x="570" y="730" class="bd" text-anchor="middle">Optimizer: 9.6GB × 8 = 76.8GB</text>
<text x="570" y="780" class="bd" text-anchor="middle">Gradient: 9.6GB</text>
<text x="570" y="820" class="bd" text-anchor="middle" font-weight="700" fill="#E74C3C">총 96GB VRAM!</text>
<rect x="980" y="540" width="740" height="300" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1350" y="610" class="h2" text-anchor="middle">현실적인 문제</text>
<text x="1350" y="680" class="bd" text-anchor="middle">❌ 일반 GPU로 불가능</text>
<text x="1350" y="730" class="bd" text-anchor="middle">❌ 학습 시간 매우 길다</text>
<text x="1350" y="780" class="bd" text-anchor="middle">❌ 비용이 너무 비싸다</text>
<text x="1350" y="820" class="bd" text-anchor="middle" fill="#27AE60" font-weight="700">→ LoRA 필요!</text>
{tip('💡 Adam Optimizer는 파라미터당 8배 메모리 필요 (momentum + variance)')}
</svg>'''

def slide_006():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">LoRA 핵심 아이디어</text>
<text x="960" y="340" class="h2" text-anchor="middle" fill="{C['pu']}">Low-Rank Adaptation</text>
<rect x="200" y="400" width="700" height="400" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="470" class="h2" text-anchor="middle">기존 방식</text>
<text x="550" y="540" class="bd" text-anchor="middle">W (1024 × 1024)</text>
<text x="550" y="600" class="bd" text-anchor="middle">↓ 모든 원소 수정</text>
<text x="550" y="660" class="bd" text-anchor="middle">W' (1024 × 1024)</text>
<text x="550" y="730" class="bd" text-anchor="middle" fill="#E74C3C">1,048,576개 파라미터 학습</text>
<rect x="1020" y="400" width="700" height="400" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="470" class="h2" text-anchor="middle">LoRA 방식</text>
<text x="1370" y="540" class="bd" text-anchor="middle">W (고정) + B×A</text>
<text x="1370" y="600" class="bd" text-anchor="middle">B(1024×8) × A(8×1024)</text>
<text x="1370" y="660" class="bd" text-anchor="middle">↓ rank=8 분해</text>
<text x="1370" y="730" class="bd" text-anchor="middle" fill="#27AE60">16,384개만 학습 (1.5%)</text>
{tip('💡 Low-Rank = 낮은 차원으로 분해. Rank는 행렬의 "본질적인 차원"')}
</svg>'''

def slide_007():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">LoRA 수식 이해하기</text>
<rect x="150" y="320" width="1620" height="150" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="410" class="h2" text-anchor="middle">h = W₀x + ΔWx = W₀x + BAx</text>
<rect x="200" y="520" width="500" height="340" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="450" y="590" class="h2" text-anchor="middle">W₀</text>
<text x="450" y="650" class="bd" text-anchor="middle">사전학습된 가중치</text>
<text x="450" y="710" class="bd" text-anchor="middle">고정 (frozen)</text>
<text x="450" y="770" class="bd" text-anchor="middle">학습하지 않음</text>
<rect x="750" y="520" width="500" height="340" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1000" y="590" class="h2" text-anchor="middle">B × A</text>
<text x="1000" y="650" class="bd" text-anchor="middle">LoRA 어댑터</text>
<text x="1000" y="710" class="bd" text-anchor="middle">학습 가능 (trainable)</text>
<text x="1000" y="770" class="bd" text-anchor="middle">B: (d × r)</text>
<text x="1000" y="820" class="bd" text-anchor="middle">A: (r × d)</text>
<rect x="1300" y="520" width="420" height="340" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1510" y="590" class="h2" text-anchor="middle">r (rank)</text>
<text x="1510" y="650" class="bd" text-anchor="middle">하이퍼파라미터</text>
<text x="1510" y="710" class="bd" text-anchor="middle">보통 4~64</text>
<text x="1510" y="770" class="bd" text-anchor="middle">작을수록 효율적</text>
<text x="1510" y="820" class="bd" text-anchor="middle">클수록 표현력 ↑</text>
{tip('💡 r=8일 때: 파라미터 수가 1024×1024에서 (1024×8 + 8×1024) = 16,384로 감소')}
</svg>'''

def slide_008():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">LoRA 하이퍼파라미터</text>
{box(200, 380, 500, 450, C['p'], 'r (rank)', ['LoRA 행렬의 차원', '', 'r↑ → 표현력↑ 메모리↑', 'r↓ → 효율↑ 성능↓', '', '권장: 8~16', 'EXAONE 실습: 64'])}
{box(760, 380, 500, 450, C['m'], 'alpha (scaling)', ['학습률 조정 계수', '', 'ΔW = (alpha/r) × BA', '', '보통 r의 2배', 'alpha=32, r=16', 'EXAONE 실습: 16'])}
{box(1310, 380, 410, 450, C['b'], 'dropout', ['과적합 방지', '', '0.05~0.1', '', 'EXAONE:', '0.05 사용'])}
{tip('💡 실습에서는 r=64, alpha=16, dropout=0.05 사용 (이론적으론 alpha=128이지만 실험적 조정)')}
</svg>'''

def slide_009():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">QLoRA = LoRA + 양자화</text>
<rect x="150" y="340" width="1620" height="120" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="420" class="h2" text-anchor="middle">4-bit Quantization + LoRA = 메모리 최소화</text>
<rect x="200" y="500" width="500" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="450" y="570" class="h2" text-anchor="middle">32-bit (FP32)</text>
<text x="450" y="640" class="bd" text-anchor="middle">일반 모델</text>
<text x="450" y="700" class="bd" text-anchor="middle">1개 = 4 bytes</text>
<text x="450" y="760" class="bd" text-anchor="middle">2.4B → 9.6GB</text>
<rect x="760" y="500" width="500" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1010" y="570" class="h2" text-anchor="middle">4-bit (NF4)</text>
<text x="1010" y="640" class="bd" text-anchor="middle">양자화된 모델</text>
<text x="1010" y="700" class="bd" text-anchor="middle">1개 = 0.5 bytes</text>
<text x="1010" y="760" class="bd" text-anchor="middle">2.4B → 1.2GB</text>
<text x="1010" y="810" class="bd" text-anchor="middle" fill="#27AE60">87.5% 절감!</text>
<rect x="1310" y="500" width="410" height="350" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1515" y="570" class="h2" text-anchor="middle">학습</text>
<text x="1515" y="640" class="bd" text-anchor="middle">W₀: 4-bit</text>
<text x="1515" y="700" class="bd" text-anchor="middle">(고정)</text>
<text x="1515" y="760" class="bd" text-anchor="middle">BA: 32-bit</text>
<text x="1515" y="810" class="bd" text-anchor="middle">(학습)</text>
{tip('💡 NF4 = Normal Float 4-bit. 가중치 분포에 최적화된 양자화 방식')}
</svg>'''

def slide_010():
    return H + f'''
{dots()}
<text x="960" y="220" class="h1" text-anchor="middle">메모리 사용량 비교</text>
<rect x="150" y="300" width="520" height="560" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="410" y="370" class="h2" text-anchor="middle">Full Fine-tuning</text>
<text x="410" y="450" class="bd" text-anchor="middle">모델: 9.6GB</text>
<text x="410" y="510" class="bd" text-anchor="middle">Optimizer: 76.8GB</text>
<text x="410" y="570" class="bd" text-anchor="middle">Gradient: 9.6GB</text>
<rect x="280" y="630" width="260" height="80" rx="15" fill="#E74C3C" opacity="0.3"/>
<text x="410" y="685" class="h2" text-anchor="middle" fill="#E74C3C">96GB</text>
<text x="410" y="780" class="bd" text-anchor="middle">A100 80GB로도 부족</text>
<rect x="700" y="300" width="520" height="560" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="960" y="370" class="h2" text-anchor="middle">LoRA</text>
<text x="960" y="450" class="bd" text-anchor="middle">모델: 9.6GB (고정)</text>
<text x="960" y="510" class="bd" text-anchor="middle">LoRA 파라미터: 0.01GB</text>
<text x="960" y="570" class="bd" text-anchor="middle">Optimizer: 0.08GB</text>
<rect x="830" y="630" width="260" height="80" rx="15" fill="#F39C12" opacity="0.3"/>
<text x="960" y="685" class="h2" text-anchor="middle" fill="#F39C12">~10GB</text>
<text x="960" y="780" class="bd" text-anchor="middle">RTX 3090 24GB 가능</text>
<rect x="1250" y="300" width="520" height="560" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1510" y="370" class="h2" text-anchor="middle">QLoRA</text>
<text x="1510" y="450" class="bd" text-anchor="middle">모델: 1.2GB (4-bit)</text>
<text x="1510" y="510" class="bd" text-anchor="middle">LoRA 파라미터: 0.01GB</text>
<text x="1510" y="570" class="bd" text-anchor="middle">Optimizer: 0.08GB</text>
<text x="1510" y="620" class="bd" text-anchor="middle">Activation: ~2GB</text>
<rect x="1380" y="670" width="260" height="80" rx="15" fill="#27AE60" opacity="0.3"/>
<text x="1510" y="725" class="h2" text-anchor="middle" fill="#27AE60">~3.5GB</text>
<text x="1510" y="780" class="bd" text-anchor="middle">Colab T4 16GB 충분!</text>
{tip('💡 QLoRA는 Full Fine-tuning 대비 메모리를 96GB → 3.5GB로 96% 이상 절감')}
</svg>'''

def slide_011():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">LoRA 적용 대상 선택</text>
<text x="960" y="340" class="h2" text-anchor="middle" fill="{C['pu']}">모든 레이어에 LoRA를 적용할까?</text>
<rect x="200" y="420" width="700" height="380" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="490" class="h2" text-anchor="middle">Attention 레이어</text>
<text x="550" y="570" class="bd" text-anchor="middle">Q, K, V, O 행렬</text>
<text x="550" y="630" class="bd" text-anchor="middle">가장 효과적</text>
<text x="550" y="690" class="bd" text-anchor="middle">필수 적용 대상</text>
<text x="550" y="750" class="bd" text-anchor="middle" fill="#27AE60" font-weight="700">✓ 권장</text>
<rect x="1020" y="420" width="700" height="380" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="490" class="h2" text-anchor="middle">FFN 레이어</text>
<text x="1370" y="570" class="bd" text-anchor="middle">Feed-Forward Network</text>
<text x="1370" y="630" class="bd" text-anchor="middle">선택적 적용</text>
<text x="1370" y="690" class="bd" text-anchor="middle">메모리↑ 성능↑</text>
<text x="1370" y="750" class="bd" text-anchor="middle" fill="#F39C12" font-weight="700">△ 선택</text>
<text x="960" y="880" class="bd" text-anchor="middle">EXAONE 실습: Q, K, V, O, Gate, Up, Down 모두 적용</text>
{tip('💡 target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]')}
</svg>'''

def slide_012():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">PEFT 라이브러리</text>
<text x="960" y="340" class="h2" text-anchor="middle" fill="{C['pu']}">Parameter-Efficient Fine-Tuning</text>
<rect x="150" y="420" width="1620" height="90" rx="15" fill="{C['p']}" opacity="0.15"/>
<text x="200" y="475" class="bd">from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training</text>
<rect x="200" y="550" width="700" height="280" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="550" y="620" class="h2" text-anchor="middle">LoraConfig</text>
<text x="550" y="690" class="bd" text-anchor="middle">r, alpha, dropout 설정</text>
<text x="550" y="740" class="bd" text-anchor="middle">target_modules 지정</text>
<text x="550" y="790" class="bd" text-anchor="middle">task_type 지정</text>
<rect x="1020" y="550" width="700" height="280" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1370" y="620" class="h2" text-anchor="middle">get_peft_model</text>
<text x="1370" y="690" class="bd" text-anchor="middle">기존 모델 + LoRA</text>
<text x="1370" y="740" class="bd" text-anchor="middle">학습 가능 파라미터 추가</text>
<text x="1370" y="790" class="bd" text-anchor="middle">자동으로 어댑터 삽입</text>
<text x="960" y="900" class="bd" text-anchor="middle">Hugging Face 공식 라이브러리로 LoRA 구현 간단!</text>
{tip('💡 PEFT는 LoRA 외에도 Prefix Tuning, P-Tuning, AdaLoRA 등 다양한 방법 지원')}
</svg>'''

def slide_013():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Fine-tuning 성공 조건</text>
{box(200, 380, 500, 200, C['p'], '충분한 데이터', ['최소 100~1000개', '도메인 특화', '고품질'])}
{box(760, 380, 500, 200, C['m'], '적절한 파라미터', ['r, alpha 조정', 'learning_rate', 'batch_size'])}
{box(1310, 380, 410, 200, C['b'], '평가 지표', ['ROUGE', 'BLEU', 'Perplexity'])}
{box(200, 640, 500, 200, C['y'], '과적합 방지', ['Dropout', 'Early stopping', 'Validation'])}
{box(760, 640, 500, 200, C['pu'], '계산 자원', ['GPU 메모리', '학습 시간', 'Batch size'])}
{box(1310, 640, 410, 200, C['o'], '도메인 적합성', ['task 맞춤', '베이스 모델', '선택'])}
{tip('💡 오늘 실습에서는 이 6가지 요소를 모두 다룹니다')}
</svg>'''

def slide_014():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">LoRA vs QLoRA 요약</text>
<rect x="150" y="340" width="800" height="80" rx="15" fill="{C['pu']}" opacity="0.15"/>
<text x="550" y="395" class="h2" text-anchor="middle">LoRA</text>
<rect x="970" y="340" width="800" height="80" rx="15" fill="{C['b']}" opacity="0.15"/>
<text x="1370" y="395" class="h2" text-anchor="middle">QLoRA</text>
<rect x="150" y="460" width="800" height="80" rx="15" fill="{C['p']}" opacity="0.1"/>
<text x="250" y="515" class="bd">모델 정밀도</text>
<text x="700" y="515" class="bd" text-anchor="end">FP32/FP16</text>
<rect x="970" y="460" width="800" height="80" rx="15" fill="{C['p']}" opacity="0.1"/>
<text x="1070" y="515" class="bd">모델 정밀도</text>
<text x="1720" y="515" class="bd" text-anchor="end">4-bit (NF4)</text>
<rect x="150" y="560" width="800" height="80" rx="15" fill="{C['m']}" opacity="0.1"/>
<text x="250" y="615" class="bd">메모리 사용</text>
<text x="700" y="615" class="bd" text-anchor="end">~10GB</text>
<rect x="970" y="560" width="800" height="80" rx="15" fill="{C['m']}" opacity="0.1"/>
<text x="1070" y="615" class="bd">메모리 사용</text>
<text x="1720" y="615" class="bd" text-anchor="end">~3.5GB</text>
<rect x="150" y="660" width="800" height="80" rx="15" fill="{C['y']}" opacity="0.1"/>
<text x="250" y="715" class="bd">학습 속도</text>
<text x="700" y="715" class="bd" text-anchor="end">빠름</text>
<rect x="970" y="660" width="800" height="80" rx="15" fill="{C['y']}" opacity="0.1"/>
<text x="1070" y="715" class="bd">학습 속도</text>
<text x="1720" y="715" class="bd" text-anchor="end">조금 느림</text>
<rect x="150" y="760" width="800" height="80" rx="15" fill="{C['b']}" opacity="0.1"/>
<text x="250" y="815" class="bd">성능</text>
<text x="700" y="815" class="bd" text-anchor="end">우수</text>
<rect x="970" y="760" width="800" height="80" rx="15" fill="{C['b']}" opacity="0.1"/>
<text x="1070" y="815" class="bd">성능</text>
<text x="1720" y="815" class="bd" text-anchor="end">거의 동일</text>
{tip('💡 메모리가 충분하면 LoRA, 제한적이면 QLoRA (실습은 QLoRA 사용)')}
</svg>'''

def slide_015():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">Section 1 정리</text>
<rect x="200" y="380" width="1520" height="450" rx="30" fill="{C['p']}" opacity="0.05"/>
<text x="960" y="460" class="h2" text-anchor="middle">핵심 개념</text>
<text x="300" y="540" class="bd">✓ Full Fine-tuning은 메모리가 너무 많이 필요 (96GB)</text>
<text x="300" y="610" class="bd">✓ LoRA는 Low-Rank 분해로 파라미터를 99% 절감</text>
<text x="300" y="680" class="bd">✓ QLoRA는 4-bit 양자화 + LoRA로 메모리 최소화</text>
<text x="300" y="750" class="bd">✓ 하이퍼파라미터: r (rank), alpha (scaling), dropout</text>
<text x="960" y="870" class="h2" text-anchor="middle" fill="{C['b']}">다음: RAFT 데이터는 왜 필요한가?</text>
{tip('💡 이제 LoRA로 효율적으로 학습할 수 있다는 걸 알았으니, 어떤 데이터로 학습할지 알아봅시다')}
</svg>'''

def slide_016():
    return H + f'''
{dots()}
<text x="960" y="250" class="h1" text-anchor="middle">Section 2: RAFT 데이터</text>
<text x="960" y="350" class="h2" text-anchor="middle" fill="{C['pu']}">Retrieval Augmented Fine-Tuning</text>
<rect x="200" y="440" width="1520" height="100" rx="15" fill="{C['p']}" opacity="0.15"/>
<text x="960" y="505" class="bd" text-anchor="middle">RAG (검색) + Fine-tuning (학습) = RAFT</text>
{box(250, 600, 650, 230, C['m'], 'RAG의 한계', ['실시간 검색 필요', '응답 속도 느림', '프롬프트 길이 제한'])}
{box(1020, 600, 650, 230, C['b'], 'RAFT의 장점', ['모델에 지식 내재화', '검색 없이 빠른 응답', '도메인 특화 성능↑'])}
{tip('💡 RAFT는 RAG의 검색 결과를 학습 데이터로 만들어 모델을 fine-tuning')}
</svg>'''

def slide_017():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">RAFT 데이터 구조</text>
<rect x="150" y="340" width="1620" height="120" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="410" class="h2" text-anchor="middle">질문 + Oracle 문서 + Distractor 문서들</text>
<rect x="200" y="500" width="500" height="330" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="450" y="570" class="h2" text-anchor="middle">Question</text>
<text x="450" y="640" class="bd" text-anchor="middle">사용자 질의</text>
<text x="450" y="700" class="bd" text-anchor="middle">"EXAONE이란?"</text>
<rect x="760" y="500" width="500" height="330" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1010" y="570" class="h2" text-anchor="middle">Oracle</text>
<text x="1010" y="640" class="bd" text-anchor="middle">정답 문서</text>
<text x="1010" y="700" class="bd" text-anchor="middle">관련도 높음</text>
<text x="1010" y="760" class="bd" text-anchor="middle" fill="#27AE60" font-weight="700">1개 (golden)</text>
<rect x="1310" y="500" width="410" height="330" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1515" y="570" class="h2" text-anchor="middle">Distractors</text>
<text x="1515" y="640" class="bd" text-anchor="middle">노이즈 문서</text>
<text x="1515" y="700" class="bd" text-anchor="middle">관련도 낮음</text>
<text x="1515" y="760" class="bd" text-anchor="middle" fill="#E74C3C" font-weight="700">3~4개</text>
{tip('💡 Oracle 1개 + Distractors 3개 = 총 4개 문서를 함께 제시 (현실 RAG 상황 모사)')}
</svg>'''

def slide_018():
    return H + f'''
{dots()}
<text x="960" y="220" class="h1" text-anchor="middle">왜 Distractor가 필요한가?</text>
<rect x="200" y="320" width="700" height="500" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="390" class="h2" text-anchor="middle">Oracle만 학습</text>
<text x="550" y="480" class="bd" text-anchor="middle">❌ 항상 좋은 문서만</text>
<text x="550" y="540" class="bd" text-anchor="middle">❌ 노이즈 대응 못함</text>
<text x="550" y="600" class="bd" text-anchor="middle">❌ 현실과 괴리</text>
<text x="550" y="680" class="bd" text-anchor="middle" fill="#E74C3C">과적합 위험</text>
<text x="550" y="760" class="bd" text-anchor="middle">실전 RAG에서는</text>
<text x="550" y="810" class="bd" text-anchor="middle">관련 없는 문서도 검색됨</text>
<rect x="1020" y="320" width="700" height="500" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="390" class="h2" text-anchor="middle">Oracle + Distractors</text>
<text x="1370" y="480" class="bd" text-anchor="middle">✓ 노이즈 섞인 상황</text>
<text x="1370" y="540" class="bd" text-anchor="middle">✓ 관련 문서 찾기 학습</text>
<text x="1370" y="600" class="bd" text-anchor="middle">✓ 현실적인 시나리오</text>
<text x="1370" y="680" class="bd" text-anchor="middle" fill="#27AE60">일반화 능력↑</text>
<text x="1370" y="760" class="bd" text-anchor="middle">모델이 스스로</text>
<text x="1370" y="810" class="bd" text-anchor="middle">유용한 정보 선별 학습</text>
{tip('💡 Distractor는 "산만하게 하는 것". 모델이 노이즈 속에서 정답을 찾도록 훈련')}
</svg>'''

def slide_019():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">RAFT 데이터 예시</text>
<rect x="150" y="320" width="1620" height="90" rx="15" fill="{C['pu']}" opacity="0.15"/>
<text x="200" y="375" class="h2">Question: "QLoRA의 메모리 절감 원리는?"</text>
<rect x="200" y="450" width="800" height="380" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="600" y="520" class="h2" text-anchor="middle">Oracle (정답 문서)</text>
<text x="250" y="590" class="bd">"QLoRA는 4-bit NF4 양자화를</text>
<text x="250" y="640" class="bd">통해 모델 가중치를 압축합니다.</text>
<text x="250" y="690" class="bd">기존 32-bit 대비 87.5% 메모리</text>
<text x="250" y="740" class="bd">절감 효과가 있습니다."</text>
<text x="600" y="800" class="bd" text-anchor="middle" fill="#27AE60" font-weight="700">✓ 질문과 직접 관련</text>
<rect x="1050" y="450" width="670" height="380" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="1385" y="520" class="h2" text-anchor="middle">Distractors (노이즈 문서)</text>
<text x="1100" y="590" class="sm">"LoRA는 Low-Rank Adaptation의 약자..."</text>
<text x="1100" y="640" class="sm">"PEFT 라이브러리 설치 방법은..."</text>
<text x="1100" y="690" class="sm">"Transformer 구조는 Attention 기반..."</text>
<text x="1385" y="780" class="bd" text-anchor="middle" fill="#E74C3C" font-weight="700">△ 관련 있지만 정답 아님</text>
{tip('💡 실습 데이터셋: neural-bridge/rag-dataset-12000 (12,000개 RAFT 샘플)')}
</svg>'''

def slide_020():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">데이터 전처리 과정</text>
<rect x="200" y="340" width="340" height="480" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="370" y="410" class="h2" text-anchor="middle">1. 데이터 로드</text>
<text x="370" y="490" class="bd" text-anchor="middle">Hugging Face</text>
<text x="370" y="540" class="bd" text-anchor="middle">datasets 라이브러리</text>
<text x="370" y="590" class="bd" text-anchor="middle">12,000개 샘플</text>
<text x="370" y="690" class="bd" text-anchor="middle">↓</text>
<text x="370" y="750" class="bd" text-anchor="middle">Question</text>
<text x="370" y="800" class="bd" text-anchor="middle">+ Documents</text>
<rect x="590" y="340" width="340" height="480" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="760" y="410" class="h2" text-anchor="middle">2. RAFT 변환</text>
<text x="760" y="490" class="bd" text-anchor="middle">1 Oracle</text>
<text x="760" y="540" class="bd" text-anchor="middle">+ 3 Distractors</text>
<text x="760" y="590" class="bd" text-anchor="middle">무작위 섞기</text>
<text x="760" y="690" class="bd" text-anchor="middle">↓</text>
<text x="760" y="750" class="bd" text-anchor="middle">Context</text>
<text x="760" y="800" class="bd" text-anchor="middle">구성</text>
<rect x="980" y="340" width="360" height="480" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1160" y="410" class="h2" text-anchor="middle">3. 토크나이징</text>
<text x="1160" y="490" class="bd" text-anchor="middle">EXAONE</text>
<text x="1160" y="540" class="bd" text-anchor="middle">Tokenizer</text>
<text x="1160" y="590" class="bd" text-anchor="middle">Label 마스킹</text>
<text x="1160" y="690" class="bd" text-anchor="middle">↓</text>
<text x="1160" y="750" class="bd" text-anchor="middle">input_ids</text>
<text x="1160" y="800" class="bd" text-anchor="middle">labels</text>
<rect x="1390" y="340" width="330" height="480" rx="25" fill="{C['y']}" opacity="0.1"/>
<text x="1555" y="410" class="h2" text-anchor="middle">4. 저장</text>
<text x="1555" y="490" class="bd" text-anchor="middle">Dataset</text>
<text x="1555" y="540" class="bd" text-anchor="middle">객체 생성</text>
<text x="1555" y="590" class="bd" text-anchor="middle">검증</text>
<text x="1555" y="690" class="bd" text-anchor="middle">↓</text>
<text x="1555" y="750" class="bd" text-anchor="middle">학습 준비</text>
<text x="1555" y="800" class="bd" text-anchor="middle">완료</text>
{tip('💡 실습 01번 노트북에서 이 4단계를 직접 수행합니다')}
</svg>'''

def slide_021():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Label 마스킹이란?</text>
<rect x="150" y="330" width="1620" height="110" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="405" class="h2" text-anchor="middle">Instruction 부분은 학습하지 않고, Answer만 학습</text>
<rect x="200" y="480" width="700" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="550" class="h2" text-anchor="middle">마스킹 없이</text>
<text x="550" y="630" class="bd" text-anchor="middle">전체 텍스트 학습</text>
<text x="550" y="690" class="bd" text-anchor="middle">질문도 예측하려 함</text>
<text x="550" y="750" class="bd" text-anchor="middle" fill="#E74C3C">비효율적</text>
<text x="550" y="810" class="bd" text-anchor="middle">질문 형식만 외움</text>
<rect x="1020" y="480" width="700" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="550" class="h2" text-anchor="middle">마스킹 적용</text>
<text x="1370" y="630" class="bd" text-anchor="middle">Answer 부분만 학습</text>
<text x="1370" y="690" class="bd" text-anchor="middle">labels[:-answer_len] = -100</text>
<text x="1370" y="750" class="bd" text-anchor="middle" fill="#27AE60">효율적</text>
<text x="1370" y="810" class="bd" text-anchor="middle">답변 생성에 집중</text>
{tip('💡 -100은 PyTorch에서 손실 계산 시 무시하는 특수 값')}
</svg>'''

def slide_022():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">데이터 품질 체크</text>
<text x="960" y="340" class="h2" text-anchor="middle" fill="{C['pu']}">전처리 후 반드시 확인해야 할 것들</text>
{box(200, 420, 500, 400, C['p'], '토큰 길이 분포', ['평균 길이', '최대 길이', '이상치 확인', '', 'max_length 설정', '근거 마련'])}
{box(760, 420, 500, 400, C['m'], '데이터 밸런스', ['Oracle 위치 분포', '4개 문서 균등?', 'Question 다양성', '', '편향 여부 확인'])}
{box(1310, 420, 410, 400, C['b'], '샘플 검증', ['텍스트 출력', '토큰 ID', 'Label 확인', '', '육안 검사'])}
{tip('💡 실습 02번 노트북에서 토큰 길이 히스토그램과 통계를 시각화')}
</svg>'''

def slide_023():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">토큰 길이의 중요성</text>
<rect x="200" y="340" width="700" height="460" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="410" class="h2" text-anchor="middle">너무 짧으면</text>
<text x="550" y="500" class="bd" text-anchor="middle">• 정보 부족</text>
<text x="550" y="560" class="bd" text-anchor="middle">• Context 불충분</text>
<text x="550" y="620" class="bd" text-anchor="middle">• 학습 효과 ↓</text>
<text x="550" y="720" class="bd" text-anchor="middle" fill="#E74C3C">답변 품질 저하</text>
<rect x="1020" y="340" width="700" height="460" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="410" class="h2" text-anchor="middle">너무 길면</text>
<text x="1370" y="500" class="bd" text-anchor="middle">• 메모리 부족</text>
<text x="1370" y="560" class="bd" text-anchor="middle">• 학습 시간 ↑</text>
<text x="1370" y="620" class="bd" text-anchor="middle">• Truncation 발생</text>
<text x="1370" y="720" class="bd" text-anchor="middle" fill="#E74C3C">정보 손실</text>
<rect x="200" y="850" width="1520" height="70" rx="15" fill="{C['b']}" opacity="0.15"/>
<text x="960" y="900" class="h2" text-anchor="middle">EXAONE 실습: max_length=2048 (평균 ~800)</text>
{tip('💡 평균 길이의 2~3배로 max_length 설정하면 대부분 샘플 수용 가능')}
</svg>'''

def slide_024():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">EXAONE 모델 특징</text>
<rect x="150" y="330" width="1620" height="100" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="400" class="h2" text-anchor="middle">LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct</text>
<rect x="200" y="470" width="500" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="450" y="540" class="h2" text-anchor="middle">모델 규모</text>
<text x="450" y="620" class="bd" text-anchor="middle">2.4B 파라미터</text>
<text x="450" y="680" class="bd" text-anchor="middle">32층 Transformer</text>
<text x="450" y="740" class="bd" text-anchor="middle">작지만 강력</text>
<rect x="760" y="470" width="500" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1010" y="540" class="h2" text-anchor="middle">한국어 특화</text>
<text x="1010" y="620" class="bd" text-anchor="middle">LG AI Research</text>
<text x="1010" y="680" class="bd" text-anchor="middle">한국어 성능 우수</text>
<text x="1010" y="740" class="bd" text-anchor="middle">Instruction 튜닝</text>
<rect x="1310" y="470" width="410" height="350" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1515" y="540" class="h2" text-anchor="middle">활용</text>
<text x="1515" y="620" class="bd" text-anchor="middle">QA</text>
<text x="1515" y="680" class="bd" text-anchor="middle">요약</text>
<text x="1515" y="740" class="bd" text-anchor="middle">대화</text>
{tip('💡 EXAONE 3.5는 7.8B 버전도 있지만, 실습에서는 가벼운 2.4B 사용')}
</svg>'''

def slide_025():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Chat Template 이해</text>
<rect x="150" y="330" width="1620" height="120" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="410" class="h2" text-anchor="middle">모델마다 다른 대화 형식 (ChatML, Llama, EXAONE...)</text>
<rect x="200" y="490" width="1520" height="330" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="560" class="h2" text-anchor="middle">EXAONE Chat Template</text>
<rect x="250" y="610" width="1420" height="180" rx="15" fill="#F8F9FA"/>
<text x="300" y="655" class="code">[|system|]System prompt[|endofturn|]</text>
<text x="300" y="695" class="code">[|user|]Question + Context[|endofturn|]</text>
<text x="300" y="735" class="code">[|assistant|]Answer[|endofturn|]</text>
{tip('💡 토크나이저가 자동으로 변환해줌: tokenizer.apply_chat_template(messages)')}
</svg>'''

def slide_026():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Context 구성 전략</text>
<rect x="200" y="340" width="700" height="460" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="410" class="h2" text-anchor="middle">순서 랜덤화</text>
<text x="550" y="500" class="bd" text-anchor="middle">Oracle 위치 섞기</text>
<text x="550" y="560" class="bd" text-anchor="middle">첫 번째가 항상 정답?</text>
<text x="550" y="620" class="bd" text-anchor="middle">→ 모델이 위치 학습</text>
<text x="550" y="720" class="bd" text-anchor="middle" fill="#27AE60">랜덤 배치로 내용 학습</text>
<rect x="1020" y="340" width="700" height="460" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="410" class="h2" text-anchor="middle">Document 개수</text>
<text x="1370" y="500" class="bd" text-anchor="middle">1 Oracle + 3 Distractors</text>
<text x="1370" y="560" class="bd" text-anchor="middle">총 4개 문서</text>
<text x="1370" y="620" class="bd" text-anchor="middle">실전 RAG top-k=4 모사</text>
<text x="1370" y="720" class="bd" text-anchor="middle" fill="#27AE60">현실적인 시나리오</text>
{tip('💡 실습에서는 random.shuffle()로 매번 다른 순서 생성')}
</svg>'''

def slide_027():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">데이터 분할 전략</text>
<rect x="150" y="330" width="1620" height="110" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="405" class="h2" text-anchor="middle">Train / Validation 분리로 과적합 방지</text>
<rect x="200" y="480" width="800" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="600" y="550" class="h2" text-anchor="middle">Train Set (90%)</text>
<text x="600" y="630" class="bd" text-anchor="middle">10,800개 샘플</text>
<text x="600" y="690" class="bd" text-anchor="middle">모델 학습용</text>
<text x="600" y="750" class="bd" text-anchor="middle">Loss 최소화</text>
<rect x="1050" y="480" width="670" height="350" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1385" y="550" class="h2" text-anchor="middle">Validation Set (10%)</text>
<text x="1385" y="630" class="bd" text-anchor="middle">1,200개 샘플</text>
<text x="1385" y="690" class="bd" text-anchor="middle">성능 검증용</text>
<text x="1385" y="750" class="bd" text-anchor="middle">과적합 감지</text>
<text x="960" y="900" class="bd" text-anchor="middle">학습 중 Validation Loss 지속 모니터링!</text>
{tip('💡 Validation Loss가 증가하면 과적합 신호 → Early stopping 고려')}
</svg>'''

def slide_028():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">과적합(Overfitting) 이해</text>
<rect x="200" y="340" width="700" height="460" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="410" class="h2" text-anchor="middle">정상 학습</text>
<text x="550" y="500" class="bd" text-anchor="middle">Train Loss ↓</text>
<text x="550" y="560" class="bd" text-anchor="middle">Val Loss ↓</text>
<text x="550" y="620" class="bd" text-anchor="middle">두 곡선 함께 감소</text>
<text x="550" y="720" class="bd" text-anchor="middle" fill="#27AE60">일반화 잘 됨</text>
<rect x="1020" y="340" width="700" height="460" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="410" class="h2" text-anchor="middle">과적합</text>
<text x="1370" y="500" class="bd" text-anchor="middle">Train Loss ↓</text>
<text x="1370" y="560" class="bd" text-anchor="middle">Val Loss ↑</text>
<text x="1370" y="620" class="bd" text-anchor="middle">학습 데이터만 외움</text>
<text x="1370" y="720" class="bd" text-anchor="middle" fill="#E74C3C">새 데이터 성능↓</text>
{tip('💡 실습 03번 노트북에서 Loss 곡선 그래프로 확인')}
</svg>'''

def slide_029():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">neural-bridge 데이터셋</text>
<rect x="150" y="330" width="1620" height="100" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="400" class="h2" text-anchor="middle">neural-bridge/rag-dataset-12000</text>
<rect x="200" y="470" width="500" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="450" y="540" class="h2" text-anchor="middle">구성</text>
<text x="450" y="620" class="bd" text-anchor="middle">12,000개 QA 쌍</text>
<text x="450" y="680" class="bd" text-anchor="middle">다양한 도메인</text>
<text x="450" y="740" class="bd" text-anchor="middle">RAFT 형식</text>
<rect x="760" y="470" width="500" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1010" y="540" class="h2" text-anchor="middle">특징</text>
<text x="1010" y="620" class="bd" text-anchor="middle">Oracle + Distractors</text>
<text x="1010" y="680" class="bd" text-anchor="middle">고품질 레이블</text>
<text x="1010" y="740" class="bd" text-anchor="middle">한국어 포함</text>
<rect x="1310" y="470" width="410" height="350" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1515" y="540" class="h2" text-anchor="middle">용도</text>
<text x="1515" y="620" class="bd" text-anchor="middle">RAG 학습</text>
<text x="1515" y="680" class="bd" text-anchor="middle">QA 연구</text>
<text x="1515" y="740" class="bd" text-anchor="middle">벤치마크</text>
{tip('💡 Hugging Face Hub에서 datasets.load_dataset()으로 간단히 로드')}
</svg>'''

def slide_030():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">Section 2 정리</text>
<rect x="200" y="380" width="1520" height="450" rx="30" fill="{C['m']}" opacity="0.05"/>
<text x="960" y="460" class="h2" text-anchor="middle">핵심 개념</text>
<text x="300" y="540" class="bd">✓ RAFT = RAG + Fine-tuning (검색 결과를 학습 데이터로)</text>
<text x="300" y="610" class="bd">✓ Oracle (정답) + Distractors (노이즈)로 현실적인 시나리오 학습</text>
<text x="300" y="680" class="bd">✓ Label 마스킹으로 Answer 부분만 효율적으로 학습</text>
<text x="300" y="750" class="bd">✓ 토큰 길이 분포 확인으로 max_length 설정</text>
<text x="960" y="870" class="h2" text-anchor="middle" fill="{C['b']}">다음: 학습 과정과 손실 함수 이해</text>
{tip('💡 좋은 데이터가 준비되었으니, 이제 실제 학습 과정을 알아봅시다')}
</svg>'''

def slide_031():
    return H + f'''
{dots()}
<text x="960" y="250" class="h1" text-anchor="middle">Section 3: 학습 이론</text>
<text x="960" y="350" class="h2" text-anchor="middle" fill="{C['pu']}">QLoRA Fine-tuning 학습 과정</text>
{box(250, 480, 650, 300, C['p'], '학습 설정', ['BitsAndBytes 4-bit', 'LoRA Config 적용', 'Trainer 초기화'])}
{box(1020, 480, 650, 300, C['m'], '학습 실행', ['Epoch 반복', 'Batch별 Loss 계산', 'Gradient Update'])}
{tip('💡 실습 03번 노트북에서 QLoRA 학습 전체 과정 실행')}
</svg>'''

def slide_032():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">BitsAndBytes Config</text>
<rect x="150" y="330" width="1620" height="120" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="410" class="h2" text-anchor="middle">4-bit 양자화 설정</text>
<rect x="200" y="490" width="500" height="330" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="450" y="560" class="h2" text-anchor="middle">load_in_4bit</text>
<text x="450" y="640" class="bd" text-anchor="middle">4-bit로 로드</text>
<text x="450" y="700" class="bd" text-anchor="middle">True</text>
<rect x="760" y="490" width="500" height="330" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1010" y="560" class="h2" text-anchor="middle">bnb_4bit_quant_type</text>
<text x="1010" y="640" class="bd" text-anchor="middle">양자화 타입</text>
<text x="1010" y="700" class="bd" text-anchor="middle">"nf4"</text>
<text x="1010" y="760" class="bd" text-anchor="middle">Normal Float 4-bit</text>
<rect x="1310" y="490" width="410" height="330" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1515" y="560" class="h2" text-anchor="middle">compute_dtype</text>
<text x="1515" y="640" class="bd" text-anchor="middle">계산 정밀도</text>
<text x="1515" y="700" class="bd" text-anchor="middle">bfloat16</text>
<text x="1515" y="760" class="bd" text-anchor="middle">효율+안정성</text>
{tip('💡 BitsAndBytesConfig는 모델 로드 시 적용 (AutoModelForCausalLM.from_pretrained)')}
</svg>'''

def slide_033():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">TrainingArguments 주요 설정</text>
{box(200, 380, 500, 180, C['p'], 'output_dir', ['모델 저장 경로', '"./exaone-qlora"'])}
{box(200, 600, 500, 180, C['m'], 'num_train_epochs', ['학습 에폭 수', '3~5 epoch'])}
{box(760, 380, 500, 180, C['b'], 'per_device_train_batch_size', ['배치 크기', '1~4 (메모리 고려)'])}
{box(760, 600, 500, 180, C['y'], 'gradient_accumulation_steps', ['그래디언트 누적', '4~8 (effective batch↑)'])}
{box(1310, 380, 410, 180, C['pu'], 'learning_rate', ['학습률', '2e-4'])}
{box(1310, 600, 410, 180, C['o'], 'logging_steps', ['로그 주기', '10'])}
{tip('💡 batch_size=1, accumulation=8 → effective batch size=8')}
</svg>'''

def slide_034():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">학습률(Learning Rate)의 중요성</text>
<rect x="200" y="340" width="700" height="460" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="410" class="h2" text-anchor="middle">너무 크면</text>
<text x="550" y="500" class="bd" text-anchor="middle">• Loss 발산</text>
<text x="550" y="560" class="bd" text-anchor="middle">• 학습 불안정</text>
<text x="550" y="620" class="bd" text-anchor="middle">• 최적점 건너뜀</text>
<text x="550" y="720" class="bd" text-anchor="middle" fill="#E74C3C">lr = 1e-3 이상 위험</text>
<rect x="1020" y="340" width="700" height="460" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="410" class="h2" text-anchor="middle">너무 작으면</text>
<text x="1370" y="500" class="bd" text-anchor="middle">• 학습 너무 느림</text>
<text x="1370" y="560" class="bd" text-anchor="middle">• 수렴 안 함</text>
<text x="1370" y="620" class="bd" text-anchor="middle">• 시간 낭비</text>
<text x="1370" y="720" class="bd" text-anchor="middle" fill="#E74C3C">lr = 1e-6 이하 비효율</text>
<rect x="200" y="850" width="1520" height="70" rx="15" fill="{C['b']}" opacity="0.15"/>
<text x="960" y="900" class="h2" text-anchor="middle">LoRA 권장: 1e-4 ~ 5e-4 (실습: 2e-4)</text>
{tip('💡 Full Fine-tuning(1e-5)보다 LoRA는 10배 큰 학습률 사용 (학습 파라미터 적어서)')}
</svg>'''

def slide_035():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Gradient Accumulation</text>
<rect x="150" y="330" width="1620" height="110" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="405" class="h2" text-anchor="middle">작은 배치로 큰 배치 효과 내기</text>
<rect x="200" y="480" width="700" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="550" class="h2" text-anchor="middle">일반적인 학습</text>
<text x="550" y="630" class="bd" text-anchor="middle">batch_size = 8</text>
<text x="550" y="690" class="bd" text-anchor="middle">→ 8개씩 처리</text>
<text x="550" y="750" class="bd" text-anchor="middle">→ 업데이트</text>
<text x="550" y="810" class="bd" text-anchor="middle" fill="#E74C3C">메모리 부족 가능</text>
<rect x="1020" y="480" width="700" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="550" class="h2" text-anchor="middle">Gradient Accumulation</text>
<text x="1370" y="630" class="bd" text-anchor="middle">batch_size = 1</text>
<text x="1370" y="690" class="bd" text-anchor="middle">accumulation = 8</text>
<text x="1370" y="750" class="bd" text-anchor="middle">→ 8번 누적 후 업데이트</text>
<text x="1370" y="810" class="bd" text-anchor="middle" fill="#27AE60">메모리 절약</text>
{tip('💡 메모리가 부족할 때 effective batch size를 키우는 핵심 기법')}
</svg>'''

def slide_036():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Loss Function 이해</text>
<rect x="150" y="330" width="1620" height="120" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="410" class="h2" text-anchor="middle">Cross-Entropy Loss (언어 모델 표준)</text>
<rect x="200" y="490" width="1520" height="330" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="560" class="h2" text-anchor="middle">Loss 계산 과정</text>
<text x="300" y="650" class="bd">1. 모델이 다음 토큰 확률 분포 예측</text>
<text x="300" y="710" class="bd">2. 정답 토큰과 비교 (Label)</text>
<text x="300" y="770" class="bd">3. Cross-Entropy로 차이 계산 → Loss 값</text>
<text x="960" y="880" class="h2" text-anchor="middle" fill="{C['b']}">Loss ↓ = 모델 예측이 정답에 가까워짐</text>
{tip('💡 Loss가 낮을수록 좋지만, Validation Loss도 함께 확인해야 과적합 방지')}
</svg>'''

def slide_037():
    return H + f'''
{dots()}
<text x="960" y="220" class="h1" text-anchor="middle">학습 곡선 패턴</text>
<rect x="200" y="320" width="520" height="500" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="460" y="390" class="h2" text-anchor="middle">정상 학습</text>
<text x="460" y="480" class="bd" text-anchor="middle">Train Loss: 2.5 → 0.8</text>
<text x="460" y="540" class="bd" text-anchor="middle">Val Loss: 2.6 → 1.0</text>
<text x="460" y="600" class="bd" text-anchor="middle">두 곡선 평행</text>
<text x="460" y="680" class="bd" text-anchor="middle" fill="#27AE60">✓ 학습 계속</text>
<rect x="750" y="320" width="520" height="500" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1010" y="390" class="h2" text-anchor="middle">과적합 시작</text>
<text x="1010" y="480" class="bd" text-anchor="middle">Train Loss: ↓↓ 계속 감소</text>
<text x="1010" y="540" class="bd" text-anchor="middle">Val Loss: ↑ 증가 시작</text>
<text x="1010" y="600" class="bd" text-anchor="middle">격차 벌어짐</text>
<text x="1010" y="680" class="bd" text-anchor="middle" fill="#F39C12">△ 주의 필요</text>
<rect x="1300" y="320" width="420" height="500" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1510" y="390" class="h2" text-anchor="middle">학습 실패</text>
<text x="1510" y="480" class="bd" text-anchor="middle">Loss 발산</text>
<text x="1510" y="540" class="bd" text-anchor="middle">NaN 발생</text>
<text x="1510" y="600" class="bd" text-anchor="middle">진동</text>
<text x="1510" y="680" class="bd" text-anchor="middle" fill="#E74C3C">✗ 재시작</text>
<text x="1510" y="740" class="sm" text-anchor="middle">lr 줄이기</text>
{tip('💡 실습에서는 matplotlib로 Loss 곡선을 그려서 패턴 확인')}
</svg>'''

def slide_038():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">SFTTrainer 활용</text>
<rect x="150" y="330" width="1620" height="100" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="400" class="h2" text-anchor="middle">Supervised Fine-Tuning Trainer (TRL 라이브러리)</text>
<rect x="200" y="470" width="500" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="450" y="540" class="h2" text-anchor="middle">일반 Trainer</text>
<text x="450" y="620" class="bd" text-anchor="middle">Hugging Face 기본</text>
<text x="450" y="680" class="bd" text-anchor="middle">범용적</text>
<text x="450" y="740" class="bd" text-anchor="middle">직접 설정 多</text>
<rect x="760" y="470" width="500" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1010" y="540" class="h2" text-anchor="middle">SFTTrainer</text>
<text x="1010" y="620" class="bd" text-anchor="middle">Chat 모델 특화</text>
<text x="1010" y="680" class="bd" text-anchor="middle">PEFT 통합</text>
<text x="1010" y="740" class="bd" text-anchor="middle">간편한 설정</text>
<rect x="1310" y="470" width="410" height="350" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1515" y="540" class="h2" text-anchor="middle">장점</text>
<text x="1515" y="620" class="bd" text-anchor="middle">자동 포맷팅</text>
<text x="1515" y="680" class="bd" text-anchor="middle">LoRA 지원</text>
<text x="1515" y="740" class="bd" text-anchor="middle">best practice</text>
{tip('💡 from trl import SFTTrainer - Instruction 튜닝에 최적화')}
</svg>'''

def slide_039():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Epoch와 Step 이해</text>
<rect x="150" y="330" width="1620" height="110" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="405" class="h2" text-anchor="middle">전체 데이터를 몇 번 반복할까?</text>
<rect x="200" y="480" width="700" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="550" class="h2" text-anchor="middle">Epoch</text>
<text x="550" y="630" class="bd" text-anchor="middle">전체 데이터 1회 순회</text>
<text x="550" y="690" class="bd" text-anchor="middle">epoch=3 → 3번 반복</text>
<text x="550" y="750" class="bd" text-anchor="middle">너무 많으면 과적합</text>
<text x="550" y="810" class="bd" text-anchor="middle">너무 적으면 학습 부족</text>
<rect x="1020" y="480" width="700" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="550" class="h2" text-anchor="middle">Step</text>
<text x="1370" y="630" class="bd" text-anchor="middle">1 batch 처리 = 1 step</text>
<text x="1370" y="690" class="bd" text-anchor="middle">10,800개, batch=1</text>
<text x="1370" y="750" class="bd" text-anchor="middle">→ 1 epoch = 10,800 steps</text>
<text x="1370" y="810" class="bd" text-anchor="middle">logging_steps=10 권장</text>
{tip('💡 실습: 3 epochs, ~32,000 steps (10,800 × 3)')}
</svg>'''

def slide_040():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">GPU 메모리 최적화 팁</text>
{box(200, 380, 500, 200, C['p'], 'Batch Size 줄이기', ['1 또는 2로 설정', '메모리 최소화'])}
{box(760, 380, 500, 200, C['m'], 'Gradient Checkpointing', ['activation 재계산', '메모리 ↓ 속도 ↓'])}
{box(1310, 380, 410, 200, C['b'], 'Mixed Precision', ['bf16 사용', '효율 ↑'])}
{box(200, 640, 500, 200, C['y'], 'Max Length 제한', ['2048 이하', '불필요한 padding ↓'])}
{box(760, 640, 500, 200, C['pu'], 'Optimizer 선택', ['AdamW 8-bit', '메모리 절약'])}
{box(1310, 640, 410, 200, C['o'], 'Gradient Accumulation', ['effective batch ↑', '메모리 유지'])}
{tip('💡 실습에서는 이 6가지 기법 모두 사용 → Colab T4 16GB로 학습 가능')}
</svg>'''

def slide_041():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">모델 저장과 로드</text>
<rect x="200" y="340" width="700" height="460" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="410" class="h2" text-anchor="middle">학습 완료 후</text>
<text x="550" y="500" class="bd" text-anchor="middle">model.save_pretrained()</text>
<text x="550" y="560" class="bd" text-anchor="middle">LoRA 어댑터만 저장</text>
<text x="550" y="620" class="bd" text-anchor="middle">adapter_config.json</text>
<text x="550" y="680" class="bd" text-anchor="middle">adapter_model.bin</text>
<text x="550" y="760" class="bd" text-anchor="middle">용량: ~수십 MB</text>
<rect x="1020" y="340" width="700" height="460" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="410" class="h2" text-anchor="middle">로드하여 사용</text>
<text x="1370" y="500" class="bd" text-anchor="middle">베이스 모델 로드</text>
<text x="1370" y="560" class="bd" text-anchor="middle">+ LoRA 어댑터 로드</text>
<text x="1370" y="620" class="bd" text-anchor="middle">PeftModel.from_pretrained()</text>
<text x="1370" y="700" class="bd" text-anchor="middle" fill="#27AE60">즉시 추론 가능</text>
<text x="1370" y="760" class="bd" text-anchor="middle">베이스 + 어댑터 = 완성</text>
{tip('💡 여러 LoRA 어댑터를 만들어 베이스 모델에 필요시 교체 가능 (다목적 활용)')}
</svg>'''

def slide_042():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">Section 3 정리</text>
<rect x="200" y="380" width="1520" height="450" rx="30" fill="{C['b']}" opacity="0.05"/>
<text x="960" y="460" class="h2" text-anchor="middle">핵심 개념</text>
<text x="300" y="540" class="bd">✓ BitsAndBytes로 4-bit 양자화, LoRA Config로 학습 설정</text>
<text x="300" y="610" class="bd">✓ Learning Rate 2e-4, Gradient Accumulation으로 메모리 최적화</text>
<text x="300" y="680" class="bd">✓ Cross-Entropy Loss로 예측과 정답 차이 최소화</text>
<text x="300" y="750" class="bd">✓ Train/Val Loss 곡선으로 과적합 감지</text>
<text x="960" y="870" class="h2" text-anchor="middle" fill="{C['m']}">다음: 학습된 모델을 어떻게 평가할까?</text>
{tip('💡 학습은 끝! 이제 성능을 정량적으로 측정하는 방법을 배웁니다')}
</svg>'''

def slide_043():
    return H + f'''
{dots()}
<text x="960" y="250" class="h1" text-anchor="middle">Section 4: 평가 방법</text>
<text x="960" y="350" class="h2" text-anchor="middle" fill="{C['pu']}">Fine-tuning 성능 측정하기</text>
{box(250, 480, 650, 300, C['p'], 'ROUGE', ['단어 중복 기반', 'Recall 중심', '요약 평가'])}
{box(1020, 480, 650, 300, C['m'], 'Embedding Similarity', ['의미 유사도', 'Cosine similarity', 'BERT/Sentence-BERT'])}
{tip('💡 실습 04번 노트북에서 두 가지 평가 지표 모두 사용')}
</svg>'''

def slide_044():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">ROUGE 지표 이해</text>
<rect x="150" y="330" width="1620" height="100" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="400" class="h2" text-anchor="middle">Recall-Oriented Understudy for Gisting Evaluation</text>
<rect x="200" y="470" width="500" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="450" y="540" class="h2" text-anchor="middle">ROUGE-1</text>
<text x="450" y="620" class="bd" text-anchor="middle">단어(unigram) 중복</text>
<text x="450" y="680" class="bd" text-anchor="middle">개별 단어 매칭</text>
<text x="450" y="740" class="bd" text-anchor="middle">기본 평가</text>
<rect x="760" y="470" width="500" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1010" y="540" class="h2" text-anchor="middle">ROUGE-2</text>
<text x="1010" y="620" class="bd" text-anchor="middle">2-gram 중복</text>
<text x="1010" y="680" class="bd" text-anchor="middle">순서 고려</text>
<text x="1010" y="740" class="bd" text-anchor="middle">유창성 반영</text>
<rect x="1310" y="470" width="410" height="350" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1515" y="540" class="h2" text-anchor="middle">ROUGE-L</text>
<text x="1515" y="620" class="bd" text-anchor="middle">LCS 기반</text>
<text x="1515" y="680" class="bd" text-anchor="middle">문장 구조</text>
<text x="1515" y="740" class="bd" text-anchor="middle">가장 종합적</text>
{tip('💡 ROUGE는 0~1 값, 높을수록 좋음. 요약 태스크에서 표준 지표')}
</svg>'''

def slide_045():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">ROUGE 계산 예시</text>
<rect x="150" y="330" width="1620" height="90" rx="15" fill="{C['pu']}" opacity="0.15"/>
<text x="200" y="385" class="h2">Reference: "QLoRA는 메모리를 절감합니다"</text>
<rect x="200" y="460" width="800" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="600" y="530" class="h2" text-anchor="middle">Generated: "QLoRA는 메모리 절감"</text>
<text x="600" y="620" class="bd" text-anchor="middle">공통 단어: QLoRA, 메모리, 절감</text>
<text x="600" y="680" class="bd" text-anchor="middle">Precision: 3/3 = 1.0</text>
<text x="600" y="740" class="bd" text-anchor="middle">Recall: 3/4 = 0.75</text>
<text x="600" y="800" class="bd" text-anchor="middle" fill="#27AE60">ROUGE-1 F1: 0.857</text>
<rect x="1050" y="460" width="670" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="1385" y="530" class="h2" text-anchor="middle">Generated: "메모리를 줄입니다"</text>
<text x="1385" y="620" class="bd" text-anchor="middle">공통 단어: 메모리</text>
<text x="1385" y="680" class="bd" text-anchor="middle">Precision: 1/2 = 0.5</text>
<text x="1385" y="740" class="bd" text-anchor="middle">Recall: 1/4 = 0.25</text>
<text x="1385" y="800" class="bd" text-anchor="middle" fill="#E74C3C">ROUGE-1 F1: 0.333</text>
{tip('💡 F1 = 2 × (Precision × Recall) / (Precision + Recall)')}
</svg>'''

def slide_046():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Embedding Similarity</text>
<rect x="150" y="330" width="1620" height="110" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="405" class="h2" text-anchor="middle">의미적 유사도 측정 (ROUGE는 단어 매칭만)</text>
<rect x="200" y="480" width="700" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="550" class="h2" text-anchor="middle">과정</text>
<text x="550" y="630" class="bd" text-anchor="middle">1. Sentence 임베딩</text>
<text x="550" y="690" class="bd" text-anchor="middle">2. 벡터로 변환</text>
<text x="550" y="750" class="bd" text-anchor="middle">3. Cosine similarity</text>
<text x="550" y="810" class="bd" text-anchor="middle">4. -1~1 값</text>
<rect x="1020" y="480" width="700" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="550" class="h2" text-anchor="middle">장점</text>
<text x="1370" y="630" class="bd" text-anchor="middle">✓ 의미적 동등성 인식</text>
<text x="1370" y="690" class="bd" text-anchor="middle">✓ 다른 단어, 같은 뜻 OK</text>
<text x="1370" y="750" class="bd" text-anchor="middle">✓ "절감" = "줄임" 인식</text>
<text x="1370" y="810" class="bd" text-anchor="middle" fill="#27AE60">ROUGE 보완</text>
{tip('💡 실습: sentence-transformers 라이브러리 사용 (all-MiniLM-L6-v2 모델)')}
</svg>'''

def slide_047():
    return H + f'''
{dots()}
<text x="960" y="220" class="h1" text-anchor="middle">평가 지표 비교</text>
<rect x="200" y="320" width="520" height="500" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="460" y="390" class="h2" text-anchor="middle">ROUGE</text>
<text x="460" y="480" class="bd" text-anchor="middle">✓ 빠름</text>
<text x="460" y="540" class="bd" text-anchor="middle">✓ 해석 쉬움</text>
<text x="460" y="600" class="bd" text-anchor="middle">✓ 표준 지표</text>
<text x="460" y="680" class="bd" text-anchor="middle">✗ 단어 매칭만</text>
<text x="460" y="740" class="bd" text-anchor="middle">✗ 의미 무시</text>
<rect x="750" y="320" width="520" height="500" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1010" y="390" class="h2" text-anchor="middle">Embedding Similarity</text>
<text x="1010" y="480" class="bd" text-anchor="middle">✓ 의미 반영</text>
<text x="1010" y="540" class="bd" text-anchor="middle">✓ 동의어 인식</text>
<text x="1010" y="600" class="bd" text-anchor="middle">✓ 문맥 고려</text>
<text x="1010" y="680" class="bd" text-anchor="middle">✗ 느림</text>
<text x="1010" y="740" class="bd" text-anchor="middle">✗ 임베딩 모델 필요</text>
<rect x="1300" y="320" width="420" height="500" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1510" y="390" class="h2" text-anchor="middle">권장 조합</text>
<text x="1510" y="480" class="bd" text-anchor="middle">ROUGE-L</text>
<text x="1510" y="540" class="bd" text-anchor="middle">+</text>
<text x="1510" y="600" class="bd" text-anchor="middle">Embedding</text>
<text x="1510" y="680" class="bd" text-anchor="middle">Similarity</text>
<text x="1510" y="760" class="bd" text-anchor="middle" fill="#27AE60">종합 평가</text>
{tip('💡 실습에서는 두 지표 모두 계산하여 다각도로 성능 확인')}
</svg>'''

def slide_048():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">Before/After 비교</text>
<rect x="150" y="330" width="1620" height="100" rx="20" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="400" class="h2" text-anchor="middle">베이스 모델 vs Fine-tuned 모델</text>
<rect x="200" y="470" width="800" height="350" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="600" y="540" class="h2" text-anchor="middle">EXAONE 3.5 Base</text>
<text x="600" y="620" class="bd" text-anchor="middle">ROUGE-L: 0.25</text>
<text x="600" y="680" class="bd" text-anchor="middle">Embedding Sim: 0.65</text>
<text x="600" y="740" class="bd" text-anchor="middle">일반적인 답변</text>
<text x="600" y="800" class="bd" text-anchor="middle">도메인 지식 부족</text>
<rect x="1050" y="470" width="670" height="350" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1385" y="540" class="h2" text-anchor="middle">EXAONE 3.5 + QLoRA</text>
<text x="1385" y="620" class="bd" text-anchor="middle">ROUGE-L: 0.45 (+80%)</text>
<text x="1385" y="680" class="bd" text-anchor="middle">Embedding Sim: 0.82 (+26%)</text>
<text x="1385" y="740" class="bd" text-anchor="middle">정확한 답변</text>
<text x="1385" y="800" class="bd" text-anchor="middle" fill="#27AE60">도메인 특화 성능</text>
{tip('💡 실습 목표: ROUGE-L 15~25% 향상, Embedding Similarity 10~20% 향상')}
</svg>'''

def slide_049():
    return H + f'''
{dots()}
<text x="960" y="240" class="h1" text-anchor="middle">성능 향상 요인 분석</text>
{box(200, 380, 500, 200, C['p'], 'RAFT 데이터', ['Oracle + Distractors', '12,000개 샘플', '품질 높은 레이블'])}
{box(760, 380, 500, 200, C['m'], 'QLoRA 효율성', ['파라미터 0.1%만 학습', '과적합 방지', '일반화 능력↑'])}
{box(1310, 380, 410, 200, C['b'], '하이퍼파라미터', ['r=64', 'lr=2e-4', 'epoch=3'])}
{box(200, 640, 500, 200, C['y'], 'Label 마스킹', ['Answer만 학습', '효율적인 학습', 'Loss 집중'])}
{box(760, 640, 500, 200, C['pu'], '메모리 최적화', ['4-bit 양자화', 'Gradient Accum', 'Batch=1'])}
{box(1310, 640, 410, 200, C['o'], '평가 방법', ['ROUGE', 'Embedding Sim', '다각도 검증'])}
{tip('💡 이 6가지 요소가 결합되어 높은 성능 향상 달성')}
</svg>'''

def slide_050():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">Day 1 전체 정리</text>
<rect x="200" y="380" width="1520" height="530" rx="30" fill="{C['pu']}" opacity="0.05"/>
<text x="960" y="460" class="h2" text-anchor="middle">오늘 배운 내용</text>
<text x="300" y="540" class="bd">1️⃣ LoRA/QLoRA로 메모리를 96% 절감하며 효율적으로 학습</text>
<text x="300" y="610" class="bd">2️⃣ RAFT 데이터로 RAG 시나리오를 모델에 내재화</text>
<text x="300" y="680" class="bd">3️⃣ 학습 과정에서 Loss 곡선으로 과적합 감지</text>
<text x="300" y="750" class="bd">4️⃣ ROUGE와 Embedding Similarity로 성능 정량 평가</text>
<text x="960" y="860" class="h2" text-anchor="middle" fill="{C['b']}">이제 8개 노트북을 직접 실행하며 실습해봅시다!</text>
{tip('🎉 축하합니다! Day 1 Fine-tuning 이론 강의를 완료했습니다!')}
</svg>'''

# ========== GENERATE ALL SLIDES ==========

def generate_all():
    import os
    os.makedirs('svg', exist_ok=True)

    slides = [
        slide_001, slide_002, slide_003, slide_004, slide_005,
        slide_006, slide_007, slide_008, slide_009, slide_010,
        slide_011, slide_012, slide_013, slide_014, slide_015,
        slide_016, slide_017, slide_018, slide_019, slide_020,
        slide_021, slide_022, slide_023, slide_024, slide_025,
        slide_026, slide_027, slide_028, slide_029, slide_030,
        slide_031, slide_032, slide_033, slide_034, slide_035,
        slide_036, slide_037, slide_038, slide_039, slide_040,
        slide_041, slide_042, slide_043, slide_044, slide_045,
        slide_046, slide_047, slide_048, slide_049, slide_050
    ]

    for i, func in enumerate(slides, 1):
        with open(f'svg/slide_{i:03d}.svg', 'w', encoding='utf-8') as f:
            f.write(func())
        print(f'✓ Generated slide_{i:03d}.svg')

    print(f'\n🎉 All 50 slides generated successfully!')

if __name__ == '__main__':
    generate_all()
