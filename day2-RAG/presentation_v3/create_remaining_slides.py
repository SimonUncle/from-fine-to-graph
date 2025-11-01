#!/usr/bin/env python3
"""Generate remaining slides (031-038)"""

slides = {
    "031": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad031" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a8edea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fed6e3;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow031"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad031)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.5"/>
    <text x="100" y="35" font-size="24" fill="#333" text-anchor="middle" font-weight="bold">Part 5</text>
  </g>
  <text x="960" y="140" font-size="56" fill="#333" text-anchor="middle" font-weight="bold">Modular RAG 아키텍처 🏗️</text>
  <text x="960" y="200" font-size="32" fill="#666" text-anchor="middle">Router + Self-RAG + CRAG 통합</text>
  <g transform="translate(300, 280)">
    <rect x="0" y="0" width="1320" height="650" rx="20" fill="white" opacity="0.95" filter="url(#shadow031)"/>
    <text x="660" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">통합 Modular RAG 플로우</text>
    <g transform="translate(150, 120)">
      <rect x="0" y="0" width="1000" height="80" rx="15" fill="#e3f2fd"/>
      <text x="500" y="50" font-size="28" fill="#1976d2" text-anchor="middle" font-weight="bold">1️⃣ Query Router: 질문 복잡도 판단</text>
    </g>
    <g transform="translate(400, 230)">
      <rect x="0" y="0" width="450" height="80" rx="15" fill="#f3e5f5"/>
      <text x="225" y="50" font-size="24" fill="#7b1fa2" text-anchor="middle" font-weight="bold">2️⃣ 검색 전략 선택</text>
    </g>
    <g transform="translate(150, 340)">
      <rect x="0" y="0" width="450" height="80" rx="15" fill="#fff3e0"/>
      <text x="225" y="50" font-size="24" fill="#e65100" text-anchor="middle" font-weight="bold">3️⃣ 초기 검색 & 답변</text>
    </g>
    <g transform="translate(650, 340)">
      <rect x="0" y="0" width="500" height="80" rx="15" fill="#e8f5e9"/>
      <text x="250" y="50" font-size="24" fill="#2e7d32" text-anchor="middle" font-weight="bold">4️⃣ Self-RAG: 품질 평가</text>
    </g>
    <g transform="translate(150, 450)">
      <rect x="0" y="0" width="1000" height="80" rx="15" fill="#fff9c4"/>
      <text x="500" y="50" font-size="24" fill="#f57f17" text-anchor="middle" font-weight="bold">5️⃣ CRAG: Correct / Ambiguous / Incorrect 분류</text>
    </g>
    <g transform="translate(350, 560)">
      <rect x="0" y="0" width="600" height="60" rx="15" fill="#4caf50"/>
      <text x="300" y="42" font-size="26" fill="white" text-anchor="middle" font-weight="bold">✅ 최종 답변 반환</text>
    </g>
  </g>
  <g transform="translate(200, 960)">
    <rect x="0" y="0" width="1520" height="80" rx="20" fill="#667eea" filter="url(#shadow031)"/>
    <text x="760" y="50" font-size="28" fill="white" text-anchor="middle" font-weight="bold">💡 Modular RAG = 여러 기법을 상황에 맞게 조합! (최고 정확도 85%+)</text>
  </g>
  <text x="960" y="1065" font-size="20" fill="#333" text-anchor="middle" opacity="0.8">Slide 31 / 38 | Part 5 완료! 🎯</text>
</svg>""",

    "032": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad032" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fbc2eb;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#a6c1ee;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow032"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad032)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.3"/>
    <text x="100" y="35" font-size="24" fill="white" text-anchor="middle" font-weight="bold">Part 6</text>
  </g>
  <text x="960" y="140" font-size="56" fill="white" text-anchor="middle" font-weight="bold">RAGAS 📊</text>
  <text x="960" y="200" font-size="32" fill="white" text-anchor="middle" opacity="0.9">RAG Assessment Score - RAG 성능 평가 지표</text>
  <g transform="translate(200, 270)">
    <rect x="0" y="0" width="1520" height="200" rx="20" fill="white" opacity="0.95" filter="url(#shadow032)"/>
    <text x="760" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">RAGAS란?</text>
    <text x="760" y="100" font-size="24" fill="#666" text-anchor="middle">RAG 시스템의 성능을 종합적으로 평가하는 프레임워크</text>
    <text x="760" y="140" font-size="22" fill="#999" text-anchor="middle">LLM 기반 자동 평가 (Ground Truth 일부 필요)</text>
  </g>
  <g transform="translate(200, 500)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="740" height="380" rx="20" fill="#e8f5e9" filter="url(#shadow032)"/>
      <text x="370" y="50" font-size="32" fill="#2e7d32" text-anchor="middle" font-weight="bold">답변 품질 측정</text>
      <g transform="translate(60, 100)">
        <rect x="0" y="0" width="620" height="110" rx="15" fill="#c8e6c9"/>
        <text x="310" y="35" font-size="26" fill="#1b5e20" text-anchor="middle" font-weight="bold">Faithfulness (충실성)</text>
        <text x="310" y="70" font-size="20" fill="#666" text-anchor="middle">답변이 검색 문서에만</text>
        <text x="310" y="100" font-size="20" fill="#666" text-anchor="middle">기반하는가? (환각 방지)</text>
        <rect x="0" y="130" width="620" height="110" rx="15" fill="#dcedc8"/>
        <text x="310" y="165" font-size="26" fill="#33691e" text-anchor="middle" font-weight="bold">Answer Relevancy</text>
        <text x="310" y="200" font-size="20" fill="#666" text-anchor="middle">답변이 질문과 관련있는가?</text>
        <text x="310" y="230" font-size="20" fill="#666" text-anchor="middle">(질문-답변 일치도)</text>
      </g>
    </g>
    <g transform="translate(780, 0)">
      <rect x="0" y="0" width="740" height="380" rx="20" fill="#e3f2fd" filter="url(#shadow032)"/>
      <text x="370" y="50" font-size="32" fill="#1976d2" text-anchor="middle" font-weight="bold">검색 품질 측정</text>
      <g transform="translate(60, 100)">
        <rect x="0" y="0" width="620" height="110" rx="15" fill="#bbdefb"/>
        <text x="310" y="35" font-size="26" fill="#0d47a1" text-anchor="middle" font-weight="bold">Context Precision (정밀도)</text>
        <text x="310" y="70" font-size="20" fill="#666" text-anchor="middle">검색된 문서가 실제로</text>
        <text x="310" y="100" font-size="20" fill="#666" text-anchor="middle">관련있는가? (노이즈 적음)</text>
        <rect x="0" y="130" width="620" height="110" rx="15" fill="#90caf9"/>
        <text x="310" y="165" font-size="26" fill="#01579b" text-anchor="middle" font-weight="bold">Context Recall (재현율)</text>
        <text x="310" y="200" font-size="20" fill="#666" text-anchor="middle">필요한 문서를 모두</text>
        <text x="310" y="230" font-size="20" fill="#666" text-anchor="middle">찾았는가? (누락 없음)</text>
      </g>
    </g>
  </g>
  <g transform="translate(200, 910)">
    <rect x="0" y="0" width="1520" height="110" rx="20" fill="#263238" filter="url(#shadow032)"/>
    <text x="760" y="40" font-size="28" fill="#81c784" text-anchor="middle" font-weight="bold">💡 RAGAS Score (0~1)</text>
    <text x="760" y="80" font-size="24" fill="#e0e0e0" text-anchor="middle">= (Faithfulness + Answer Relevancy + Context Precision + Context Recall) / 4</text>
  </g>
  <text x="960" y="1065" font-size="20" fill="white" text-anchor="middle" opacity="0.8">Slide 32 / 38</text>
</svg>""",

    "033": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad033" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fa709a;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fee140;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow033"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad033)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.3"/>
    <text x="100" y="35" font-size="24" fill="white" text-anchor="middle" font-weight="bold">Part 6</text>
  </g>
  <text x="960" y="140" font-size="56" fill="white" text-anchor="middle" font-weight="bold">Faithfulness & Answer Relevancy 📝</text>
  <text x="960" y="200" font-size="32" fill="white" text-anchor="middle" opacity="0.9">답변 품질 지표</text>
  <g transform="translate(150, 270)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="810" height="600" rx="20" fill="white" opacity="0.95" filter="url(#shadow033)"/>
      <text x="405" y="50" font-size="32" fill="#2e7d32" text-anchor="middle" font-weight="bold">Faithfulness (충실성)</text>
      <g transform="translate(60, 100)">
        <text x="0" y="0" font-size="24" fill="#333" font-weight="bold">측정 방법:</text>
        <text x="0" y="40" font-size="22" fill="#666">LLM에게 물음:</text>
        <rect x="0" y="60" width="690" height="90" rx="10" fill="#e8f5e9"/>
        <text x="345" y="90" font-size="20" fill="#666" text-anchor="middle">"이 답변의 각 문장이</text>
        <text x="345" y="120" font-size="20" fill="#666" text-anchor="middle">검색 문서에 근거하는가?"</text>
        <text x="0" y="180" font-size="24" fill="#333" font-weight="bold">예시:</text>
        <rect x="0" y="200" width="690" height="160" rx="10" fill="#fff9c4"/>
        <g transform="translate(20, 225)">
          <text x="0" y="0" font-size="20" fill="#666">질문: 김치찌개 레시피?</text>
          <text x="0" y="35" font-size="20" fill="#2e7d32">✓ "김치와 돼지고기를 넣고</text>
          <text x="0" y="60" font-size="20" fill="#2e7d32">   20분 끓이세요" (문서 기반)</text>
          <text x="0" y="95" font-size="20" fill="#c62828">✗ "마늘 5개 필수" (문서 없음)</text>
          <text x="0" y="125" font-size="18" fill="#666">→ Faithfulness: 0.75 (3/4)</text>
        </g>
      </g>
    </g>
    <g transform="translate(860, 0)">
      <rect x="0" y="0" width="810" height="600" rx="20" fill="white" opacity="0.95" filter="url(#shadow033)"/>
      <text x="405" y="50" font-size="32" fill="#1976d2" text-anchor="middle" font-weight="bold">Answer Relevancy</text>
      <g transform="translate(60, 100)">
        <text x="0" y="0" font-size="24" fill="#333" font-weight="bold">측정 방법:</text>
        <text x="0" y="40" font-size="22" fill="#666">LLM에게 물음:</text>
        <rect x="0" y="60" width="690" height="90" rx="10" fill="#e3f2fd"/>
        <text x="345" y="90" font-size="20" fill="#666" text-anchor="middle">"이 답변이 질문에</text>
        <text x="345" y="120" font-size="20" fill="#666" text-anchor="middle">직접적으로 답하는가?"</text>
        <text x="0" y="180" font-size="24" fill="#333" font-weight="bold">예시:</text>
        <rect x="0" y="200" width="690" height="160" rx="10" fill="#fff9c4"/>
        <g transform="translate(20, 225)">
          <text x="0" y="0" font-size="20" fill="#666">질문: 김치찌개 조리 시간?</text>
          <text x="0" y="35" font-size="20" fill="#2e7d32">✓ "20분 끓이세요" (직접 답변)</text>
          <text x="0" y="70" font-size="20" fill="#c62828">✗ "김치찌개는 한국 음식이고</text>
          <text x="0" y="95" font-size="20" fill="#c62828">   다양한 재료가..." (관계없음)</text>
          <text x="0" y="125" font-size="18" fill="#666">→ Answer Relevancy: 0.9</text>
        </g>
      </g>
    </g>
  </g>
  <g transform="translate(150, 900)">
    <rect x="0" y="0" width="1620" height="120" rx="20" fill="#4caf50" filter="url(#shadow033)"/>
    <text x="810" y="45" font-size="32" fill="white" text-anchor="middle" font-weight="bold">💡 둘 다 LLM 기반 자동 평가!</text>
    <text x="810" y="85" font-size="26" fill="white" text-anchor="middle">Faithfulness는 환각 방지, Answer Relevancy는 질문-답변 일치도</text>
  </g>
  <text x="960" y="1065" font-size="20" fill="white" text-anchor="middle" opacity="0.8">Slide 33 / 38</text>
</svg>""",

    "034": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad034" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow034"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad034)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.3"/>
    <text x="100" y="35" font-size="24" fill="white" text-anchor="middle" font-weight="bold">Part 6</text>
  </g>
  <text x="960" y="140" font-size="56" fill="white" text-anchor="middle" font-weight="bold">Context Precision & Recall 🎯</text>
  <text x="960" y="200" font-size="32" fill="white" text-anchor="middle" opacity="0.9">검색 품질 지표 (Ground Truth 필요)</text>
  <g transform="translate(150, 270)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="810" height="600" rx="20" fill="white" opacity="0.95" filter="url(#shadow034)"/>
      <text x="405" y="50" font-size="32" fill="#e65100" text-anchor="middle" font-weight="bold">Context Precision (정밀도)</text>
      <g transform="translate(60, 100)">
        <text x="0" y="0" font-size="24" fill="#333" font-weight="bold">측정 방법:</text>
        <rect x="0" y="30" width="690" height="90" rx="10" fill="#fff3e0"/>
        <text x="345" y="60" font-size="22" fill="#666" text-anchor="middle">검색된 문서 중 실제 관련있는</text>
        <text x="345" y="90" font-size="22" fill="#666" text-anchor="middle">문서 비율 (Cosine ≥ threshold)</text>
        <text x="0" y="150" font-size="24" fill="#333" font-weight="bold">예시:</text>
        <rect x="0" y="170" width="690" height="200" rx="10" fill="#fff9c4"/>
        <g transform="translate(20, 195)">
          <text x="0" y="0" font-size="20" fill="#666">질문: "김치찌개 레시피"</text>
          <text x="0" y="35" font-size="20" fill="#666">검색된 Top-5:</text>
          <text x="20" y="65" font-size="18" fill="#2e7d32">✓ 김치찌개 레시피 (0.92)</text>
          <text x="20" y="95" font-size="18" fill="#2e7d32">✓ 백종원 김치찌개 (0.88)</text>
          <text x="20" y="125" font-size="18" fill="#c62828">✗ 조리 용어 사전 (0.25)</text>
          <text x="0" y="160" font-size="18" fill="#666">→ Precision: 0.67 (4/6 관련)</text>
        </g>
      </g>
    </g>
    <g transform="translate(860, 0)">
      <rect x="0" y="0" width="810" height="600" rx="20" fill="white" opacity="0.95" filter="url(#shadow034)"/>
      <text x="405" y="50" font-size="32" fill="#1976d2" text-anchor="middle" font-weight="bold">Context Recall (재현율)</text>
      <g transform="translate(60, 100)">
        <text x="0" y="0" font-size="24" fill="#333" font-weight="bold">측정 방법:</text>
        <rect x="0" y="30" width="690" height="90" rx="10" fill="#e3f2fd"/>
        <text x="345" y="60" font-size="22" fill="#666" text-anchor="middle">필요한 문서(Ground Truth) 중</text>
        <text x="345" y="90" font-size="22" fill="#666" text-anchor="middle">실제 찾은 문서 비율</text>
        <text x="0" y="150" font-size="24" fill="#333" font-weight="bold">예시:</text>
        <rect x="0" y="170" width="690" height="200" rx="10" fill="#fff9c4"/>
        <g transform="translate(20, 195)">
          <text x="0" y="0" font-size="20" fill="#666">필요한 문서 (Ground Truth):</text>
          <text x="20" y="30" font-size="18" fill="#666">• 김치찌개 레시피</text>
          <text x="20" y="55" font-size="18" fill="#666">• 백종원 김치찌개</text>
          <text x="20" y="80" font-size="18" fill="#666">• 흑백요리사 김치찌개</text>
          <text x="0" y="115" font-size="20" fill="#666">실제 찾은 것: 2개</text>
          <text x="0" y="150" font-size="18" fill="#666">→ Recall: 0.67 (2/3)</text>
        </g>
      </g>
    </g>
  </g>
  <g transform="translate(150, 900)">
    <rect x="0" y="0" width="1620" height="120" rx="20" fill="#263238" filter="url(#shadow034)"/>
    <text x="810" y="45" font-size="32" fill="#81c784" text-anchor="middle" font-weight="bold">💡 Precision과 Recall 둘 다 중요!</text>
    <g transform="translate(200, 75)">
      <text x="0" y="0" font-size="24" fill="#e0e0e0">Precision 높음 = 노이즈 적음 (정확)</text>
      <text x="800" y="0" font-size="24" fill="#e0e0e0">Recall 높음 = 누락 적음 (완전)</text>
    </g>
  </g>
  <text x="960" y="1065" font-size="20" fill="white" text-anchor="middle" opacity="0.8">Slide 34 / 38</text>
</svg>""",

    "035": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad035" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#c1dfc4;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#deecdd;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow035"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad035)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.5"/>
    <text x="100" y="35" font-size="24" fill="#2e7d32" text-anchor="middle" font-weight="bold">Part 6</text>
  </g>
  <text x="960" y="140" font-size="56" fill="#2e7d32" text-anchor="middle" font-weight="bold">Tuning 파라미터 ⚙️</text>
  <text x="960" y="200" font-size="32" fill="#558b2f" text-anchor="middle">성능 최적화를 위한 3대 파라미터</text>
  <g transform="translate(200, 270)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="490" height="580" rx="20" fill="white" opacity="0.95" filter="url(#shadow035)"/>
      <text x="245" y="50" font-size="32" fill="#1976d2" text-anchor="middle" font-weight="bold">chunk_size</text>
      <text x="245" y="90" font-size="24" fill="#666" text-anchor="middle">청크 크기</text>
      <g transform="translate(40, 130)">
        <rect x="0" y="0" width="410" height="80" rx="10" fill="#e3f2fd"/>
        <text x="205" y="30" font-size="22" fill="#333" text-anchor="middle" font-weight="bold">권장 범위</text>
        <text x="205" y="60" font-size="24" fill="#1976d2" text-anchor="middle" font-weight="bold">200 ~ 500 글자</text>
        <text x="0" y="120" font-size="22" fill="#666" font-weight="bold">효과:</text>
        <text x="0" y="155" font-size="20" fill="#666">• 작을수록: 정확도 ↑</text>
        <text x="0" y="190" font-size="20" fill="#666">  (의미 명확, 노이즈 ↓)</text>
        <text x="0" y="235" font-size="20" fill="#666">• 클수록: 문맥 ↑</text>
        <text x="0" y="270" font-size="20" fill="#666">  (정보 완전)</text>
        <rect x="0" y="310" width="410" height="90" rx="10" fill="#fff9c4"/>
        <text x="205" y="345" font-size="20" fill="#f57f17" text-anchor="middle" font-weight="bold">💡 Best Practice</text>
        <text x="205" y="375" font-size="18" fill="#666" text-anchor="middle">300~400 글자 + overlap</text>
      </g>
    </g>
    <g transform="translate(515, 0)">
      <rect x="0" y="0" width="490" height="580" rx="20" fill="white" opacity="0.95" filter="url(#shadow035)"/>
      <text x="245" y="50" font-size="32" fill="#7b1fa2" text-anchor="middle" font-weight="bold">top_k</text>
      <text x="245" y="90" font-size="24" fill="#666" text-anchor="middle">검색 문서 개수</text>
      <g transform="translate(40, 130)">
        <rect x="0" y="0" width="410" height="80" rx="10" fill="#f3e5f5"/>
        <text x="205" y="30" font-size="22" fill="#333" text-anchor="middle" font-weight="bold">권장 범위</text>
        <text x="205" y="60" font-size="24" fill="#7b1fa2" text-anchor="middle" font-weight="bold">3 ~ 10 개</text>
        <text x="0" y="120" font-size="22" fill="#666" font-weight="bold">효과:</text>
        <text x="0" y="155" font-size="20" fill="#666">• 적을수록: 정확도 ↑</text>
        <text x="0" y="190" font-size="20" fill="#666">  (관련 문서만)</text>
        <text x="0" y="235" font-size="20" fill="#666">• 많을수록: Recall ↑</text>
        <text x="0" y="270" font-size="20" fill="#666">  (누락 방지)</text>
        <rect x="0" y="310" width="410" height="90" rx="10" fill="#fff9c4"/>
        <text x="205" y="345" font-size="20" fill="#f57f17" text-anchor="middle" font-weight="bold">💡 Best Practice</text>
        <text x="205" y="375" font-size="18" fill="#666" text-anchor="middle">5개 (Naive) / 10개 (Rerank)</text>
      </g>
    </g>
    <g transform="translate(1030, 0)">
      <rect x="0" y="0" width="490" height="580" rx="20" fill="white" opacity="0.95" filter="url(#shadow035)"/>
      <text x="245" y="50" font-size="32" fill="#e65100" text-anchor="middle" font-weight="bold">threshold</text>
      <text x="245" y="90" font-size="24" fill="#666" text-anchor="middle">유사도 임계값</text>
      <g transform="translate(40, 130)">
        <rect x="0" y="0" width="410" height="80" rx="10" fill="#fff3e0"/>
        <text x="205" y="30" font-size="22" fill="#333" text-anchor="middle" font-weight="bold">권장 범위</text>
        <text x="205" y="60" font-size="24" fill="#e65100" text-anchor="middle" font-weight="bold">0.3 ~ 0.7</text>
        <text x="0" y="120" font-size="22" fill="#666" font-weight="bold">효과:</text>
        <text x="0" y="155" font-size="20" fill="#666">• 높을수록: 정확도 ↑</text>
        <text x="0" y="190" font-size="20" fill="#666">  (엄격 필터링)</text>
        <text x="0" y="235" font-size="20" fill="#666">• 낮을수록: Recall ↑</text>
        <text x="0" y="270" font-size="20" fill="#666">  (더 많이 검색)</text>
        <rect x="0" y="310" width="410" height="90" rx="10" fill="#fff9c4"/>
        <text x="205" y="345" font-size="20" fill="#f57f17" text-anchor="middle" font-weight="bold">💡 Best Practice</text>
        <text x="205" y="375" font-size="18" fill="#666" text-anchor="middle">0.5~0.6 (균형있게)</text>
      </g>
    </g>
  </g>
  <g transform="translate(200, 880)">
    <rect x="0" y="0" width="1520" height="140" rx="20" fill="#4caf50" filter="url(#shadow035)"/>
    <text x="760" y="45" font-size="32" fill="white" text-anchor="middle" font-weight="bold">💡 파라미터 튜닝 팁</text>
    <g transform="translate(100, 75)">
      <text x="0" y="0" font-size="24" fill="white">1️⃣ chunk_size: 300-400으로 시작 → RAGAS로 측정 → 조정</text>
      <text x="0" y="40" font-size="24" fill="white">2️⃣ top_k: 5개 → 성능 안나오면 10개 (Reranking 필수)</text>
    </g>
  </g>
  <text x="960" y="1065" font-size="20" fill="#2e7d32" text-anchor="middle" opacity="0.8">Slide 35 / 38 | Part 6 완료! 🎯</text>
</svg>"""
}

# Write slides 031-035
import os
svg_dir = "/Users/gim-yujin/workspace/lecture_cj/day2-RAG/presentation_v3/svg"
for slide_num, svg_content in slides.items():
    filepath = os.path.join(svg_dir, f"slide_{slide_num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Created slide_{slide_num}.svg")

print(f"\nCreated {len(slides)} slides (031-035)")
