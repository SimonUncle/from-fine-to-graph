#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 1 Fine-tuning Presentation - Theory-Focused Version
초보자 중심, 이론 개념, 비유와 스토리텔링
"""

# Color palette
C = {'p':'#FFB6C1','m':'#98D8C8','pu':'#B19CD9','b':'#6C9BCF','y':'#F4D35E','o':'#FFB347'}

# SVG Header
H = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
<defs><style>
.t{font-family:Arial,sans-serif;font-size:72px;font-weight:900;fill:#2C3E50}
.st{font-family:Arial,sans-serif;font-size:36px;font-weight:500;fill:#7F8C8D}
.h1{font-family:Arial,sans-serif;font-size:56px;font-weight:700;fill:#2C3E50}
.h2{font-family:Arial,sans-serif;font-size:42px;font-weight:700;fill:#2C3E50}
.bd{font-family:Arial,sans-serif;font-size:32px;font-weight:400;fill:#2C3E50}
.sm{font-family:Arial,sans-serif;font-size:28px;font-weight:400;fill:#2C3E50}
.tp{font-family:Arial,sans-serif;font-size:28px;font-weight:500;fill:#7F8C8D}
</style></defs>
<rect width="1920" height="1080" fill="white"/>'''

def dots(x=885, y=180):
    return f'<circle cx="{x}" cy="{y}" r="12" fill="{C["p"]}"/><circle cx="{x+30}" cy="{y}" r="12" fill="{C["m"]}"/><circle cx="{x+60}" cy="{y}" r="12" fill="{C["pu"]}"/><circle cx="{x+90}" cy="{y}" r="12" fill="{C["b"]}"/><circle cx="{x+120}" cy="{y}" r="12" fill="{C["y"]}"/>'

def box(x, y, w, h, color, title, lines):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="25" fill="{color}" opacity="0.15"/>'
    s += f'<text x="{x+w//2}" y="{y+60}" class="h2" text-anchor="middle" font-weight="700">{title}</text>'
    for i, line in enumerate(lines):
        s += f'<text x="{x+w//2}" y="{y+130+i*55}" class="bd" text-anchor="middle">{line}</text>'
    return s

def tip(text):
    return f'<rect x="80" y="980" width="1760" height="80" rx="15" fill="#F8F9FA"/><text x="120" y="1035" class="tp">{text}</text>'

# ========== SECTION 0: 프롤로그 (001-003) ==========

def slide_001():
    return H + f'''
{dots()}
<text x="960" y="380" class="t" text-anchor="middle">Day 1: Fine-tuning</text>
<text x="960" y="480" class="st" text-anchor="middle">거대 AI를 내 손안으로</text>
<rect x="350" y="620" width="400" height="180" rx="25" fill="{C['p']}" opacity="0.2"/>
<text x="550" y="690" class="h2" text-anchor="middle">📚 LoRA</text>
<text x="550" y="750" class="bd" text-anchor="middle">변화량 기록</text>
<rect x="800" y="620" width="400" height="180" rx="25" fill="{C['m']}" opacity="0.2"/>
<text x="1000" y="690" class="h2" text-anchor="middle">🗜️ QLoRA</text>
<text x="1000" y="750" class="bd" text-anchor="middle">모델 압축</text>
<rect x="1250" y="620" width="320" height="180" rx="25" fill="{C['b']}" opacity="0.2"/>
<text x="1410" y="690" class="h2" text-anchor="middle">🎯 RAFT</text>
<text x="1410" y="750" class="bd" text-anchor="middle">현실 학습</text>
{tip('💡 오늘은 작은 GPU로도 거대 모델을 학습하는 이론을 배웁니다')}
</svg>'''

def slide_002():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">오늘의 여정</text>
<rect x="200" y="360" width="340" height="500" rx="30" fill="{C['p']}" opacity="0.1"/>
<text x="370" y="430" class="h2" text-anchor="middle">1. 문제 발견</text>
<text x="370" y="510" class="bd" text-anchor="middle">Fine-tuning은</text>
<text x="370" y="570" class="bd" text-anchor="middle">왜 어려운가?</text>
<text x="370" y="650" class="sm" text-anchor="middle">메모리 부족</text>
<text x="370" y="700" class="sm" text-anchor="middle">시간 오래 걸림</text>
<text x="370" y="750" class="sm" text-anchor="middle">비용 많이 듦</text>
<rect x="590" y="360" width="340" height="500" rx="30" fill="{C['m']}" opacity="0.1"/>
<text x="760" y="430" class="h2" text-anchor="middle">2. 해법 1</text>
<text x="760" y="510" class="bd" text-anchor="middle">LoRA</text>
<text x="760" y="590" class="sm" text-anchor="middle">변화량만 학습</text>
<text x="760" y="680" class="bd" text-anchor="middle">QLoRA</text>
<text x="760" y="760" class="sm" text-anchor="middle">모델 압축</text>
<rect x="980" y="360" width="340" height="500" rx="30" fill="{C['b']}" opacity="0.1"/>
<text x="1150" y="430" class="h2" text-anchor="middle">3. 해법 2</text>
<text x="1150" y="510" class="bd" text-anchor="middle">RAFT 데이터</text>
<text x="1150" y="590" class="sm" text-anchor="middle">현실적인</text>
<text x="1150" y="640" class="sm" text-anchor="middle">학습 방식</text>
<rect x="1370" y="360" width="340" height="500" rx="30" fill="{C['y']}" opacity="0.1"/>
<text x="1540" y="430" class="h2" text-anchor="middle">4. 실전</text>
<text x="1540" y="510" class="bd" text-anchor="middle">학습 과정</text>
<text x="1540" y="570" class="sm" text-anchor="middle">Loss 이해</text>
<text x="1540" y="650" class="bd" text-anchor="middle">평가 방법</text>
<text x="1540" y="710" class="sm" text-anchor="middle">ROUGE</text>
<text x="1540" y="760" class="sm" text-anchor="middle">Embedding</text>
{tip('💡 문제 인식 → 해법 탐색 → 실전 적용 순서로 진행됩니다')}
</svg>'''

def slide_003():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">학습 방법</text>
<rect x="200" y="380" width="750" height="420" rx="30" fill="{C['p']}" opacity="0.1"/>
<text x="575" y="460" class="h2" text-anchor="middle">💬 이 강의 (이론)</text>
<text x="575" y="560" class="bd" text-anchor="middle">왜 이 기술이 필요한가?</text>
<text x="575" y="620" class="bd" text-anchor="middle">어떤 원리로 작동하는가?</text>
<text x="575" y="680" class="bd" text-anchor="middle">다른 방법과 무엇이 다른가?</text>
<text x="575" y="760" class="sm" text-anchor="middle">개념과 원리 이해</text>
<rect x="1000" y="380" width="700" height="420" rx="30" fill="{C['m']}" opacity="0.1"/>
<text x="1350" y="460" class="h2" text-anchor="middle">💻 노트북 (실습)</text>
<text x="1350" y="560" class="bd" text-anchor="middle">코드로 직접 실행</text>
<text x="1350" y="620" class="bd" text-anchor="middle">데이터 처리부터 평가까지</text>
<text x="1350" y="680" class="bd" text-anchor="middle">결과를 눈으로 확인</text>
<text x="1350" y="760" class="sm" text-anchor="middle">Prerequisites 6개 + Main 4개</text>
{tip('💡 강의로 이론을 이해하고, 노트북으로 직접 실습합니다')}
</svg>'''

# ========== SECTION 1: LoRA 이론 (004-015) ==========

def slide_004():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">출발: 우리가 가진 것</text>
<rect x="150" y="360" width="1620" height="150" rx="25" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="455" class="h2" text-anchor="middle">사전학습된 거대 모델 EXAONE 3.5</text>
<rect x="250" y="560" width="650" height="280" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="575" y="630" class="h2" text-anchor="middle">📚 모델이 아는 것</text>
<text x="575" y="710" class="bd" text-anchor="middle">일반적인 언어 지식</text>
<text x="575" y="770" class="bd" text-anchor="middle">광범위한 상식</text>
<rect x="1020" y="560" width="650" height="280" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1345" y="630" class="h2" text-anchor="middle">🎯 우리가 원하는 것</text>
<text x="1345" y="710" class="bd" text-anchor="middle">내 도메인 특화 지식</text>
<text x="1345" y="770" class="bd" text-anchor="middle">내 데이터로 맞춤 학습</text>
{tip('💡 거대 모델을 내 데이터에 맞게 조정하고 싶다!')}
</svg>'''

def slide_005():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">문제: Fine-tuning의 벽</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">전통적인 방법: 모든 파라미터 수정</text>
<rect x="200" y="450" width="700" height="380" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="530" class="h2" text-anchor="middle">파라미터란?</text>
<text x="550" y="620" class="bd" text-anchor="middle">모델의 기억 = 수십억 개의 숫자</text>
<text x="550" y="690" class="bd" text-anchor="middle">각 숫자가 학습된 지식 조각</text>
<text x="550" y="760" class="bd" text-anchor="middle">비유: 백과사전의 모든 글자</text>
<rect x="1020" y="450" width="680" height="380" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1360" y="530" class="h2" text-anchor="middle">Full Fine-tuning 문제</text>
<text x="1360" y="620" class="bd" text-anchor="middle">❌ 메모리 부족 (GPU 책상 작음)</text>
<text x="1360" y="690" class="bd" text-anchor="middle">❌ 시간 오래 걸림</text>
<text x="1360" y="760" class="bd" text-anchor="middle">❌ 비싼 GPU 여러 대 필요</text>
{tip('💡 거대한 백과사전 전체를 다시 쓰는 것처럼 비효율적')}
</svg>'''

def slide_006():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">핵심 질문</text>
<rect x="200" y="380" width="1520" height="200" rx="30" fill="{C['y']}" opacity="0.2"/>
<text x="960" y="460" class="t" text-anchor="middle">정말 모든 걸</text>
<text x="960" y="550" class="t" text-anchor="middle">바꿔야 할까?</text>
<rect x="250" y="640" width="650" height="180" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="575" y="720" class="bd" text-anchor="middle">대부분의 지식은 그대로 두고</text>
<text x="575" y="780" class="bd" text-anchor="middle">필요한 부분만 수정하면?</text>
<rect x="1020" y="640" width="650" height="180" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1345" y="720" class="bd" text-anchor="middle">원본은 고정 (frozen)</text>
<text x="1345" y="780" class="bd" text-anchor="middle">변화량만 별도 기록</text>
{tip('💡 이것이 LoRA 아이디어의 출발점입니다')}
</svg>'''

def slide_007():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">LoRA의 발견</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">변화량을 별도로 기록하자</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">원본 W₀</text>
<text x="550" y="630" class="bd" text-anchor="middle">사전학습된 가중치</text>
<text x="550" y="690" class="bd" text-anchor="middle">고정 (frozen)</text>
<text x="550" y="750" class="bd" text-anchor="middle">학습하지 않음</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">변화량 ΔW</text>
<text x="1370" y="630" class="bd" text-anchor="middle">추가로 학습할 내용</text>
<text x="1370" y="690" class="bd" text-anchor="middle">학습 가능 (trainable)</text>
<text x="1370" y="750" class="bd" text-anchor="middle">따로 저장</text>
<text x="960" y="890" class="h2" text-anchor="middle">사용 시: W₀ + ΔW</text>
{tip('💡 비유: 책을 다시 쓰지 말고, 수정 메모만 붙이기')}
</svg>'''

def slide_008():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Low-Rank의 의미</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">변화량을 압축 저장</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">직접 저장하면</text>
<text x="550" y="630" class="bd" text-anchor="middle">큰 변화량 ΔW 전체 저장</text>
<text x="550" y="690" class="bd" text-anchor="middle">여전히 메모리 많이 필요</text>
<text x="550" y="750" class="bd" text-anchor="middle">비유: 거대한 메모판</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">분해하면</text>
<text x="1370" y="630" class="bd" text-anchor="middle">ΔW = B × A (작은 행렬 2개)</text>
<text x="1370" y="690" class="bd" text-anchor="middle">메모리 대폭 절감</text>
<text x="1370" y="750" class="bd" text-anchor="middle">비유: 작은 메모지 여러 장</text>
{tip('💡 Rank = 정보의 본질적 차원. 대부분의 변화는 저차원으로 표현 가능')}
</svg>'''

def slide_009():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">행렬 분해 시각화</text>
<text x="960" y="340" class="h2" text-anchor="middle" fill="{C['pu']}">예: 1000×1000 행렬을 rank=64로 분해</text>
<rect x="200" y="420" width="270" height="250" rx="20" fill="{C['p']}" opacity="0.2"/>
<text x="335" y="480" class="h2" text-anchor="middle">B</text>
<text x="335" y="540" class="bd" text-anchor="middle">[1000×64]</text>
<text x="335" y="600" class="sm" text-anchor="middle">64,000개</text>
<text x="335" y="650" class="sm" text-anchor="middle">파라미터</text>
<text x="530" y="545" class="h1" text-anchor="middle">×</text>
<rect x="590" y="420" width="430" height="250" rx="20" fill="{C['m']}" opacity="0.2"/>
<text x="805" y="480" class="h2" text-anchor="middle">A</text>
<text x="805" y="540" class="bd" text-anchor="middle">[64×1000]</text>
<text x="805" y="600" class="sm" text-anchor="middle">64,000개</text>
<text x="805" y="650" class="sm" text-anchor="middle">파라미터</text>
<text x="1090" y="545" class="h1" text-anchor="middle">=</text>
<rect x="1150" y="420" width="420" height="250" rx="20" fill="{C['b']}" opacity="0.2"/>
<text x="1360" y="480" class="h2" text-anchor="middle">ΔW</text>
<text x="1360" y="540" class="bd" text-anchor="middle">[1000×1000]</text>
<text x="1360" y="600" class="sm" text-anchor="middle">동일한 결과!</text>
<rect x="200" y="710" width="750" height="140" rx="25" fill="{C['y']}" opacity="0.15"/>
<text x="575" y="770" class="h2" text-anchor="middle">LoRA 저장: 128K 파라미터</text>
<text x="575" y="825" class="bd" text-anchor="middle">64K + 64K = 128,000개</text>
<rect x="1000" y="710" width="720" height="140" rx="25" fill="#E74C3C" opacity="0.15"/>
<text x="1360" y="770" class="h2" text-anchor="middle">직접 저장: 1M 파라미터</text>
<text x="1360" y="825" class="bd" text-anchor="middle">1,000,000개 (87% 절감!)</text>
{tip('💡 행렬 곱셈으로 복원 가능하므로 작은 B, A만 저장하면 됨')}
</svg>'''

def slide_010():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">하이퍼파라미터 r (rank)</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">메모지 크기 결정</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">r이 크면</text>
<text x="550" y="630" class="bd" text-anchor="middle">✓ 표현력 높음</text>
<text x="550" y="690" class="bd" text-anchor="middle">✓ 복잡한 변화 가능</text>
<text x="550" y="750" class="bd" text-anchor="middle">✗ 메모리 많이 필요</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">r이 작으면</text>
<text x="1370" y="630" class="bd" text-anchor="middle">✓ 메모리 효율적</text>
<text x="1370" y="690" class="bd" text-anchor="middle">✓ 빠른 학습</text>
<text x="1370" y="750" class="bd" text-anchor="middle">✗ 표현력 제한</text>
{tip('💡 균형점 찾기가 중요! 실습에서는 r=64 사용')}
</svg>'''

def slide_011():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">하이퍼파라미터 alpha</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">변화량 조절 나사</text>
<rect x="150" y="450" width="1620" height="100" rx="20" fill="{C['b']}" opacity="0.15"/>
<text x="960" y="515" class="h2" text-anchor="middle">실제 변화량 = (alpha / r) × B × A</text>
<rect x="250" y="600" width="650" height="220" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="575" y="680" class="h2" text-anchor="middle">alpha 크면</text>
<text x="575" y="760" class="bd" text-anchor="middle">변화 폭이 커짐</text>
<rect x="1020" y="600" width="650" height="220" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1345" y="680" class="h2" text-anchor="middle">alpha 작으면</text>
<text x="1345" y="760" class="bd" text-anchor="middle">안정적, 보수적</text>
{tip('💡 보통 r의 2배 정도로 설정 (r=64면 alpha=128)')}
</svg>'''

def slide_012():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">어디에 LoRA를 적용할까?</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">Attention 메커니즘이 핵심</text>
<rect x="150" y="460" width="380" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="340" y="540" class="h2" text-anchor="middle">Q (Query)</text>
<text x="340" y="620" class="bd" text-anchor="middle">"무엇을 찾을까?"</text>
<text x="340" y="690" class="bd" text-anchor="middle">질문 만들기</text>
<rect x="580" y="460" width="380" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="770" y="540" class="h2" text-anchor="middle">K (Key)</text>
<text x="770" y="620" class="bd" text-anchor="middle">"어디에 있을까?"</text>
<text x="770" y="690" class="bd" text-anchor="middle">위치 찾기</text>
<rect x="1010" y="460" width="380" height="360" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1200" y="540" class="h2" text-anchor="middle">V (Value)</text>
<text x="1200" y="620" class="bd" text-anchor="middle">"무엇을 가져올까?"</text>
<text x="1200" y="690" class="bd" text-anchor="middle">정보 추출</text>
<rect x="1440" y="460" width="280" height="360" rx="25" fill="{C['y']}" opacity="0.1"/>
<text x="1580" y="540" class="h2" text-anchor="middle">O</text>
<text x="1580" y="620" class="bd" text-anchor="middle">출력</text>
<text x="1580" y="670" class="bd" text-anchor="middle">조합</text>
{tip('💡 이 4가지를 조정하면 모델이 "주목"하는 방식이 바뀝니다')}
</svg>'''

def slide_013():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">LoRA의 장점</text>
{box(250, 400, 600, 200, C['p'], '📉 메모리 절감', ['작은 GPU에서도 가능', '변화량만 저장'])}
{box(900, 400, 600, 200, C['m'], '⚡ 빠른 학습', ['일부만 학습', '시간 단축'])}
{box(250, 650, 600, 200, C['b'], '🔄 유연성', ['여러 어댑터 제작', '상황별 교체 가능'])}
{box(900, 650, 600, 200, C['y'], '📦 작은 배포', ['어댑터만 공유', '베이스 모델 재사용'])}
{tip('💡 이 4가지 장점이 LoRA를 인기 있게 만든 이유입니다')}
</svg>'''

def slide_014():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">LoRA의 한계</text>
<rect x="200" y="380" width="1520" height="160" rx="25" fill="{C['p']}" opacity="0.15"/>
<text x="960" y="455" class="h2" text-anchor="middle">변화량은 작아졌지만</text>
<text x="960" y="515" class="h2" text-anchor="middle">원본 모델 W₀는 여전히 크다</text>
<rect x="300" y="600" width="600" height="220" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="600" y="680" class="bd" text-anchor="middle">원본 모델을 메모리에</text>
<text x="600" y="740" class="bd" text-anchor="middle">올리는 것 자체가 부담</text>
<text x="600" y="800" class="bd" text-anchor="middle" fill="#E74C3C">여전히 큰 GPU 필요</text>
<rect x="1020" y="600" width="600" height="220" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1320" y="680" class="bd" text-anchor="middle">해결책은?</text>
<text x="1320" y="740" class="bd" text-anchor="middle">→ 모델 자체를 압축</text>
<text x="1320" y="800" class="bd" text-anchor="middle" fill="#27AE60">QLoRA 등장!</text>
{tip('💡 LoRA + 양자화 = QLoRA')}
</svg>'''

def slide_015():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">Section 1 정리</text>
<rect x="200" y="380" width="1520" height="500" rx="30" fill="{C['p']}" opacity="0.05"/>
<text x="960" y="470" class="h2" text-anchor="middle">핵심 개념</text>
<text x="300" y="560" class="bd">✓ Full Fine-tuning: 모든 파라미터 수정 → 메모리 부담 큼</text>
<text x="300" y="640" class="bd">✓ LoRA 아이디어: 원본 고정 + 변화량만 별도 기록</text>
<text x="300" y="720" class="bd">✓ Low-Rank: 변화량을 B×A로 분해하여 압축 저장</text>
<text x="300" y="800" class="bd">✓ 한계: 원본 모델은 여전히 크다</text>
<text x="960" y="910" class="h2" text-anchor="middle" fill="{C['b']}">다음: QLoRA로 모델 자체를 압축하기</text>
{tip('💡 LoRA = 변화량만 학습하는 효율적인 방법')}
</svg>'''

# ========== SECTION 2: QLoRA 이론 (016-023) ==========

def slide_016():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">새로운 문제</text>
<rect x="200" y="380" width="1520" height="180" rx="25" fill="{C['p']}" opacity="0.15"/>
<text x="960" y="455" class="h2" text-anchor="middle">LoRA로 학습은 가벼워졌지만</text>
<text x="960" y="525" class="h2" text-anchor="middle">모델 자체를 메모리에 올리는 게 힘들다</text>
<rect x="300" y="620" width="1320" height="200" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="960" y="700" class="bd" text-anchor="middle">비유: 가구를 옮기고 싶은데</text>
<text x="960" y="760" class="bd" text-anchor="middle">문이 좁아서 가구가 들어가지 않는 상황</text>
{tip('💡 해결책: 가구를 분해(압축)해서 들여놓기')}
</svg>'''

def slide_017():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">양자화 (Quantization)</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">정밀도를 포기하고 공간 확보</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">32-bit (원래)</text>
<text x="550" y="630" class="bd" text-anchor="middle">매우 정밀한 소수</text>
<text x="550" y="690" class="bd" text-anchor="middle">3.141592653589...</text>
<text x="550" y="750" class="bd" text-anchor="middle">공간 많이 차지</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">4-bit (양자화)</text>
<text x="1370" y="630" class="bd" text-anchor="middle">대략적인 값</text>
<text x="1370" y="690" class="bd" text-anchor="middle">3.14</text>
<text x="1370" y="750" class="bd" text-anchor="middle">공간 절약</text>
{tip('💡 비유: 소수점 여러 자리 → 반올림해서 정수로')}
</svg>'''

def slide_018():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">어떻게 압축할까?</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">숫자 표현 범위 줄이기</text>
<rect x="200" y="460" width="1520" height="120" rx="20" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="535" class="bd" text-anchor="middle">32-bit: 약 40억 가지 다른 숫자 표현 가능</text>
<rect x="200" y="620" width="1520" height="120" rx="20" fill="{C['m']}" opacity="0.1"/>
<text x="960" y="695" class="bd" text-anchor="middle">4-bit: 16가지 숫자만 표현 가능</text>
<text x="960" y="800" class="h2" text-anchor="middle">문제: 어떤 16가지를 선택할까?</text>
{tip('💡 비유: 수천 가지 색 → 16색 팔레트. 어떤 색을 선택할지가 중요')}
</svg>'''

def slide_019():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">NF4: 똑똑한 압축</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">Normal Float 4-bit</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">균등 양자화</text>
<text x="550" y="630" class="bd" text-anchor="middle">-8, -7, -6, ..., 0, ..., 7</text>
<text x="550" y="690" class="bd" text-anchor="middle">간격이 모두 같음</text>
<text x="550" y="750" class="bd" text-anchor="middle">단순하지만 비효율</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">NF4</text>
<text x="1370" y="630" class="bd" text-anchor="middle">가중치 분포에 최적화</text>
<text x="1370" y="690" class="bd" text-anchor="middle">자주 나오는 값에 집중</text>
<text x="1370" y="750" class="bd" text-anchor="middle">정보 손실 최소화</text>
{tip('💡 비유: 자주 쓰는 색을 팔레트에 더 많이 넣기')}
</svg>'''

def slide_020():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">QLoRA = LoRA + 양자화</text>
<rect x="150" y="360" width="1620" height="130" rx="25" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="445" class="h2" text-anchor="middle">두 기술의 결합</text>
<rect x="250" y="530" width="650" height="340" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="575" y="600" class="h2" text-anchor="middle">원본 모델 W₀</text>
<text x="575" y="680" class="bd" text-anchor="middle">4-bit로 압축 (NF4)</text>
<text x="575" y="740" class="bd" text-anchor="middle">고정 (frozen)</text>
<text x="575" y="800" class="sm" text-anchor="middle">메모리 75% 절감</text>
<rect x="1020" y="530" width="650" height="340" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1345" y="600" class="h2" text-anchor="middle">LoRA 어댑터 B×A</text>
<text x="1345" y="680" class="bd" text-anchor="middle">16-bit 유지 (BF16)</text>
<text x="1345" y="740" class="bd" text-anchor="middle">학습 (trainable)</text>
<text x="1345" y="800" class="sm" text-anchor="middle">rank=64, alpha=128</text>
<text x="960" y="920" class="h2" text-anchor="middle">추론: 압축된 모델 + 정밀한 어댑터</text>
{tip('💡 원본은 4-bit 압축, 어댑터는 16-bit 정밀도 유지')}
</svg>'''

def slide_021():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Double Quantization</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">압축의 압축</text>
<rect x="200" y="460" width="1520" height="130" rx="20" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="540" class="bd" text-anchor="middle">양자화에도 메타데이터가 필요 (스케일, 오프셋 등)</text>
<rect x="300" y="640" width="600" height="180" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="600" y="720" class="bd" text-anchor="middle">메타데이터도</text>
<text x="600" y="780" class="bd" text-anchor="middle">양자화해서 저장</text>
<rect x="1020" y="640" width="600" height="180" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1320" y="720" class="bd" text-anchor="middle">추가 메모리</text>
<text x="1320" y="780" class="bd" text-anchor="middle">절감 효과</text>
{tip('💡 비유: 압축 프로그램을 다시 압축하기')}
</svg>'''

def slide_022():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">QLoRA의 장점</text>
{box(200, 400, 700, 200, C['p'], '🗜️ 대폭 압축', ['작은 GPU 활용', '누구나 접근 가능'])}
{box(1020, 400, 700, 200, C['m'], '⚖️ 성능 유지', ['약간의 손실', '실용적 수준'])}
{box(200, 650, 700, 200, C['b'], '💰 비용 절감', ['비싼 GPU 불필요', '전기료 감소'])}
{box(1020, 650, 700, 200, C['y'], '🌍 민주화', ['개인도 학습', '연구 활성화'])}
{tip('💡 QLoRA 덕분에 개인 컴퓨터에서도 거대 모델 학습 가능')}
</svg>'''

def slide_023():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">Section 2 정리</text>
<rect x="200" y="380" width="1520" height="500" rx="30" fill="{C['m']}" opacity="0.05"/>
<text x="960" y="470" class="h2" text-anchor="middle">핵심 개념</text>
<text x="300" y="560" class="bd">✓ 양자화: 정밀도 포기로 메모리 절감 (32-bit → 4-bit)</text>
<text x="300" y="640" class="bd">✓ NF4: 가중치 분포에 최적화된 양자화 방식</text>
<text x="300" y="720" class="bd">✓ QLoRA: 압축된 모델(4-bit) + 정밀한 어댑터(32-bit)</text>
<text x="300" y="800" class="bd">✓ 작은 GPU에서도 거대 모델 Fine-tuning 가능</text>
<text x="960" y="910" class="h2" text-anchor="middle" fill="{C['b']}">다음: RAFT 데이터로 무엇을 학습할까?</text>
{tip('💡 QLoRA = LoRA + 양자화로 메모리 문제 해결')}
</svg>'''

# ========== SECTION 3: RAFT 데이터 이론 (024-035) ==========

def slide_024():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">데이터 이야기 시작</text>
<rect x="200" y="380" width="1520" height="160" rx="25" fill="{C['pu']}" opacity="0.15"/>
<text x="960" y="455" class="h2" text-anchor="middle">모델은 준비됐다 (QLoRA)</text>
<text x="960" y="515" class="h2" text-anchor="middle">무엇을 가르칠까?</text>
<rect x="300" y="600" width="600" height="220" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="600" y="680" class="bd" text-anchor="middle">일반적인 Q&amp;A?</text>
<text x="600" y="740" class="bd" text-anchor="middle">→ 단순 암기</text>
<text x="600" y="800" class="bd" text-anchor="middle">새로운 질문엔 약함</text>
<rect x="1020" y="600" width="600" height="220" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1320" y="680" class="bd" text-anchor="middle">현실적인 시나리오?</text>
<text x="1320" y="740" class="bd" text-anchor="middle">→ 검색 결과 보고 답하기</text>
<text x="1320" y="800" class="bd" text-anchor="middle" fill="#27AE60">일반화 능력↑</text>
{tip('💡 RAFT: Retrieval Augmented Fine-Tuning')}
</svg>'''

def slide_025():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">RAG의 한계</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">Retrieval-Augmented Generation</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">RAG 방식</text>
<text x="550" y="630" class="bd" text-anchor="middle">질문마다 DB 검색</text>
<text x="550" y="690" class="bd" text-anchor="middle">문서 찾아서 답변</text>
<text x="550" y="750" class="bd" text-anchor="middle">✗ 느림 (매번 검색)</text>
<text x="550" y="800" class="bd" text-anchor="middle">✗ 검색 의존</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">아이디어</text>
<text x="1370" y="630" class="bd" text-anchor="middle">자주 묻는 내용은</text>
<text x="1370" y="690" class="bd" text-anchor="middle">모델이 기억하면?</text>
<text x="1370" y="750" class="bd" text-anchor="middle">✓ 빠름 (검색 불필요)</text>
<text x="1370" y="800" class="bd" text-anchor="middle">✓ 도메인 특화</text>
{tip('💡 RAG 결과를 학습 데이터로 만들어 Fine-tuning → RAFT')}
</svg>'''

def slide_026():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">RAFT의 핵심 아이디어</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">검색 시뮬레이션</text>
<rect x="150" y="450" width="1620" height="120" rx="20" fill="{C['p']}" opacity="0.15"/>
<text x="960" y="525" class="bd" text-anchor="middle">질문 + 여러 문서 → 정답 찾기 (마치 검색 엔진처럼)</text>
<rect x="250" y="620" width="650" height="200" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="575" y="700" class="h2" text-anchor="middle">학습 데이터</text>
<text x="575" y="770" class="bd" text-anchor="middle">검색 결과처럼 구성</text>
<rect x="1020" y="620" width="650" height="200" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1345" y="700" class="h2" text-anchor="middle">학습 과정</text>
<text x="1345" y="770" class="bd" text-anchor="middle">문서 보고 답하는 법</text>
{tip('💡 이 과정 자체를 학습 데이터로 만든다')}
</svg>'''

def slide_027():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Oracle 문서</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">정답이 있는 문서</text>
<rect x="200" y="460" width="1520" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="540" class="h2" text-anchor="middle">특징</text>
<text x="960" y="630" class="bd" text-anchor="middle">✓ 질문에 대한 답을 포함</text>
<text x="960" y="700" class="bd" text-anchor="middle">✓ 1개만 제공 (golden document)</text>
<text x="960" y="770" class="bd" text-anchor="middle">✓ 모델이 이걸 찾아서 답해야 함</text>
{tip('💡 비유: 시험 문제집의 정답 페이지')}
</svg>'''

def slide_028():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Distractor 문서</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">방해꾼 (산만하게 하는 것)</text>
<rect x="200" y="460" width="1520" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="960" y="540" class="h2" text-anchor="middle">특징</text>
<text x="960" y="630" class="bd" text-anchor="middle">✓ 관련 없거나 오해를 유발하는 문서</text>
<text x="960" y="700" class="bd" text-anchor="middle">✓ 여러 개 섞여 있음</text>
<text x="960" y="770" class="bd" text-anchor="middle">✓ 현실의 검색 결과를 모사</text>
{tip('💡 비유: 시험에 섞인 낚시 문제, 헷갈리게 만드는 오답 선지')}
</svg>'''

def slide_029():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">왜 Distractor가 필요한가?</text>
<rect x="200" y="360" width="700" height="460" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="440" class="h2" text-anchor="middle">Oracle만 학습하면</text>
<text x="550" y="540" class="bd" text-anchor="middle">❌ 항상 좋은 문서만</text>
<text x="550" y="600" class="bd" text-anchor="middle">❌ 노이즈 대응 못함</text>
<text x="550" y="660" class="bd" text-anchor="middle">❌ 현실과 괴리</text>
<text x="550" y="740" class="bd" text-anchor="middle" fill="#E74C3C">과적합 위험</text>
<rect x="1020" y="360" width="700" height="460" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="440" class="h2" text-anchor="middle">Distractor 섞으면</text>
<text x="1370" y="540" class="bd" text-anchor="middle">✓ 노이즈 섞인 상황</text>
<text x="1370" y="600" class="bd" text-anchor="middle">✓ 좋은 문서 찾는 법</text>
<text x="1370" y="660" class="bd" text-anchor="middle">✓ 현실적 시나리오</text>
<text x="1370" y="740" class="bd" text-anchor="middle" fill="#27AE60">일반화 능력↑</text>
{tip('💡 현실의 검색은 완벽하지 않다. 관련 없는 문서도 많이 나온다')}
</svg>'''

def slide_030():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">RAFT 학습 과정</text>
<rect x="150" y="350" width="390" height="470" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="345" y="420" class="h2" text-anchor="middle">1. 문서 읽기</text>
<text x="345" y="510" class="bd" text-anchor="middle">Oracle +</text>
<text x="345" y="570" class="bd" text-anchor="middle">Distractors</text>
<text x="345" y="630" class="bd" text-anchor="middle">여러 개 제시</text>
<rect x="590" y="350" width="390" height="470" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="785" y="420" class="h2" text-anchor="middle">2. 판단 학습</text>
<text x="785" y="510" class="bd" text-anchor="middle">어떤 문서가</text>
<text x="785" y="570" class="bd" text-anchor="middle">유용한가?</text>
<text x="785" y="630" class="bd" text-anchor="middle">어떤 건</text>
<text x="785" y="690" class="bd" text-anchor="middle">무시해야 하나?</text>
<rect x="1030" y="350" width="390" height="470" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1225" y="420" class="h2" text-anchor="middle">3. 답변 생성</text>
<text x="1225" y="510" class="bd" text-anchor="middle">Oracle 기반</text>
<text x="1225" y="570" class="bd" text-anchor="middle">정확한 답변</text>
<rect x="1470" y="350" width="250" height="470" rx="25" fill="{C['y']}" opacity="0.1"/>
<text x="1595" y="420" class="h2" text-anchor="middle">반복</text>
<text x="1595" y="510" class="bd" text-anchor="middle">다양한</text>
<text x="1595" y="560" class="bd" text-anchor="middle">상황</text>
<text x="1595" y="610" class="bd" text-anchor="middle">학습</text>
<text x="960" y="910" class="h2" text-anchor="middle" fill="{C['b']}">다음: 데이터 품질 확인</text>
{tip('💡 모델이 스스로 유용한 정보를 선별하는 법을 배운다')}
</svg>'''

def slide_031():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Oracle 없는 경우</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">모른다고 말하는 법 배우기</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">일부 샘플</text>
<text x="550" y="630" class="bd" text-anchor="middle">Oracle 제거</text>
<text x="550" y="690" class="bd" text-anchor="middle">Distractor만 제공</text>
<text x="550" y="750" class="bd" text-anchor="middle">정답 없는 상황</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">학습 목표</text>
<text x="1370" y="630" class="bd" text-anchor="middle">"정보 부족" 판단</text>
<text x="1370" y="690" class="bd" text-anchor="middle">"모르겠습니다" 답변</text>
<text x="1370" y="750" class="bd" text-anchor="middle">거짓말보다 낫다</text>
{tip('💡 잘못된 답변보다 "모름"을 인정하는 게 더 정직하다')}
</svg>'''

def slide_032():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Label 마스킹 원리</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">답변만 학습하기</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">질문 부분</text>
<text x="550" y="630" class="bd" text-anchor="middle">학습하지 않음 (mask)</text>
<text x="550" y="690" class="bd" text-anchor="middle">-100으로 표시</text>
<text x="550" y="750" class="bd" text-anchor="middle">Loss 계산 제외</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">답변 부분</text>
<text x="1370" y="630" class="bd" text-anchor="middle">학습 대상</text>
<text x="1370" y="690" class="bd" text-anchor="middle">실제 토큰 ID</text>
<text x="1370" y="750" class="bd" text-anchor="middle">Loss 계산 포함</text>
{tip('💡 질문 형식을 외우는 게 아니라, 답변 생성에만 집중')}
</svg>'''

def slide_033():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">토큰화 (Tokenization)</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">텍스트를 숫자로 변환</text>
<rect x="200" y="460" width="1520" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="540" class="h2" text-anchor="middle">왜 필요한가?</text>
<text x="960" y="630" class="bd" text-anchor="middle">모델은 숫자만 이해할 수 있다</text>
<text x="960" y="700" class="bd" text-anchor="middle">텍스트 → 토큰 → ID (숫자)</text>
<text x="960" y="770" class="bd" text-anchor="middle">예: "안녕" → [12345, 67890]</text>
{tip('💡 Tokenizer가 이 변환을 자동으로 처리')}
</svg>'''

def slide_034():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Context 구성</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">질문 + 문서들</text>
<rect x="200" y="460" width="1520" height="140" rx="20" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="545" class="bd" text-anchor="middle">Question + Document 1 + Document 2 + ... + Document N</text>
<rect x="300" y="650" width="600" height="170" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="600" y="730" class="bd" text-anchor="middle">순서는 랜덤</text>
<text x="600" y="790" class="bd" text-anchor="middle">(위치 편향 방지)</text>
<rect x="1020" y="650" width="600" height="170" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1320" y="730" class="bd" text-anchor="middle">모델이 내용으로</text>
<text x="1320" y="790" class="bd" text-anchor="middle">판단하도록</text>
{tip('💡 Oracle이 항상 첫 번째면 모델이 위치를 외워버린다')}
</svg>'''

def slide_035():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">Section 3 정리</text>
<rect x="200" y="380" width="1520" height="500" rx="30" fill="{C['b']}" opacity="0.05"/>
<text x="960" y="470" class="h2" text-anchor="middle">핵심 개념</text>
<text x="300" y="560" class="bd">✓ RAFT: 검색 시뮬레이션을 학습 데이터로</text>
<text x="300" y="640" class="bd">✓ Oracle (정답) + Distractors (노이즈) 섞어서 제공</text>
<text x="300" y="720" class="bd">✓ 모델이 유용한 문서 선별하는 법 학습</text>
<text x="300" y="800" class="bd">✓ Label 마스킹으로 답변 부분만 효율적 학습</text>
<text x="960" y="910" class="h2" text-anchor="middle" fill="{C['m']}">다음: 학습 과정은 어떻게 진행되는가?</text>
{tip('💡 RAFT = 현실적인 검색 상황을 학습 데이터로')}
</svg>'''

# ========== SECTION 4: 학습 과정 이론 (036-045) ==========

def slide_036():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">학습이란?</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">틀린 만큼 수정하기</text>
<rect x="150" y="450" width="390" height="370" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="345" y="530" class="h2" text-anchor="middle">1. 예측</text>
<text x="345" y="620" class="bd" text-anchor="middle">모델이</text>
<text x="345" y="680" class="bd" text-anchor="middle">답을 생성</text>
<rect x="590" y="450" width="390" height="370" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="785" y="530" class="h2" text-anchor="middle">2. 비교</text>
<text x="785" y="620" class="bd" text-anchor="middle">정답과</text>
<text x="785" y="680" class="bd" text-anchor="middle">비교</text>
<rect x="1030" y="450" width="390" height="370" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1225" y="530" class="h2" text-anchor="middle">3. 조정</text>
<text x="1225" y="620" class="bd" text-anchor="middle">차이만큼</text>
<text x="1225" y="680" class="bd" text-anchor="middle">파라미터</text>
<text x="1225" y="740" class="bd" text-anchor="middle">수정</text>
<rect x="1470" y="450" width="250" height="370" rx="25" fill="{C['y']}" opacity="0.1"/>
<text x="1595" y="530" class="h2" text-anchor="middle">반복</text>
<text x="1595" y="620" class="bd" text-anchor="middle">점점</text>
<text x="1595" y="680" class="bd" text-anchor="middle">정확</text>
<text x="1595" y="740" class="bd" text-anchor="middle">해짐</text>
{tip('💡 비유: 과녁 맞추기. 빗나간 만큼 다음에 조정')}
</svg>'''

def slide_037():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Loss Function</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">얼마나 틀렸나?</text>
<rect x="200" y="460" width="1520" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="540" class="h2" text-anchor="middle">Cross-Entropy Loss</text>
<text x="960" y="630" class="bd" text-anchor="middle">확률 분포의 차이를 측정</text>
<text x="960" y="700" class="bd" text-anchor="middle">정답에 가까울수록 Loss ↓</text>
<text x="960" y="770" class="bd" text-anchor="middle">0에 가까워지도록 학습</text>
{tip('💡 Loss = 틀린 정도. 낮을수록 좋다')}
</svg>'''

def slide_038():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Optimizer</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">어떻게 수정할까?</text>
<rect x="250" y="460" width="650" height="290" rx="25" fill="{C['p']}" opacity="0.15"/>
<text x="575" y="540" class="h2" text-anchor="middle" font-weight="700">📍 Gradient</text>
<text x="575" y="630" class="bd" text-anchor="middle">틀린 방향 계산</text>
<text x="575" y="690" class="bd" text-anchor="middle">어느 방향으로 수정할지</text>
<rect x="1020" y="460" width="650" height="290" rx="25" fill="{C['m']}" opacity="0.15"/>
<text x="1345" y="540" class="h2" text-anchor="middle" font-weight="700">📏 Learning Rate</text>
<text x="1345" y="630" class="bd" text-anchor="middle">수정 폭 결정</text>
<text x="1345" y="690" class="bd" text-anchor="middle">한 번에 얼마나 바꿀지</text>
{tip('💡 Adam: 효율적인 수정 방법 (자동으로 학습률 조절)')}
</svg>'''

def slide_039():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Learning Rate</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">한 번에 얼마나?</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">크면</text>
<text x="550" y="630" class="bd" text-anchor="middle">✓ 빠르게 이동</text>
<text x="550" y="690" class="bd" text-anchor="middle">✗ 불안정</text>
<text x="550" y="750" class="bd" text-anchor="middle">✗ 최적점 건너뜀</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">작으면</text>
<text x="1370" y="630" class="bd" text-anchor="middle">✓ 안정적</text>
<text x="1370" y="690" class="bd" text-anchor="middle">✗ 너무 느림</text>
<text x="1370" y="750" class="bd" text-anchor="middle">✗ 수렴 안 함</text>
{tip('💡 비유: 걸음 크기. 너무 크면 넘어지고, 너무 작으면 못 간다')}
</svg>'''

def slide_040():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Batch</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">몇 개씩 묶어서?</text>
<rect x="200" y="460" width="1520" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="540" class="h2" text-anchor="middle">Batch 개념</text>
<text x="960" y="630" class="bd" text-anchor="middle">한 번에 여러 샘플 보고 평균내기</text>
<text x="960" y="700" class="bd" text-anchor="middle">안정적인 학습</text>
<text x="960" y="770" class="bd" text-anchor="middle">메모리와 속도의 균형</text>
{tip('💡 비유: 시험 문제를 한 문제씩 vs 여러 문제 풀고 평균 점수')}
</svg>'''

def slide_041():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Gradient Accumulation</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">메모리 절약 기법</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">일반적인 방법</text>
<text x="550" y="630" class="bd" text-anchor="middle">큰 배치 한 번에 처리</text>
<text x="550" y="690" class="bd" text-anchor="middle">→ 메모리 많이 필요</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">Accumulation</text>
<text x="1370" y="630" class="bd" text-anchor="middle">작은 배치 여러 번</text>
<text x="1370" y="690" class="bd" text-anchor="middle">Gradient 누적 후 업데이트</text>
<text x="1370" y="750" class="bd" text-anchor="middle">→ 효과는 같고 메모리 절약</text>
{tip('💡 비유: 큰 짐을 한 번에 vs 나눠서 여러 번')}
</svg>'''

def slide_042():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Epoch</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">전체 데이터 몇 바퀴?</text>
<rect x="200" y="460" width="1520" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="540" class="h2" text-anchor="middle">1 Epoch = 모든 데이터 1회</text>
<text x="960" y="630" class="bd" text-anchor="middle">여러 epoch 반복</text>
<text x="960" y="700" class="bd" text-anchor="middle">너무 많으면 과적합</text>
<text x="960" y="770" class="bd" text-anchor="middle">너무 적으면 학습 부족</text>
{tip('💡 비유: 문제집을 몇 번 반복할까?')}
</svg>'''

def slide_043():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">과적합 (Overfitting)</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">문제집만 외우기</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">증상</text>
<text x="550" y="630" class="bd" text-anchor="middle">Training Loss ↓ (좋음)</text>
<text x="550" y="690" class="bd" text-anchor="middle">Validation Loss ↑ (나쁨)</text>
<text x="550" y="750" class="bd" text-anchor="middle">새 데이터에 약함</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">해결</text>
<text x="1370" y="630" class="bd" text-anchor="middle">Dropout (일부 끄기)</text>
<text x="1370" y="690" class="bd" text-anchor="middle">Early Stopping</text>
<text x="1370" y="750" class="bd" text-anchor="middle">더 많은 데이터</text>
{tip('💡 비유: 문제집 답을 외웠지만, 새 문제는 못 푸는 상황')}
</svg>'''

def slide_044():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">학습 곡선 읽기</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">진행 상황 체크</text>
<rect x="200" y="460" width="520" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="460" y="540" class="h2" text-anchor="middle">정상 학습</text>
<text x="460" y="630" class="bd" text-anchor="middle">Train Loss ↓</text>
<text x="460" y="690" class="bd" text-anchor="middle">Val Loss ↓</text>
<text x="460" y="750" class="bd" text-anchor="middle" fill="#27AE60">계속 진행</text>
<rect x="770" y="460" width="520" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1030" y="540" class="h2" text-anchor="middle">과적합</text>
<text x="1030" y="630" class="bd" text-anchor="middle">Train Loss ↓</text>
<text x="1030" y="690" class="bd" text-anchor="middle">Val Loss ↑</text>
<text x="1030" y="750" class="bd" text-anchor="middle" fill="#F39C12">주의 필요</text>
<rect x="1340" y="460" width="380" height="360" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1530" y="540" class="h2" text-anchor="middle">실패</text>
<text x="1530" y="630" class="bd" text-anchor="middle">Loss 발산</text>
<text x="1530" y="690" class="bd" text-anchor="middle">NaN 발생</text>
<text x="1530" y="750" class="bd" text-anchor="middle" fill="#E74C3C">재시작</text>
{tip('💡 두 Loss를 함께 모니터링해야 한다')}
</svg>'''

def slide_045():
    return H + f'''
{dots()}
<text x="960" y="280" class="h1" text-anchor="middle">Section 4 정리</text>
<rect x="200" y="380" width="1520" height="500" rx="30" fill="{C['y']}" opacity="0.05"/>
<text x="960" y="470" class="h2" text-anchor="middle">핵심 개념</text>
<text x="300" y="560" class="bd">✓ 학습: 예측 → 비교 → 조정 반복</text>
<text x="300" y="640" class="bd">✓ Loss: 틀린 정도 (0에 가깝게)</text>
<text x="300" y="720" class="bd">✓ Learning Rate: 수정 폭 (균형 중요)</text>
<text x="300" y="800" class="bd">✓ 과적합: Training vs Validation 곡선으로 감지</text>
<text x="960" y="910" class="h2" text-anchor="middle" fill="{C['m']}">다음: 고급 학습 기법</text>
{tip('💡 Loss를 줄이는 반복 과정이 학습')}
</svg>'''

# ========== SECTION 5: 평가 이론 (046-050) ==========

def slide_046():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">평가의 필요성</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">Before vs After</text>
<rect x="250" y="460" width="650" height="290" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="575" y="540" class="h2" text-anchor="middle">주관적 느낌</text>
<text x="575" y="630" class="bd" text-anchor="middle">"더 좋아진 것 같다"</text>
<text x="575" y="700" class="bd" text-anchor="middle">✗ 불명확</text>
<rect x="1020" y="460" width="650" height="290" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1345" y="540" class="h2" text-anchor="middle">정량적 지표</text>
<text x="1345" y="630" class="bd" text-anchor="middle">숫자로 측정</text>
<text x="1345" y="700" class="bd" text-anchor="middle">✓ 명확한 비교</text>
{tip('💡 학습 전/후를 객관적으로 비교해야 한다')}
</svg>'''

def slide_047():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">ROUGE 원리</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">단어 겹침 비율</text>
<rect x="200" y="460" width="1520" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="540" class="h2" text-anchor="middle">개념</text>
<text x="960" y="630" class="bd" text-anchor="middle">정답과 예측의 공통 단어</text>
<text x="960" y="700" class="bd" text-anchor="middle">Recall 중심 (정답 단어를 얼마나 포함?)</text>
<text x="960" y="770" class="bd" text-anchor="middle">요약/생성 태스크 표준</text>
{tip('💡 ROUGE = Recall-Oriented Understudy for Gisting Evaluation')}
</svg>'''

def slide_048():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">ROUGE의 한계</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">형태만 본다</text>
<rect x="200" y="460" width="1520" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="960" y="540" class="h2" text-anchor="middle">문제점</text>
<text x="960" y="630" class="bd" text-anchor="middle">❌ "절감" ≠ "줄임" (다른 단어로 인식)</text>
<text x="960" y="700" class="bd" text-anchor="middle">❌ 동의어 무시</text>
<text x="960" y="770" class="bd" text-anchor="middle">❌ 의미는 고려하지 않음</text>
{tip('💡 단어 매칭만으로는 의미적 유사성을 놓친다')}
</svg>'''

def slide_049():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Embedding Similarity</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">의미 거리 측정</text>
<rect x="150" y="450" width="520" height="370" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="410" y="530" class="h2" text-anchor="middle">1. 임베딩</text>
<text x="410" y="620" class="bd" text-anchor="middle">문장 →</text>
<text x="410" y="680" class="bd" text-anchor="middle">벡터</text>
<rect x="720" y="450" width="520" height="370" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="980" y="530" class="h2" text-anchor="middle">2. 거리 계산</text>
<text x="980" y="620" class="bd" text-anchor="middle">Cosine</text>
<text x="980" y="680" class="bd" text-anchor="middle">Similarity</text>
<rect x="1290" y="450" width="430" height="370" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1505" y="530" class="h2" text-anchor="middle">3. 장점</text>
<text x="1505" y="620" class="bd" text-anchor="middle">동의어</text>
<text x="1505" y="680" class="bd" text-anchor="middle">인식</text>
<text x="1505" y="740" class="bd" text-anchor="middle">"절감"≈"줄임"</text>
{tip('💡 의미가 비슷하면 벡터도 가까워진다')}
</svg>'''

def slide_050():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Section 5 정리</text>
<rect x="200" y="380" width="1520" height="500" rx="30" fill="{C['pu']}" opacity="0.05"/>
<text x="960" y="470" class="h2" text-anchor="middle">핵심 개념</text>
<text x="300" y="560" class="bd">✓ 객관적 평가 지표 필요</text>
<text x="300" y="640" class="bd">✓ ROUGE: 단어 겹침 (빠르고 간단)</text>
<text x="300" y="720" class="bd">✓ Embedding Similarity: 의미 유사도 (정확)</text>
<text x="300" y="800" class="bd">✓ 두 지표를 함께 사용하여 다각도 평가</text>
<text x="960" y="910" class="h2" text-anchor="middle" fill="{C['b']}">다음: 실전 &amp; 배포</text>
{tip('💡 ROUGE + Embedding Similarity 조합이 최선')}
</svg>'''

# ========== SECTION 2.5: 데이터 분석 & 검증 (051-056) ==========

def slide_051():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">데이터 품질의 중요성</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">Garbage In, Garbage Out</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">나쁜 데이터</text>
<text x="550" y="630" class="bd" text-anchor="middle">❌ 결측치 많음</text>
<text x="550" y="690" class="bd" text-anchor="middle">❌ 중복/오류</text>
<text x="550" y="750" class="bd" text-anchor="middle">❌ 불균형</text>
<text x="550" y="800" class="bd" text-anchor="middle" fill="#E74C3C">→ 나쁜 모델</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">좋은 데이터</text>
<text x="1370" y="630" class="bd" text-anchor="middle">✓ 완전한 정보</text>
<text x="1370" y="690" class="bd" text-anchor="middle">✓ 정제된 품질</text>
<text x="1370" y="750" class="bd" text-anchor="middle">✓ 적절한 분포</text>
<text x="1370" y="800" class="bd" text-anchor="middle" fill="#27AE60">→ 좋은 모델</text>
{tip('💡 학습 전 데이터 검증은 필수!')}
</svg>'''

def slide_052():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">스키마 검증</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">데이터 구조 확인</text>
{box(200, 420, 700, 260, C['p'], '필수 컬럼', ['question 존재?', 'answer 존재?', 'documents 존재?'])}
{box(1020, 420, 700, 260, C['m'], '데이터 타입', ['문자열인가?', '리스트인가?', '타입 일관성'])}
{box(200, 710, 700, 130, C['b'], '구조 일관성', ['모든 샘플 동일 구조'])}
{box(1020, 710, 700, 130, C['y'], '빠른 발견', ['초기 단계에서 오류 차단'])}
{tip('💡 스키마 불일치는 학습 중 에러의 주요 원인')}
</svg>'''

def slide_053():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">결측치 &amp; 중복 처리</text>
<rect x="200" y="360" width="700" height="460" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="440" class="h2" text-anchor="middle">결측치 (Missing Values)</text>
<text x="550" y="540" class="bd" text-anchor="middle">빈 문자열 ""</text>
<text x="550" y="600" class="bd" text-anchor="middle">None, null</text>
<text x="550" y="660" class="bd" text-anchor="middle">처리: 제거 or 기본값</text>
<text x="550" y="740" class="bd" text-anchor="middle" fill="#E74C3C">학습 오류 유발</text>
<rect x="1020" y="360" width="700" height="460" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="440" class="h2" text-anchor="middle">중복 (Duplicates)</text>
<text x="1370" y="540" class="bd" text-anchor="middle">같은 질문/답변</text>
<text x="1370" y="600" class="bd" text-anchor="middle">과적합 위험</text>
<text x="1370" y="660" class="bd" text-anchor="middle">처리: 제거</text>
<text x="1370" y="740" class="bd" text-anchor="middle" fill="#F39C12">데이터 편향</text>
{tip('💡 실습 노트북 02에서 자동 검사')}
</svg>'''

def slide_054():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">토큰 길이 분석</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">Distribution 확인</text>
<rect x="150" y="450" width="520" height="370" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="410" y="530" class="h2" text-anchor="middle">평균 길이</text>
<text x="410" y="620" class="bd" text-anchor="middle">전체 평균</text>
<text x="410" y="680" class="bd" text-anchor="middle">너무 길면?</text>
<text x="410" y="740" class="bd" text-anchor="middle">메모리 부족</text>
<rect x="720" y="450" width="520" height="370" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="980" y="530" class="h2" text-anchor="middle">최대 길이</text>
<text x="980" y="620" class="bd" text-anchor="middle">이상치 탐지</text>
<text x="980" y="680" class="bd" text-anchor="middle">잘릴 위험</text>
<text x="980" y="740" class="bd" text-anchor="middle">정보 손실</text>
<rect x="1290" y="450" width="430" height="370" rx="25" fill="{C['b']}" opacity="0.1"/>
<text x="1505" y="530" class="h2" text-anchor="middle">분포 확인</text>
<text x="1505" y="620" class="bd" text-anchor="middle">히스토그램</text>
<text x="1505" y="680" class="bd" text-anchor="middle">불균형?</text>
<text x="1505" y="740" class="bd" text-anchor="middle">조정 필요</text>
{tip('💡 적절한 max_seq_length 설정의 기준')}
</svg>'''

def slide_055():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Context Length 제한</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">max_seq_length</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">잘림 (Truncation)</text>
<text x="550" y="630" class="bd" text-anchor="middle">너무 긴 텍스트</text>
<text x="550" y="690" class="bd" text-anchor="middle">뒷부분 잘림</text>
<text x="550" y="750" class="bd" text-anchor="middle">정보 손실 위험</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">패딩 (Padding)</text>
<text x="1370" y="630" class="bd" text-anchor="middle">너무 짧은 텍스트</text>
<text x="1370" y="690" class="bd" text-anchor="middle">빈 공간 채우기</text>
<text x="1370" y="750" class="bd" text-anchor="middle">메모리 낭비</text>
{tip('💡 실습에서는 2048 사용 (EXAONE 기준)')}
</svg>'''

def slide_056():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Train/Validation Split</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">데이터 분리 전략</text>
{box(200, 460, 700, 180, C['p'], '분리 비율', ['Train 80-90%', 'Validation 10-20%', '적절한 균형'])}
{box(1020, 460, 700, 180, C['m'], '랜덤 vs 계층화', ['랜덤: 무작위', '계층화: 분포 유지', '일반적으로 랜덤'])}
{box(200, 690, 700, 130, C['b'], '데이터 누수 방지', ['Test 데이터 절대 학습X'])}
{box(1020, 690, 700, 130, C['y'], '재현성', ['Random seed 고정'])}
<text x="960" y="910" class="h2" text-anchor="middle" fill="{C['m']}">다음: 학습 이론</text>
{tip('💡 Validation으로 과적합 모니터링')}
</svg>'''

# ========== SECTION 4.5: 고급 학습 기법 (057-060) ==========

def slide_057():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Warmup Steps</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">서서히 올리기</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">문제: 초기 불안정</text>
<text x="550" y="630" class="bd" text-anchor="middle">처음부터 큰 Learning Rate</text>
<text x="550" y="690" class="bd" text-anchor="middle">→ Gradient 폭발</text>
<text x="550" y="750" class="bd" text-anchor="middle">→ Loss 발산</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">해결: Warmup</text>
<text x="1370" y="630" class="bd" text-anchor="middle">0에서 서서히 증가</text>
<text x="1370" y="690" class="bd" text-anchor="middle">안정적인 시작</text>
<text x="1370" y="750" class="bd" text-anchor="middle">전체 10% 정도</text>
{tip('💡 비유: 자동차 워밍업처럼 천천히 시작')}
</svg>'''

def slide_058():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Learning Rate Scheduler</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">동적으로 조절</text>
{box(200, 460, 500, 180, C['p'], 'Cosine Annealing', ['코사인 곡선', '부드럽게 감소', '많이 사용'])}
{box(750, 460, 500, 180, C['m'], 'Linear Decay', ['선형 감소', '단순하고 안정', '예측 가능'])}
{box(1300, 460, 420, 180, C['b'], 'Constant', ['고정', '간단', '덜 효율적'])}
{box(200, 690, 750, 130, C['y'], '왜 필요한가?', ['후반: 세밀한 조정', '수렴 가속화'])}
{box(1000, 690, 720, 130, C['o'], '실습', ['Cosine 사용'])}
{tip('💡 학습 진행에 따라 Learning Rate 줄이기')}
</svg>'''

def slide_059():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Gradient Clipping</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">폭발 방지</text>
<rect x="200" y="460" width="700" height="360" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="540" class="h2" text-anchor="middle">Gradient Explosion</text>
<text x="550" y="630" class="bd" text-anchor="middle">Gradient가 너무 큼</text>
<text x="550" y="690" class="bd" text-anchor="middle">파라미터 급변</text>
<text x="550" y="750" class="bd" text-anchor="middle">NaN Loss 발생</text>
<rect x="1020" y="460" width="700" height="360" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="540" class="h2" text-anchor="middle">Clipping</text>
<text x="1370" y="630" class="bd" text-anchor="middle">Max Norm 설정 (1.0)</text>
<text x="1370" y="690" class="bd" text-anchor="middle">초과 시 잘라냄</text>
<text x="1370" y="750" class="bd" text-anchor="middle">안정적 학습</text>
{tip('💡 비유: 속도 제한기처럼 최대값 제한')}
</svg>'''

def slide_060():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">Mixed Precision Training</text>
<text x="960" y="360" class="h2" text-anchor="middle" fill="{C['pu']}">FP16 / BF16</text>
{box(200, 460, 700, 180, C['p'], 'FP32 (원래)', ['32-bit 정밀도', '정확하지만 느림', '메모리 많이 사용'])}
{box(1020, 460, 700, 180, C['m'], 'FP16', ['16-bit 정밀도', '빠르고 가벼움', '범위 제한'])}
{box(200, 690, 700, 130, C['b'], 'BF16 (추천)', ['16-bit', '넓은 범위', 'Overflow 적음'])}
{box(1020, 690, 700, 130, C['y'], '효과', ['메모리 50% 절감', '속도 2배 향상'])}
<text x="960" y="910" class="h2" text-anchor="middle" fill="{C['b']}">다음: 평가 방법</text>
{tip('💡 실습에서는 BF16 사용 (Modern GPU)')}
</svg>'''

# ========== SECTION 5.5: 실전 & 배포 (061-062) ==========

def slide_061():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">OOM &amp; Checkpoint 전략</text>
<rect x="200" y="360" width="700" height="460" rx="25" fill="{C['p']}" opacity="0.1"/>
<text x="550" y="440" class="h2" text-anchor="middle">OOM 대처법</text>
<text x="550" y="540" class="bd" text-anchor="middle">✓ Batch size 줄이기</text>
<text x="550" y="600" class="bd" text-anchor="middle">✓ Gradient Accumulation</text>
<text x="550" y="660" class="bd" text-anchor="middle">✓ Sequence 길이 줄이기</text>
<text x="550" y="720" class="bd" text-anchor="middle">✓ Mixed Precision</text>
<rect x="1020" y="360" width="700" height="460" rx="25" fill="{C['m']}" opacity="0.1"/>
<text x="1370" y="440" class="h2" text-anchor="middle">Checkpoint 저장</text>
<text x="1370" y="540" class="bd" text-anchor="middle">✓ 주기적 저장</text>
<text x="1370" y="600" class="bd" text-anchor="middle">✓ Best model 보관</text>
<text x="1370" y="660" class="bd" text-anchor="middle">✓ 학습 재개 가능</text>
<text x="1370" y="720" class="bd" text-anchor="middle">✓ 실험 재현성</text>
{tip('💡 중단되어도 다시 시작할 수 있게 준비')}
</svg>'''

def slide_062():
    return H + f'''
{dots()}
<text x="960" y="260" class="h1" text-anchor="middle">전체 여정 정리</text>
<rect x="200" y="320" width="1520" height="580" rx="30" fill="{C['pu']}" opacity="0.05"/>
<text x="960" y="390" class="h2" text-anchor="middle">오늘 배운 이론</text>
<text x="300" y="460" class="bd">1️⃣ 문제: Fine-tuning은 메모리가 많이 필요</text>
<text x="300" y="520" class="bd">2️⃣ LoRA: 변화량만 기록 (B×A 분해)</text>
<text x="300" y="580" class="bd">3️⃣ QLoRA: 모델 압축 (4-bit 양자화)</text>
<text x="300" y="640" class="bd">4️⃣ RAFT: 검색 시뮬레이션 학습 (Oracle + Distractors)</text>
<text x="300" y="700" class="bd">5️⃣ 데이터: 품질 검증, 토큰 분석, Train/Val Split</text>
<text x="300" y="760" class="bd">6️⃣ 학습: Loss, Optimizer, Warmup, Scheduler</text>
<text x="300" y="820" class="bd">7️⃣ 평가: ROUGE + Embedding Similarity</text>
<text x="300" y="880" class="bd">8️⃣ 실전: OOM 대처, Checkpoint, Mixed Precision</text>
<text x="960" y="950" class="h2" text-anchor="middle" fill="{C['b']}">이제 실습 노트북으로 직접 해봅시다!</text>
{tip('🎉 이론 학습 완료! 8개 노트북으로 직접 실행해보세요')}
</svg>'''

# ========== GENERATE ALL ==========

def generate_all():
    import os
    os.makedirs('svg', exist_ok=True)

    slides = [
        # 001-003: 인트로
        slide_001, slide_002, slide_003,
        # 004-015: Fine-tuning 기초
        slide_004, slide_005, slide_006, slide_007, slide_008,
        slide_009, slide_010, slide_011, slide_012, slide_013,
        slide_014, slide_015,
        # 016-030: RAFT 데이터
        slide_016, slide_017, slide_018, slide_019, slide_020,
        slide_021, slide_022, slide_023, slide_024, slide_025,
        slide_026, slide_027, slide_028, slide_029, slide_030,
        # 031-036: 데이터 품질 & 검증 (기존 051-056)
        slide_051, slide_052, slide_053, slide_054, slide_055, slide_056,
        # 037-048: 학습 이론 (기존 031-042)
        slide_031, slide_032, slide_033, slide_034, slide_035,
        slide_036, slide_037, slide_038, slide_039, slide_040,
        slide_041, slide_042,
        # 049-052: 고급 학습 기법 (기존 057-060)
        slide_057, slide_058, slide_059, slide_060,
        # 053-060: 평가 방법 (기존 043-050)
        slide_043, slide_044, slide_045, slide_046, slide_047,
        slide_048, slide_049, slide_050,
        # 061-062: 실전 & 배포
        slide_061, slide_062
    ]

    for i, func in enumerate(slides, 1):
        with open(f'svg/slide_{i:03d}.svg', 'w', encoding='utf-8') as f:
            f.write(func())
        print(f'✓ slide_{i:03d}.svg')

    print(f'\n🎉 이론 중심 62 슬라이드 완성!')

if __name__ == '__main__':
    generate_all()
