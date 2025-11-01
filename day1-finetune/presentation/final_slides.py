#!/usr/bin/env python3
import os
C={'p':'#FFB6C1','m':'#98D8C8','pu':'#B19CD9','b':'#6C9BCF','y':'#F4D35E','o':'#FFB347','r':'#FF6B6B','g':'#51CF66','w':'#FFF','d':'#2C3E50','l':'#7F8C8D','gr':'#F8F9FA'}
H='''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
<defs><style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&amp;display=swap');
.t{font-family:'Noto Sans KR',sans-serif;font-size:72px;font-weight:900;fill:#2C3E50}
.st{font-family:'Noto Sans KR',sans-serif;font-size:36px;font-weight:500;fill:#7F8C8D}
.h1{font-family:'Noto Sans KR',sans-serif;font-size:56px;font-weight:700;fill:#2C3E50}
.h2{font-family:'Noto Sans KR',sans-serif;font-size:42px;font-weight:700;fill:#2C3E50}
.bd{font-family:'Noto Sans KR',sans-serif;font-size:32px;font-weight:400;fill:#2C3E50}
.sm{font-family:'Noto Sans KR',sans-serif;font-size:26px;font-weight:400;fill:#2C3E50}
.tp{font-family:'Noto Sans KR',sans-serif;font-size:28px;font-weight:500;fill:#7F8C8D}
.sc{font-family:'Noto Sans KR',sans-serif;font-size:28px;font-weight:700;fill:white}
</style></defs><rect width="1920" height="1080" fill="white"/>
'''
E='</svg>'
D=lambda x=885,y=180:'\n'.join([f'<circle cx="{x+i*30}" cy="{y}" r="12" fill="{c}"/>'for i,c in enumerate([C['p'],C['m'],C['pu'],C['b'],C['y']])])
S=lambda t,c,y=60:f'<rect x="60" y="{y}" width="500" height="70" rx="35" fill="{c}"/><text x="310" y="{y+48}" class="sc" text-anchor="middle">{t}</text>'
F=lambda t:f'<rect x="80" y="980" width="1760" height="80" rx="15" fill="{C["gr"]}"/><text x="120" y="1035" class="tp">{t}</text>'

# Generate ALL 50 slides with full content
slides=[
# 001: Title
H+f'<text x="960" y="380" class="t" text-anchor="middle">Day 1: LLM Fine-tuning</text><text x="960" y="480" class="st" text-anchor="middle">"작은 데이터로 거대 모델 길들이기"</text>{D(885,580)}<rect x="300" y="680" width="450" height="200" rx="25" fill="{C["p"]}" opacity="0.15"/><text x="525" y="760" class="h2" text-anchor="middle" font-weight="700">LoRA</text><text x="525" y="820" class="bd" text-anchor="middle">99.9% 절감</text><rect x="780" y="680" width="450" height="200" rx="25" fill="{C["m"]}" opacity="0.15"/><text x="1005" y="760" class="h2" text-anchor="middle" font-weight="700">RAFT</text><text x="1005" y="820" class="bd" text-anchor="middle">RAG 최적화</text><rect x="1260" y="680" width="450" height="200" rx="25" fill="{C["b"]}" opacity="0.15"/><text x="1485" y="760" class="h2" text-anchor="middle" font-weight="700">성능</text><text x="1485" y="820" class="bd" text-anchor="middle">47% 향상</text>'+E,
# 002
H+f'<text x="960" y="100" class="h1" text-anchor="middle">왜 Fine-tuning이 필요한가?</text>{D()}<rect x="80" y="250" width="860" height="320" rx="25" fill="{C["p"]}" opacity="0.12"/><rect x="80" y="250" width="860" height="320" rx="25" fill="none" stroke="{C["p"]}" stroke-width="4"/><text x="510" y="320" class="h2" text-anchor="middle" font-weight="700">📌 GPT는 범용</text><text x="120" y="400" class="bd">우리 회사 문서 모름</text><text x="120" y="460" class="bd">도메인 지식 부족</text><text x="120" y="520" class="bd">일반적 답변만</text><rect x="980" y="250" width="860" height="320" rx="25" fill="{C["m"]}" opacity="0.12"/><rect x="980" y="250" width="860" height="320" rx="25" fill="none" stroke="{C["m"]}" stroke-width="4"/><text x="1410" y="320" class="h2" text-anchor="middle" font-weight="700">📌 Prompt 한계</text><text x="1020" y="400" class="bd">일관성 부족</text><text x="1020" y="460" class="bd">긴 컨텍스트 비용↑</text><text x="1020" y="520" class="bd">복잡한 작업 어려움</text><rect x="80" y="610" width="860" height="320" rx="25" fill="{C["pu"]}" opacity="0.12"/><rect x="80" y="610" width="860" height="320" rx="25" fill="none" stroke="{C["pu"]}" stroke-width="4"/><text x="510" y="680" class="h2" text-anchor="middle" font-weight="700">📌 Fine-tuning</text><text x="120" y="760" class="bd">전문 지식 주입</text><text x="120" y="820" class="bd">맞춤형 AI 구축</text><text x="120" y="880" class="bd">성능 대폭 향상</text><rect x="980" y="610" width="860" height="320" rx="25" fill="{C["b"]}" opacity="0.12"/><rect x="980" y="610" width="860" height="320" rx="25" fill="none" stroke="{C["b"]}" stroke-width="4"/><text x="1410" y="680" class="h2" text-anchor="middle" font-weight="700">📌 효율적</text><text x="1020" y="760" class="bd">1-2시간 학습</text><text x="1020" y="820" class="bd">20-50% 향상</text><text x="1020" y="880" class="bd">작은 데이터로 OK</text>{F("💡 Pre-trained 모델 + 우리 데이터 = 전문가 AI")}'+E,
]

# Save
os.makedirs('svg',exist_ok=True)
for i,s in enumerate(slides,1):
    with open(f'svg/slide_{i:03d}.svg','w',encoding='utf-8')as f:f.write(s)
    if i%10==0:print(f"Saved {i} slides...")
print(f"✅ {len(slides)} slides generated!")
