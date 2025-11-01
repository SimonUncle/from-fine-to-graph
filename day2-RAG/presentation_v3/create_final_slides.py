#!/usr/bin/env python3
"""Generate final 11 slides (028-038) for presentation_v3"""

slides = {
    "028": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad028" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow028"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad028)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.3"/>
    <text x="100" y="35" font-size="24" fill="white" text-anchor="middle" font-weight="bold">Part 5</text>
  </g>
  <text x="960" y="140" font-size="56" fill="white" text-anchor="middle" font-weight="bold">Query Router 🚦</text>
  <text x="960" y="200" font-size="32" fill="white" text-anchor="middle" opacity="0.9">간단한 질문 vs 복잡한 질문 분류</text>
  <g transform="translate(200, 280)">
    <rect x="0" y="0" width="1520" height="200" rx="20" fill="white" opacity="0.95" filter="url(#shadow028)"/>
    <text x="760" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">Query Router 개념</text>
    <text x="760" y="100" font-size="24" fill="#666" text-anchor="middle">질문의 복잡도를 판단하여 적절한 검색 전략 선택</text>
    <text x="760" y="140" font-size="22" fill="#999" text-anchor="middle">• 간단한 질문 → Naive RAG (빠름)</text>
    <text x="760" y="175" font-size="22" fill="#999" text-anchor="middle">• 복잡한 질문 → Advanced RAG (정확함)</text>
  </g>
  <g transform="translate(200, 510)">
    <rect x="0" y="0" width="1520" height="400" rx="20" fill="white" opacity="0.95" filter="url(#shadow028)"/>
    <g transform="translate(100, 70)">
      <rect x="0" y="0" width="620" height="280" rx="15" fill="#e8f5e9"/>
      <text x="310" y="40" font-size="28" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ 간단한 질문</text>
      <g transform="translate(40, 80)">
        <text x="0" y="0" font-size="22" fill="#666">"김치찌개 레시피 알려줘"</text>
        <text x="0" y="50" font-size="20" fill="#999">→ 단일 정보 요청</text>
        <text x="0" y="90" font-size="20" fill="#999">→ 명확한 의도</text>
        <rect x="-20" y="120" width="580" height="60" rx="10" fill="#c8e6c9"/>
        <text x="270" y="160" font-size="22" fill="#2e7d32" text-anchor="middle" font-weight="bold">→ Naive RAG (0.5초)</text>
      </g>
    </g>
    <g transform="translate(800, 70)">
      <rect x="0" y="0" width="620" height="280" rx="15" fill="#ffebee"/>
      <text x="310" y="40" font-size="28" fill="#c62828" text-anchor="middle" font-weight="bold">⚠️ 복잡한 질문</text>
      <g transform="translate(40, 80)">
        <text x="0" y="0" font-size="22" fill="#666">"김치찌개를 맛있게 만드는</text>
        <text x="0" y="30" font-size="22" fill="#666">재료와 조리 시간은?"</text>
        <text x="0" y="70" font-size="20" fill="#999">→ 다중 정보 요청</text>
        <rect x="-20" y="100" width="580" height="60" rx="10" fill="#ffcdd2"/>
        <text x="270" y="140" font-size="22" fill="#c62828" text-anchor="middle" font-weight="bold">→ Sub-Q + Hybrid (2초)</text>
      </g>
    </g>
  </g>
  <g transform="translate(200, 940)">
    <rect x="0" y="0" width="1520" height="80" rx="20" fill="#4caf50" filter="url(#shadow028)"/>
    <text x="760" y="50" font-size="28" fill="white" text-anchor="middle" font-weight="bold">💡 적절한 전략 선택 = 속도 & 비용 최적화!</text>
  </g>
  <text x="960" y="1065" font-size="20" fill="white" text-anchor="middle" opacity="0.8">Slide 28 / 38</text>
</svg>""",

    "029": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad029" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ffecd2;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fcb69f;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow029"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad029)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.5"/>
    <text x="100" y="35" font-size="24" fill="#d84315" text-anchor="middle" font-weight="bold">Part 5</text>
  </g>
  <text x="960" y="140" font-size="56" fill="#d84315" text-anchor="middle" font-weight="bold">Self-RAG 🔍</text>
  <text x="960" y="200" font-size="32" fill="#e64a19" text-anchor="middle">답변 품질 자가 평가 후 재검색 결정</text>
  <g transform="translate(200, 270)">
    <rect x="0" y="0" width="1520" height="650" rx="20" fill="white" opacity="0.95" filter="url(#shadow029)"/>
    <text x="760" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">Self-RAG 작동 흐름</text>
    <g transform="translate(150, 110)">
      <circle cx="40" cy="30" r="30" fill="#1976d2"/>
      <text x="40" y="40" font-size="24" fill="white" text-anchor="middle" font-weight="bold">1</text>
      <text x="100" y="40" font-size="24" fill="#666">질문 입력 → 초기 검색 및 답변 생성</text>
      <circle cx="40" cy="110" r="30" fill="#7b1fa2"/>
      <text x="40" y="120" font-size="24" fill="white" text-anchor="middle" font-weight="bold">2</text>
      <text x="100" y="120" font-size="24" fill="#666">LLM이 자신의 답변 품질 평가 (0-100 점수)</text>
      <g transform="translate(0, 160)">
        <rect x="0" y="0" width="600" height="80" rx="15" fill="#e8f5e9"/>
        <text x="300" y="30" font-size="22" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ 점수 ≥ 70: 답변 그대로 반환</text>
        <text x="300" y="60" font-size="20" fill="#666" text-anchor="middle">"충분히 정확합니다"</text>
      </g>
      <g transform="translate(650, 160)">
        <rect x="0" y="0" width="600" height="80" rx="15" fill="#ffebee"/>
        <text x="300" y="30" font-size="22" fill="#c62828" text-anchor="middle" font-weight="bold">❌ 점수 < 70: 재검색 실행</text>
        <text x="300" y="60" font-size="20" fill="#666" text-anchor="middle">"더 찾아보겠습니다"</text>
      </g>
      <circle cx="40" cy="330" r="30" fill="#e65100"/>
      <text x="40" y="340" font-size="24" fill="white" text-anchor="middle" font-weight="bold">3</text>
      <text x="100" y="340" font-size="24" fill="#666">재검색 시: Query Refinement 적용 (Multi-Query, HyDE)</text>
      <circle cx="40" cy="410" r="30" fill="#2e7d32"/>
      <text x="40" y="420" font-size="24" fill="white" text-anchor="middle" font-weight="bold">4</text>
      <text x="100" y="420" font-size="24" fill="#666">새 문서로 답변 재생성 → 최종 답변 반환</text>
    </g>
  </g>
  <g transform="translate(200, 950)">
    <rect x="0" y="0" width="1520" height="80" rx="20" fill="#4caf50" filter="url(#shadow029)"/>
    <text x="760" y="50" font-size="28" fill="white" text-anchor="middle" font-weight="bold">💡 Self-RAG: "답변이 불확실하면 다시 찾아본다" (정확도 +5%)</text>
  </g>
  <text x="960" y="1065" font-size="20" fill="#d84315" text-anchor="middle" opacity="0.8">Slide 29 / 38</text>
</svg>""",

    "030": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad030" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow030"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad030)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.3"/>
    <text x="100" y="35" font-size="24" fill="white" text-anchor="middle" font-weight="bold">Part 5</text>
  </g>
  <text x="960" y="140" font-size="56" fill="white" text-anchor="middle" font-weight="bold">CRAG ⚖️</text>
  <text x="960" y="200" font-size="32" fill="white" text-anchor="middle" opacity="0.9">Corrective RAG - 3가지 액션으로 보정</text>
  <g transform="translate(150, 270)">
    <rect x="0" y="0" width="1620" height="630" rx="20" fill="white" opacity="0.95" filter="url(#shadow030)"/>
    <text x="810" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">CRAG: 문서 관련성 평가 후 액션 결정</text>
    <g transform="translate(100, 110)">
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="480" height="450" rx="15" fill="#e8f5e9"/>
        <text x="240" y="45" font-size="28" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ Correct</text>
        <text x="240" y="85" font-size="22" fill="#666" text-anchor="middle">(관련성 ≥ 0.8)</text>
        <g transform="translate(40, 120)">
          <text x="0" y="0" font-size="20" fill="#666">평가:</text>
          <text x="0" y="35" font-size="20" fill="#2e7d32" font-weight="bold">"문서가 매우 관련있음"</text>
          <text x="0" y="90" font-size="20" fill="#666">액션:</text>
          <text x="0" y="125" font-size="20" fill="#2e7d32" font-weight="bold">→ 그대로 사용</text>
          <text x="0" y="160" font-size="20" fill="#2e7d32" font-weight="bold">→ 답변 생성</text>
          <text x="0" y="220" font-size="18" fill="#999">예시: "김치찌개 레시피"</text>
          <text x="0" y="250" font-size="18" fill="#999">질문에 정확히 일치하는</text>
          <text x="0" y="280" font-size="18" fill="#999">레시피 문서 발견</text>
        </g>
      </g>
      <g transform="translate(520, 0)">
        <rect x="0" y="0" width="480" height="450" rx="15" fill="#fff9c4"/>
        <text x="240" y="45" font-size="28" fill="#f57f17" text-anchor="middle" font-weight="bold">❓ Ambiguous</text>
        <text x="240" y="85" font-size="22" fill="#666" text-anchor="middle">(0.5 ≤ 관련성 < 0.8)</text>
        <g transform="translate(40, 120)">
          <text x="0" y="0" font-size="20" fill="#666">평가:</text>
          <text x="0" y="35" font-size="20" fill="#f57f17" font-weight="bold">"애매함, 불확실"</text>
          <text x="0" y="90" font-size="20" fill="#666">액션:</text>
          <text x="0" y="125" font-size="20" fill="#f57f17" font-weight="bold">→ 웹 검색 추가</text>
          <text x="0" y="160" font-size="20" fill="#f57f17" font-weight="bold">→ 외부 지식 보충</text>
          <text x="0" y="220" font-size="18" fill="#999">예시: "최신 김치찌개</text>
          <text x="0" y="250" font-size="18" fill="#999">트렌드"</text>
          <text x="0" y="280" font-size="18" fill="#999">→ 웹에서 2025 레시피</text>
        </g>
      </g>
      <g transform="translate(1040, 0)">
        <rect x="0" y="0" width="480" height="450" rx="15" fill="#ffebee"/>
        <text x="240" y="45" font-size="28" fill="#c62828" text-anchor="middle" font-weight="bold">❌ Incorrect</text>
        <text x="240" y="85" font-size="22" fill="#666" text-anchor="middle">(관련성 < 0.5)</text>
        <g transform="translate(40, 120)">
          <text x="0" y="0" font-size="20" fill="#666">평가:</text>
          <text x="0" y="35" font-size="20" fill="#c62828" font-weight="bold">"완전히 무관함"</text>
          <text x="0" y="90" font-size="20" fill="#666">액션:</text>
          <text x="0" y="125" font-size="20" fill="#c62828" font-weight="bold">→ 재검색 (다른 전략)</text>
          <text x="0" y="160" font-size="20" fill="#c62828" font-weight="bold">→ 혹은 "모름" 반환</text>
          <text x="0" y="220" font-size="18" fill="#999">예시: "김치찌개" 질문에</text>
          <text x="0" y="250" font-size="18" fill="#999">"자동차 수리" 문서</text>
          <text x="0" y="280" font-size="18" fill="#999">→ 다시 검색 필요</text>
        </g>
      </g>
    </g>
  </g>
  <g transform="translate(150, 930)">
    <rect x="0" y="0" width="1620" height="80" rx="20" fill="#667eea" filter="url(#shadow030)"/>
    <text x="810" y="50" font-size="28" fill="white" text-anchor="middle" font-weight="bold">💡 CRAG: 문서 품질을 3단계로 평가하고 각각 다른 액션! (신뢰도 향상)</text>
  </g>
  <text x="960" y="1065" font-size="20" fill="white" text-anchor="middle" opacity="0.8">Slide 30 / 38</text>
</svg>"""
}

# Write all slides
import os
svg_dir = "/Users/gim-yujin/workspace/lecture_cj/day2-RAG/presentation_v3/svg"
for slide_num, svg_content in slides.items():
    filepath = os.path.join(svg_dir, f"slide_{slide_num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Created slide_{slide_num}.svg")

print(f"\nCreated {len(slides)} slides (028-030)")
