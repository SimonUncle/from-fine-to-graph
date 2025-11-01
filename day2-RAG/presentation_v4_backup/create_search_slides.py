#!/usr/bin/env python3
"""검색 개선 슬라이드 (018-020)"""

slides = {
    "018": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg18" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh18"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg18)"/>
  <text x="960" y="120" font-size="64" fill="white" text-anchor="middle" font-weight="bold">BM25 🔤</text>
  <text x="960" y="190" font-size="32" fill="white" text-anchor="middle" opacity="0.9">키워드 빈도로 점수 매기기</text>
  <g transform="translate(200,260)">
    <rect width="1520" height="200" rx="20" fill="white" opacity="0.95" filter="url(#sh18)"/>
    <text x="760" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">BM25 = Best Matching 25</text>
    <text x="760" y="100" font-size="26" fill="#666" text-anchor="middle">단어 빈도(TF) + 문서 희소성(IDF) 고려</text>
    <text x="760" y="145" font-size="24" fill="#999" text-anchor="middle">문서에 키워드가 많이 등장 + 희귀한 단어 → 높은 점수</text>
  </g>
  <g transform="translate(150,510)">
    <rect width="780" height="420" rx="20" fill="white" opacity="0.95" filter="url(#sh18)"/>
    <text x="390" y="50" font-size="28" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ 장점</text>
    <g transform="translate(60,100)">
      <text x="0" y="0" font-size="24" fill="#666">• <tspan font-weight="bold">정확한 키워드 매칭</tspan></text>
      <text x="0" y="50" font-size="24" fill="#666">  "김치찌개" 정확히 포함된</text>
      <text x="0" y="85" font-size="24" fill="#666">  문서 우선 선택</text>
      <text x="0" y="140" font-size="24" fill="#666">• <tspan font-weight="bold">빠른 속도</tspan></text>
      <text x="0" y="190" font-size="24" fill="#666">  인덱스 기반 검색</text>
      <text x="0" y="240" font-size="24" fill="#666">• <tspan font-weight="bold">구현 간단</tspan></text>
      <text x="0" y="290" font-size="24" fill="#666">  전통적이고 검증됨</text>
    </g>
  </g>
  <g transform="translate(990,510)">
    <rect width="780" height="420" rx="20" fill="white" opacity="0.95" filter="url(#sh18)"/>
    <text x="390" y="50" font-size="28" fill="#c62828" text-anchor="middle" font-weight="bold">❌ 단점</text>
    <g transform="translate(60,100)">
      <text x="0" y="0" font-size="24" fill="#666">• <tspan font-weight="bold">의미 이해 불가</tspan></text>
      <text x="0" y="50" font-size="24" fill="#666">  "만드는 법" ≠ "레시피"</text>
      <text x="0" y="85" font-size="24" fill="#666">  (동의어 인식 안됨)</text>
      <text x="0" y="140" font-size="24" fill="#666">• <tspan font-weight="bold">표현 변화에 약함</tspan></text>
      <text x="0" y="190" font-size="24" fill="#666">  질문과 문서의 단어가</text>
      <text x="0" y="225" font-size="24" fill="#666">  다르면 검색 실패</text>
      <rect x="-20" y="270" width="660" height="90" rx="15" fill="#e3f2fd"/>
      <text x="310" y="310" font-size="22" fill="#1976d2" text-anchor="middle" font-weight="bold">💡 해결책</text>
      <text x="310" y="345" font-size="20" fill="#666" text-anchor="middle">Vector Search와 조합!</text>
    </g>
  </g>
</svg>""",

    "019": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg19" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh19"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg19)"/>
  <text x="960" y="120" font-size="64" fill="white" text-anchor="middle" font-weight="bold">Hybrid Search 🔀</text>
  <text x="960" y="190" font-size="32" fill="white" text-anchor="middle" opacity="0.9">Vector + BM25 장점 결합</text>
  <g transform="translate(250,260)">
    <rect width="420" height="220" rx="20" fill="white" opacity="0.95" filter="url(#sh19)"/>
    <text x="210" y="50" font-size="28" fill="#1976d2" text-anchor="middle" font-weight="bold">Vector Search</text>
    <circle cx="210" cy="110" r="40" fill="#1976d2"/>
    <text x="210" y="123" font-size="28" fill="white" text-anchor="middle">🔍</text>
    <text x="210" y="180" font-size="22" fill="#666" text-anchor="middle">의미 이해</text>
  </g>
  <g transform="translate(750,320)">
    <text x="0" y="0" font-size="48" fill="white" text-anchor="middle" font-weight="bold">+</text>
  </g>
  <g transform="translate(900,260)">
    <rect width="420" height="220" rx="20" fill="white" opacity="0.95" filter="url(#sh19)"/>
    <text x="210" y="50" font-size="28" fill="#e65100" text-anchor="middle" font-weight="bold">BM25 Search</text>
    <circle cx="210" cy="110" r="40" fill="#e65100"/>
    <text x="210" y="123" font-size="28" fill="white" text-anchor="middle">🔤</text>
    <text x="210" y="180" font-size="22" fill="#666" text-anchor="middle">키워드 정확성</text>
  </g>
  <g transform="translate(1400,320)">
    <text x="0" y="0" font-size="48" fill="white" text-anchor="middle" font-weight="bold">=</text>
  </g>
  <g transform="translate(1500,260)">
    <rect width="320" height="220" rx="20" fill="#4caf50" filter="url(#sh19)"/>
    <text x="160" y="50" font-size="28" fill="white" text-anchor="middle" font-weight="bold">Hybrid</text>
    <circle cx="160" cy="110" r="40" fill="white" opacity="0.3"/>
    <text x="160" y="123" font-size="28" fill="white" text-anchor="middle">💚</text>
    <text x="160" y="180" font-size="22" fill="white" text-anchor="middle">둘 다!</text>
  </g>
  <g transform="translate(200,550)">
    <rect width="1520" height="400" rx="20" fill="white" opacity="0.95" filter="url(#sh19)"/>
    <text x="760" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">🔄 Hybrid Search 작동 방식</text>
    <g transform="translate(100,110)">
      <circle cx="30" cy="20" r="25" fill="#1976d2"/>
      <text x="30" y="28" font-size="20" fill="white" text-anchor="middle" font-weight="bold">1</text>
      <text x="80" y="28" font-size="24" fill="#666">Vector Search 실행 → Top-10 추출</text>
      <circle cx="30" cy="85" r="25" fill="#e65100"/>
      <text x="30" y="93" font-size="20" fill="white" text-anchor="middle" font-weight="bold">2</text>
      <text x="80" y="93" font-size="24" fill="#666">BM25 Search 실행 → Top-10 추출</text>
      <circle cx="30" cy="150" r="25" fill="#7b1fa2"/>
      <text x="30" y="158" font-size="20" fill="white" text-anchor="middle" font-weight="bold">3</text>
      <text x="80" y="158" font-size="24" fill="#666">RRF로 두 결과 합치기 (순위 기반 통합)</text>
      <rect x="0" y="200" width="1320" height="150" rx="15" fill="#e8f5e9"/>
      <text x="660" y="245" font-size="28" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ 결과</text>
      <text x="660" y="285" font-size="24" fill="#666" text-anchor="middle">의미도 잡고, 키워드도 잡는 강력한 검색!</text>
      <text x="660" y="325" font-size="22" fill="#999" text-anchor="middle">Naive RAG 대비 정확도 +15-20% 향상</text>
    </g>
  </g>
</svg>""",

    "020": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg20" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ffecd2;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#fcb69f;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh20"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg20)"/>
  <text x="960" y="120" font-size="64" fill="#d84315" text-anchor="middle" font-weight="bold">Cross-Encoder Reranking 🥇</text>
  <text x="960" y="190" font-size="32" fill="#e64a19" text-anchor="middle">2단계 검색: 빠른 선별 → 정밀 평가</text>
  <g transform="translate(200,260)">
    <rect width="1520" height="600" rx="20" fill="white" opacity="0.95" filter="url(#sh20)"/>
    <text x="760" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">🎯 2단계 Retrieval 전략</text>
    <g transform="translate(100,110)">
      <rect width="620" height="400" rx="15" fill="#e3f2fd"/>
      <text x="310" y="40" font-size="28" fill="#1976d2" text-anchor="middle" font-weight="bold">Stage 1: Bi-Encoder</text>
      <text x="310" y="75" font-size="22" fill="#666" text-anchor="middle">(1차 서류 심사)</text>
      <circle cx="310" cy="150" r="50" fill="#1976d2"/>
      <text x="310" y="165" font-size="32" fill="white" text-anchor="middle">🏃</text>
      <g transform="translate(60,220)">
        <text x="0" y="0" font-size="22" fill="#666">✓ 빠른 속도</text>
        <text x="0" y="40" font-size="22" fill="#666">✓ 대량 문서 처리</text>
        <text x="0" y="80" font-size="22" fill="#666">✓ 정확도: 중간</text>
        <text x="0" y="130" font-size="24" fill="#1976d2" font-weight="bold">→ Top-100 추출</text>
      </g>
    </g>
    <g transform="translate(800,110)">
      <rect width="620" height="400" rx="15" fill="#fff3e0"/>
      <text x="310" y="40" font-size="28" fill="#e65100" text-anchor="middle" font-weight="bold">Stage 2: Cross-Encoder</text>
      <text x="310" y="75" font-size="22" fill="#666" text-anchor="middle">(2차 심층 면접)</text>
      <circle cx="310" cy="150" r="50" fill="#e65100"/>
      <text x="310" y="165" font-size="32" fill="white" text-anchor="middle">🎯</text>
      <g transform="translate(60,220)">
        <text x="0" y="0" font-size="22" fill="#666">✓ 느린 속도</text>
        <text x="0" y="40" font-size="22" fill="#666">✓ 정밀 평가</text>
        <text x="0" y="80" font-size="22" fill="#666">✓ 정확도: 매우 높음</text>
        <text x="0" y="130" font-size="24" fill="#e65100" font-weight="bold">→ Top-5 최종 선택</text>
      </g>
    </g>
  </g>
  <g transform="translate(200,900)">
    <rect width="1520" height="130" rx="20" fill="#4caf50" filter="url(#sh20)"/>
    <text x="760" y="45" font-size="32" fill="white" text-anchor="middle" font-weight="bold">💡 왜 2단계?</text>
    <text x="760" y="90" font-size="26" fill="white" text-anchor="middle">Cross-Encoder는 느려서 전체 문서에 쓸 수 없음!</text>
  </g>
</svg>"""
}

import os
svg_dir = "/Users/gim-yujin/workspace/lecture_cj/day2-RAG/presentation_v4/svg"
for slide_num, content in slides.items():
    with open(os.path.join(svg_dir, f"slide_{slide_num}.svg"), 'w') as f:
        f.write(content)
    print(f"Created slide_{slide_num}.svg")
print(f"\n✅ Created {len(slides)} slides (018-020)")
