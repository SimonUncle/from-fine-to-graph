#!/usr/bin/env python3
"""
Day 1 Fine-tuning - Pure Theory Slides
No deployment, no hands-on instructions - ONLY theory and concepts
"""

import os

C = {
    'pink': '#FFB6C1',
    'mint': '#98D8C8',
    'purple': '#B19CD9',
    'blue': '#6C9BCF',
    'yellow': '#F4D35E',
    'orange': '#FFB347',
    'red': '#FF6B6B',
    'green': '#51CF66',
    'bg': '#FFFFFF',
    'dark': '#2C3E50',
    'light': '#7F8C8D',
    'gray': '#F8F9FA'
}

def svg_header():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
<defs>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&amp;display=swap');
.title{font-family:'Noto Sans KR',sans-serif;font-size:72px;font-weight:900;fill:#2C3E50}
.subtitle{font-family:'Noto Sans KR',sans-serif;font-size:36px;font-weight:500;fill:#7F8C8D}
.section-label{font-family:'Noto Sans KR',sans-serif;font-size:28px;font-weight:700;fill:white}
.h1{font-family:'Noto Sans KR',sans-serif;font-size:56px;font-weight:700;fill:#2C3E50}
.h2{font-family:'Noto Sans KR',sans-serif;font-size:42px;font-weight:700;fill:#2C3E50}
.body{font-family:'Noto Sans KR',sans-serif;font-size:32px;font-weight:400;fill:#2C3E50}
.small{font-family:'Noto Sans KR',sans-serif;font-size:26px;font-weight:400;fill:#2C3E50}
.tiny{font-family:'Noto Sans KR',sans-serif;font-size:22px;font-weight:400;fill:#2C3E50}
.bold{font-weight:700}
.tip{font-family:'Noto Sans KR',sans-serif;font-size:28px;font-weight:500;fill:#7F8C8D}
</style>
</defs>
<rect width="1920" height="1080" fill="white"/>
'''

def svg_footer():
    return '</svg>'

def dots(x=885, y=180):
    colors = [C['pink'], C['mint'], C['purple'], C['blue'], C['yellow']]
    return '\n'.join([f'<circle cx="{x + i*30}" cy="{y}" r="12" fill="{c}"/>' for i, c in enumerate(colors)])

def section_label(text, color, y=60):
    return f'<rect x="60" y="{y}" width="500" height="70" rx="35" fill="{color}"/>\n<text x="310" y="{y+48}" class="section-label" text-anchor="middle">{text}</text>'

def footer(text):
    return f'<rect x="80" y="980" width="1760" height="80" rx="15" fill="{C["gray"]}"/>\n<text x="120" y="1035" class="tip">{text}</text>'

def box(x, y, w, h, color, title, lines, title_size='h2'):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="25" fill="{color}" opacity="0.12"/>\n'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="25" fill="none" stroke="{color}" stroke-width="4"/>\n'
    s += f'<text x="{x+40}" y="{y+70}" class="{title_size} bold">{title}</text>\n'
    ly = y + 140
    for line in lines:
        if line.startswith('•'):
            s += f'<text x="{x+60}" y="{ly}" class="body">{line}</text>\n'
        elif line.startswith('  '):
            s += f'<text x="{x+80}" y="{ly}" class="small">{line.strip()}</text>\n'
        elif line == '':
            ly += 20
            continue
        else:
            s += f'<text x="{x+40}" y="{ly}" class="body">{line}</text>\n'
        ly += 50
    return s

# Generate all slides
slides = []

# =============================================================================
# SECTION 0: INTRO (001-003)
# =============================================================================

# 001: Title
slides.append(f'''{svg_header()}
<text x="960" y="380" class="title" text-anchor="middle">Day 1: LLM Fine-tuning</text>
<text x="960" y="480" class="subtitle" text-anchor="middle">"작은 데이터로 거대 모델 길들이기"</text>
{dots(885, 580)}
<rect x="300" y="680" width="450" height="200" rx="25" fill="{C['pink']}" opacity="0.15"/>
<text x="525" y="760" class="h2 bold" text-anchor="middle">LoRA</text>
<text x="525" y="820" class="body" text-anchor="middle">99.9% 절감</text>
<rect x="780" y="680" width="450" height="200" rx="25" fill="{C['mint']}" opacity="0.15"/>
<text x="1005" y="760" class="h2 bold" text-anchor="middle">RAFT</text>
<text x="1005" y="820" class="body" text-anchor="middle">RAG 최적화</text>
<rect x="1260" y="680" width="450" height="200" rx="25" fill="{C['blue']}" opacity="0.15"/>
<text x="1485" y="760" class="h2 bold" text-anchor="middle">성능</text>
<text x="1485" y="820" class="body" text-anchor="middle">47% 향상</text>
{svg_footer()}''')

# 002: Why fine-tuning?
slides.append(f'''{svg_header()}
<text x="960" y="100" class="h1" text-anchor="middle">왜 Fine-tuning이 필요한가?</text>
{dots()}
{box(80, 250, 860, 320, C['pink'], '📌 GPT는 범용 모델', ['우리 회사 문서를 모름', '도메인 전문 지식 부족', '일반적 답변만 가능'])}
{box(980, 250, 860, 320, C['mint'], '📌 Prompt의 한계', ['일관성 부족', '긴 컨텍스트는 비용↑', '복잡한 작업은 어려움'])}
{box(80, 610, 860, 320, C['purple'], '📌 Fine-tuning 해결책', ['모델에 전문 지식 주입', '맞춤형 AI 구축', '성능 대폭 향상'])}
{box(980, 610, 860, 320, C['blue'], '📌 효율적 비용', ['1-2시간 학습', '성능 20-50% 향상', '작은 데이터로 가능'])}
{footer('💡 Pre-trained 모델 + 우리 데이터 = 전문가 AI')}
{svg_footer()}''')

# 003: Today's journey
slides.append(f'''{svg_header()}
<text x="960" y="100" class="h1" text-anchor="middle">오늘 배울 핵심 개념</text>
{dots()}
<rect x="600" y="220" width="720" height="720" rx="35" fill="{C['gray']}"/>
<text x="960" y="300" class="h2 bold" text-anchor="middle" fill="{C['pink']}">1. Fine-tuning 방법론</text>
<text x="960" y="360" class="body" text-anchor="middle">Full FT vs LoRA vs QLoRA</text>
<line x1="700" y1="390" x2="1220" y2="390" stroke="{C['light']}" stroke-width="2"/>
<text x="960" y="460" class="h2 bold" text-anchor="middle" fill="{C['mint']}">2. RAFT 데이터 형식</text>
<text x="960" y="520" class="body" text-anchor="middle">RAG에 최적화된 학습</text>
<line x1="700" y1="550" x2="1220" y2="550" stroke="{C['light']}" stroke-width="2"/>
<text x="960" y="620" class="h2 bold" text-anchor="middle" fill="{C['purple']}">3. 학습 원리</text>
<text x="960" y="680" class="body" text-anchor="middle">Loss, Hyperparameter</text>
<line x1="700" y1="710" x2="1220" y2="710" stroke="{C['light']}" stroke-width="2"/>
<text x="960" y="780" class="h2 bold" text-anchor="middle" fill="{C['blue']}">4. 평가 방법</text>
<text x="960" y="840" class="body" text-anchor="middle">ROUGE, Embedding Similarity</text>
{footer('💡 이론 이해 → 노트북 실습으로 이어집니다')}
{svg_footer()}''')

# =============================================================================
# SECTION 1: BASICS (004-015) - 12 slides
# =============================================================================

# 004: Section 1 header + Full FT problem
slides.append(f'''{svg_header()}
{section_label('Section 1: Fine-tuning 기초', C['pink'])}
<text x="960" y="200" class="h1" text-anchor="middle">전통적 Fine-tuning의 문제</text>
{dots(885, 280)}
<rect x="100" y="380" width="800" height="540" rx="25" fill="{C['pink']}" opacity="0.1"/>
<text x="500" y="460" class="h2 bold" text-anchor="middle">Full Fine-tuning</text>
<text x="500" y="550" class="body" text-anchor="middle">24억 개 파라미터</text>
<text x="500" y="610" class="body" text-anchor="middle">전부 다 업데이트</text>
<line x1="200" y1="650" x2="800" y2="650" stroke="{C['pink']}" stroke-width="2"/>
<text x="500" y="720" class="body" text-anchor="middle" fill="{C['red']}">GPU: 48GB 필요</text>
<text x="500" y="780" class="body" text-anchor="middle" fill="{C['red']}">시간: 24시간</text>
<text x="500" y="840" class="body" text-anchor="middle" fill="{C['red']}">비용: $$$$$</text>
<rect x="1020" y="380" width="800" height="540" rx="25" fill="{C['red']}" opacity="0.1"/>
<text x="1420" y="460" class="h2 bold" text-anchor="middle">4가지 문제점</text>
<text x="1420" y="570" class="body" text-anchor="middle">❌ 너무 느림 (24h)</text>
<text x="1420" y="660" class="body" text-anchor="middle">❌ GPU 비쌈 (A100)</text>
<text x="1420" y="750" class="body" text-anchor="middle">❌ Overfitting 위험</text>
<text x="1420" y="840" class="body" text-anchor="middle">❌ 배포 파일 24GB</text>
{footer('💡 개인이나 작은 팀이 사용하기엔 비현실적')}
{svg_footer()}''')

# 005: PEFT concept
slides.append(f'''{svg_header()}
<text x="960" y="80" class="h1" text-anchor="middle">PEFT 등장 배경</text>
<text x="960" y="150" class="subtitle" text-anchor="middle">Parameter-Efficient Fine-Tuning</text>
{dots(885, 210)}
<rect x="200" y="290" width="1520" height="380" rx="25" fill="{C['gray']}"/>
<text x="300" y="360" class="h2 bold">비교표</text>
<line x1="250" y1="390" x2="1670" y2="390" stroke="{C['dark']}" stroke-width="3"/>
<text x="350" y="450" class="body bold">방법</text>
<text x="700" y="450" class="body bold">파라미터 수정</text>
<text x="1050" y="450" class="body bold">메모리</text>
<text x="1400" y="450" class="body bold">학습 시간</text>
<line x1="250" y1="475" x2="1670" y2="475" stroke="{C['light']}" stroke-width="2"/>
<text x="350" y="540" class="body">Full FT</text>
<text x="700" y="540" class="body">100% (24억 개)</text>
<text x="1050" y="540" class="body">48GB</text>
<text x="1400" y="540" class="body">24시간</text>
<line x1="250" y1="565" x2="1670" y2="565" stroke="{C['light']}" stroke-width="1"/>
<text x="350" y="630" class="body bold" fill="{C['mint']}">PEFT (LoRA)</text>
<text x="700" y="630" class="body bold" fill="{C['mint']}">0.1% (260만 개)</text>
<text x="1050" y="630" class="body bold" fill="{C['mint']}">8GB</text>
<text x="1400" y="630" class="body bold" fill="{C['mint']}">2시간</text>
<rect x="300" y="720" width="1320" height="130" rx="20" fill="{C['mint']}" opacity="0.2"/>
<text x="960" y="805" class="h2 bold" text-anchor="middle">"모든 파라미터를 바꾸지 말고, 작은 어댑터만 추가하자!"</text>
{footer('💡 핵심 아이디어: 원본 모델은 그대로, 작은 부분만 학습')}
{svg_footer()}''')

# 006: LoRA core principle
slides.append(f'''{svg_header()}
<text x="960" y="90" class="h1" text-anchor="middle">LoRA 핵심 원리</text>
<text x="960" y="160" class="subtitle" text-anchor="middle">Low-Rank Adaptation</text>
{dots(885, 220)}
<rect x="100" y="310" width="850" height="600" rx="25" fill="{C['purple']}" opacity="0.12"/>
<text x="525" y="390" class="h2 bold" text-anchor="middle">수학적 원리</text>
<text x="525" y="480" class="body" text-anchor="middle">원본 가중치 W (4096 × 4096)</text>
<text x="525" y="550" class="body" text-anchor="middle" fill="{C['purple']}">↓ 고정 (freeze)</text>
<text x="525" y="640" class="body" text-anchor="middle">두 개의 작은 행렬 추가:</text>
<text x="525" y="710" class="body bold" text-anchor="middle" fill="{C['mint']}">B (4096 × 8)</text>
<text x="525" y="780" class="body bold" text-anchor="middle" fill="{C['mint']}">A (8 × 4096)</text>
<text x="525" y="860" class="h2 bold" text-anchor="middle" fill="{C['blue']}">W_new = W + B×A</text>
<rect x="980" y="310" width="860" height="600" rx="25" fill="{C['purple']}" opacity="0.12"/>
<text x="1410" y="390" class="h2 bold" text-anchor="middle">파라미터 계산</text>
<text x="1410" y="500" class="body" text-anchor="middle">원본 W:</text>
<text x="1410" y="560" class="small" text-anchor="middle">4096 × 4096 = 16,777,216</text>
<text x="1410" y="650" class="body" text-anchor="middle" fill="{C['mint']}">LoRA (B + A):</text>
<text x="1410" y="710" class="small" text-anchor="middle" fill="{C['mint']}">(4096×8) + (8×4096)</text>
<text x="1410" y="770" class="small" text-anchor="middle" fill="{C['mint']}">= 65,536</text>
<text x="1410" y="860" class="h2 bold" text-anchor="middle" fill="{C['blue']}">절감: 99.6%!</text>
{footer('💡 r=8이 핵심: rank가 작을수록 효율적, 클수록 표현력↑')}
{svg_footer()}''')

# 007: LoRA visualization
slides.append(f'''{svg_header()}
<text x="960" y="90" class="h1" text-anchor="middle">LoRA 시각적 이해</text>
{dots()}
<rect x="150" y="250" width="750" height="650" rx="25" fill="{C['pink']}" opacity="0.12"/>
<text x="525" y="330" class="h2 bold" text-anchor="middle">전통적 방식</text>
<rect x="250" y="400" width="550" height="400" rx="15" fill="{C['red']}" opacity="0.3"/>
<text x="525" y="480" class="body bold" text-anchor="middle">거대한 행렬 W</text>
<text x="525" y="540" class="small" text-anchor="middle">(4096 × 4096)</text>
<text x="525" y="620" class="body" text-anchor="middle">↓</text>
<text x="525" y="690" class="body" text-anchor="middle">전부 수정 ❌</text>
<text x="525" y="760" class="small" text-anchor="middle">16M 파라미터 업데이트</text>
<rect x="1020" y="250" width="750" height="650" rx="25" fill="{C['mint']}" opacity="0.12"/>
<text x="1395" y="330" class="h2 bold" text-anchor="middle">LoRA 방식</text>
<rect x="1120" y="400" width="200" height="180" rx="15" fill="{C['blue']}" opacity="0.3"/>
<text x="1220" y="500" class="body bold" text-anchor="middle">W</text>
<text x="1220" y="550" class="small" text-anchor="middle">고정</text>
<text x="1340" y="490" class="body" text-anchor="middle">+</text>
<rect x="1380" y="400" width="140" height="60" rx="10" fill="{C['mint']}" opacity="0.5"/>
<text x="1450" y="445" class="small bold" text-anchor="middle">B</text>
<text x="1340" y="520" class="body" text-anchor="middle">×</text>
<rect x="1380" y="520" width="140" height="60" rx="10" fill="{C['mint']}" opacity="0.5"/>
<text x="1450" y="565" class="small bold" text-anchor="middle">A</text>
<text x="1395" y="660" class="body" text-anchor="middle">↓</text>
<text x="1395" y="730" class="body" text-anchor="middle" fill="{C['mint']}">작은 행렬만 학습 ✅</text>
<text x="1395" y="800" class="small" text-anchor="middle" fill="{C['mint']}">65K 파라미터만!</text>
{footer('💡 원본 모델 W는 동결, B와 A만 학습 → 효율적!')}
{svg_footer()}''')

# 008: r, alpha, dropout
slides.append(f'''{svg_header()}
<text x="960" y="90" class="h1" text-anchor="middle">LoRA 하이퍼파라미터</text>
{dots()}
{box(80, 230, 570, 680, C['blue'], 'r (rank)', ['• 행렬의 차원', '• 낮을수록:', '  빠르고 메모리 적음', '  하지만 표현력↓', '• 높을수록:', '  느리고 메모리 많음', '  하지만 표현력↑', '', '• 일반적 권장:', '  r = 8 ~ 16', '', '• 실습에서:', '  r = 8 사용'])}
{box(680, 230, 570, 680, C['mint'], 'alpha', ['• LoRA 영향력 조절', '• 공식:', '  scaling = alpha / r', '', '• alpha가 클수록:', '  LoRA 영향↑', '', '• 일반적 규칙:', '  alpha = r × 2', '', '• 예시:', '  r=8 → alpha=16', '  r=16 → alpha=32'])}
{box(1280, 230, 560, 680, C['yellow'], 'dropout', ['• Overfitting 방지', '• 0.05 = 5% 끔', '', '• 데이터 적으면:', '  dropout 높게', '  (0.1 ~ 0.2)', '', '• 데이터 많으면:', '  dropout 낮게', '  (0.05)', '', '• 실습:', '  0.05 사용'])}
{footer('💡 실습 설정: r=8, alpha=16, dropout=0.05')}
{svg_footer()}''')

# 009: QLoRA concept
slides.append(f'''{svg_header()}
<text x="960" y="90" class="h1" text-anchor="middle">QLoRA: 메모리를 더 줄이자</text>
<text x="960" y="160" class="subtitle" text-anchor="middle">Quantization + LoRA</text>
{dots(885, 220)}
<rect x="100" y="310" width="850" height="580" rx="25" fill="{C['orange']}" opacity="0.12"/>
<text x="525" y="390" class="h2 bold" text-anchor="middle">Quantization이란?</text>
<text x="525" y="490" class="body" text-anchor="middle">32-bit Float → 4-bit Integer</text>
<rect x="250" y="540" width="550" height="120" rx="15" fill="{C['gray']}"/>
<text x="525" y="590" class="body" text-anchor="middle">3.14159265... (32비트)</text>
<text x="525" y="640" class="body" text-anchor="middle">↓</text>
<text x="525" y="710" class="h2 bold" text-anchor="middle" fill="{C['orange']}">3 (4비트)</text>
<text x="525" y="800" class="body" text-anchor="middle">정밀도 ↓ / 메모리 ↓↓↓</text>
<rect x="980" y="310" width="860" height="580" rx="25" fill="{C['orange']}" opacity="0.12"/>
<text x="1410" y="390" class="h2 bold" text-anchor="middle">효과 비교</text>
<text x="1410" y="500" class="body" text-anchor="middle">LoRA (FP16):</text>
<text x="1410" y="560" class="small" text-anchor="middle">메모리 8GB / 정확도 100%</text>
<line x1="1100" y1="600" x2="1720" y2="600" stroke="{C['light']}" stroke-width="2"/>
<text x="1410" y="670" class="body bold" text-anchor="middle" fill="{C['orange']}">QLoRA (4-bit):</text>
<text x="1410" y="730" class="small bold" text-anchor="middle" fill="{C['orange']}">메모리 4GB / 정확도 98%</text>
<text x="1410" y="830" class="h2 bold" text-anchor="middle" fill="{C['blue']}">T4 GPU로 가능!</text>
{footer('💡 약간의 정확도 희생으로 메모리 절반! Google Colab 무료 GPU 사용 가능')}
{svg_footer()}''')

# 010: Full FT vs LoRA vs QLoRA
slides.append(f'''{svg_header()}
<text x="960" y="80" class="h1" text-anchor="middle">3가지 방법 완전 비교</text>
{dots()}
<rect x="150" y="200" width="1620" height="680" rx="25" fill="{C['gray']}"/>
<text x="250" y="270" class="body bold">항목</text>
<text x="640" y="270" class="body bold">Full FT</text>
<text x="1050" y="270" class="body bold">LoRA</text>
<text x="1460" y="270" class="body bold">QLoRA</text>
<line x1="200" y1="290" x2="1720" y2="290" stroke="{C['dark']}" stroke-width="3"/>
<text x="250" y="360" class="body">파라미터 수정</text>
<text x="640" y="360" class="body">100%</text>
<text x="1050" y="360" class="body" fill="{C['mint']}">0.1%</text>
<text x="1460" y="360" class="body" fill="{C['mint']}">0.1%</text>
<line x1="200" y1="380" x2="1720" y2="380" stroke="{C['light']}" stroke-width="1"/>
<text x="250" y="450" class="body">메모리 (GB)</text>
<text x="640" y="450" class="body">48</text>
<text x="1050" y="450" class="body" fill="{C['mint']}">8</text>
<text x="1460" y="450" class="body" fill="{C['orange']}">4</text>
<line x1="200" y1="470" x2="1720" y2="470" stroke="{C['light']}" stroke-width="1"/>
<text x="250" y="540" class="body">학습 시간</text>
<text x="640" y="540" class="body">24h</text>
<text x="1050" y="540" class="body" fill="{C['mint']}">2h</text>
<text x="1460" y="540" class="body" fill="{C['orange']}">3h</text>
<line x1="200" y1="560" x2="1720" y2="560" stroke="{C['light']}" stroke-width="1"/>
<text x="250" y="630" class="body">정확도</text>
<text x="640" y="630" class="body">100%</text>
<text x="1050" y="630" class="body" fill="{C['mint']}">95%</text>
<text x="1460" y="630" class="body" fill="{C['orange']}">93%</text>
<line x1="200" y1="650" x2="1720" y2="650" stroke="{C['light']}" stroke-width="1"/>
<text x="250" y="720" class="body">배포 파일 크기</text>
<text x="640" y="720" class="body">24GB</text>
<text x="1050" y="720" class="body" fill="{C['mint']}">32MB</text>
<text x="1460" y="720" class="body" fill="{C['orange']}">32MB</text>
<line x1="200" y1="740" x2="1720" y2="740" stroke="{C['light']}" stroke-width="1"/>
<text x="250" y="810" class="body">필요 GPU</text>
<text x="640" y="810" class="body">A100</text>
<text x="1050" y="810" class="body" fill="{C['mint']}">T4</text>
<text x="1460" y="810" class="body" fill="{C['orange']}">T4</text>
{footer('💡 결론: QLoRA는 성능 90%대 유지하며 비용 1/10 절감!')}
{svg_footer()}''')

# Continue generating remaining slides...
# I'll create a comprehensive set covering all theory topics

print("Generating first 10 slides...")
for i, slide in enumerate(slides[:10], 1):
    os.makedirs('svg', exist_ok=True)
    with open(f'svg/slide_{i:03d}.svg', 'w', encoding='utf-8') as f:
        f.write(slide)

print(f"Generated {len(slides)} slides so far. Continuing...")
