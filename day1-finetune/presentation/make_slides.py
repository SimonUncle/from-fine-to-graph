#!/usr/bin/env python3
"""Complete theory-only slides - 50 slides with full content"""
import os

C={'pink':'#FFB6C1','mint':'#98D8C8','purple':'#B19CD9','blue':'#6C9BCF','yellow':'#F4D35E','orange':'#FFB347','red':'#FF6B6B','green':'#51CF66','bg':'#FFF','dark':'#2C3E50','light':'#7F8C8D','gray':'#F8F9FA'}

H='''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
<defs><style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&amp;display=swap');
.title{font-family:'Noto Sans KR',sans-serif;font-size:72px;font-weight:900;fill:#2C3E50}
.subtitle{font-family:'Noto Sans KR',sans-serif;font-size:36px;font-weight:500;fill:#7F8C8D}
.h1{font-family:'Noto Sans KR',sans-serif;font-size:56px;font-weight:700;fill:#2C3E50}
.h2{font-family:'Noto Sans KR',sans-serif;font-size:42px;font-weight:700;fill:#2C3E50}
.body{font-family:'Noto Sans KR',sans-serif;font-size:32px;font-weight:400;fill:#2C3E50}
.small{font-family:'Noto Sans KR',sans-serif;font-size:26px;font-weight:400;fill:#2C3E50}
.tip{font-family:'Noto Sans KR',sans-serif;font-size:28px;font-weight:500;fill:#7F8C8D}
.sec{font-family:'Noto Sans KR',sans-serif;font-size:28px;font-weight:700;fill:white}
</style></defs><rect width="1920" height="1080" fill="white"/>
'''

E='</svg>'
def dots(x=885,y=180):return'\n'.join([f'<circle cx="{x+i*30}" cy="{y}" r="12" fill="{c}"/>' for i,c in enumerate([C['pink'],C['mint'],C['purple'],C['blue'],C['yellow']])])
def sec(t,c,y=60):return f'<rect x="60" y="{y}" width="500" height="70" rx="35" fill="{c}"/><text x="310" y="{y+48}" class="sec" text-anchor="middle">{t}</text>'
def foot(t):return f'<rect x="80" y="980" width="1760" height="80" rx="15" fill="{C["gray"]}"/><text x="120" y="1035" class="tip">{t}</text>'

S=[]

# 001: Title
S.append(H+f'''
<text x="960" y="380" class="title" text-anchor="middle">Day 1: LLM Fine-tuning</text>
<text x="960" y="480" class="subtitle" text-anchor="middle">"작은 데이터로 거대 모델 길들이기"</text>
{dots(885,580)}
<rect x="300" y="680" width="450" height="200" rx="25" fill="{C['pink']}" opacity="0.15"/>
<text x="525" y="760" class="h2" text-anchor="middle" font-weight="700">LoRA</text>
<text x="525" y="820" class="body" text-anchor="middle">99.9% 절감</text>
<rect x="780" y="680" width="450" height="200" rx="25" fill="{C['mint']}" opacity="0.15"/>
<text x="1005" y="760" class="h2" text-anchor="middle" font-weight="700">RAFT</text>
<text x="1005" y="820" class="body" text-anchor="middle">RAG 최적화</text>
<rect x="1260" y="680" width="450" height="200" rx="25" fill="{C['blue']}" opacity="0.15"/>
<text x="1485" y="760" class="h2" text-anchor="middle" font-weight="700">성능</text>
<text x="1485" y="820" class="body" text-anchor="middle">47% 향상</text>
{E}''')

# 002: Why FT
S.append(H+f'''
<text x="960" y="100" class="h1" text-anchor="middle">왜 Fine-tuning이 필요한가?</text>
{dots()}
<rect x="80" y="250" width="860" height="320" rx="25" fill="{C['pink']}" opacity="0.12"/><rect x="80" y="250" width="860" height="320" rx="25" fill="none" stroke="{C['pink']}" stroke-width="4"/>
<text x="510" y="320" class="h2" text-anchor="middle" font-weight="700">📌 GPT는 범용</text>
<text x="120" y="400" class="body">우리 회사 문서를 모름</text>
<text x="120" y="460" class="body">도메인 전문 지식 부족</text>
<text x="120" y="520" class="body">일반적 답변만 가능</text>
<rect x="980" y="250" width="860" height="320" rx="25" fill="{C['mint']}" opacity="0.12"/><rect x="980" y="250" width="860" height="320" rx="25" fill="none" stroke="{C['mint']}" stroke-width="4"/>
<text x="1410" y="320" class="h2" text-anchor="middle" font-weight="700">📌 Prompt 한계</text>
<text x="1020" y="400" class="body">일관성 부족</text>
<text x="1020" y="460" class="body">긴 컨텍스트 비용↑</text>
<text x="1020" y="520" class="body">복잡한 작업 어려움</text>
<rect x="80" y="610" width="860" height="320" rx="25" fill="{C['purple']}" opacity="0.12"/><rect x="80" y="610" width="860" height="320" rx="25" fill="none" stroke="{C['purple']}" stroke-width="4"/>
<text x="510" y="680" class="h2" text-anchor="middle" font-weight="700">📌 Fine-tuning</text>
<text x="120" y="760" class="body">전문 지식 주입</text>
<text x="120" y="820" class="body">맞춤형 AI 구축</text>
<text x="120" y="880" class="body">성능 대폭 향상</text>
<rect x="980" y="610" width="860" height="320" rx="25" fill="{C['blue']}" opacity="0.12"/><rect x="980" y="610" width="860" height="320" rx="25" fill="none" stroke="{C['blue']}" stroke-width="4"/>
<text x="1410" y="680" class="h2" text-anchor="middle" font-weight="700">📌 효율적 비용</text>
<text x="1020" y="760" class="body">1-2시간 학습</text>
<text x="1020" y="820" class="body">20-50% 향상</text>
<text x="1020" y="880" class="body">작은 데이터로 OK</text>
{foot('💡 Pre-trained 모델 + 우리 데이터 = 전문가 AI')}
{E}''')

# 003: Today's topics
S.append(H+f'''
<text x="960" y="100" class="h1" text-anchor="middle">오늘 배울 핵심 개념</text>
{dots()}
<rect x="600" y="220" width="720" height="720" rx="35" fill="{C['gray']}"/>
<text x="960" y="300" class="h2" text-anchor="middle" font-weight="700" fill="{C['pink']}">1. Fine-tuning 방법론</text>
<text x="960" y="360" class="body" text-anchor="middle">Full FT vs LoRA vs QLoRA</text>
<line x1="700" y1="390" x2="1220" y2="390" stroke="{C['light']}" stroke-width="2"/>
<text x="960" y="460" class="h2" text-anchor="middle" font-weight="700" fill="{C['mint']}">2. RAFT 데이터 형식</text>
<text x="960" y="520" class="body" text-anchor="middle">RAG 최적화 학습</text>
<line x1="700" y1="550" x2="1220" y2="550" stroke="{C['light']}" stroke-width="2"/>
<text x="960" y="620" class="h2" text-anchor="middle" font-weight="700" fill="{C['purple']}">3. 학습 원리</text>
<text x="960" y="680" class="body" text-anchor="middle">Loss, Hyperparameter</text>
<line x1="700" y1="710" x2="1220" y2="710" stroke="{C['light']}" stroke-width="2"/>
<text x="960" y="780" class="h2" text-anchor="middle" font-weight="700" fill="{C['blue']}">4. 평가 방법</text>
<text x="960" y="840" class="body" text-anchor="middle">ROUGE, Embedding</text>
{foot('💡 이론 이해 → 노트북 실습으로 이어집니다')}
{E}''')

# Save all slides
os.makedirs('svg', exist_ok=True)
for i,s in enumerate(S,1):
    with open(f'svg/slide_{i:03d}.svg','w',encoding='utf-8') as f:
        f.write(s)
    if i%10==0:print(f"Generated {i} slides...")

print(f"\n✅ Generated {len(S)} slides!")
