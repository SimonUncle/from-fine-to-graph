#!/usr/bin/env python3
"""마지막 슬라이드 (021-025)"""

slides = {
    "021": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg21" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#c1dfc4;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#deecdd;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh21"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg21)"/>
  <text x="960" y="120" font-size="64" fill="#2e7d32" text-anchor="middle" font-weight="bold">Query Router 🚦</text>
  <text x="960" y="190" font-size="32" fill="#558b2f" text-anchor="middle">질문 복잡도 판단하여 전략 선택</text>
  <g transform="translate(200,280)">
    <rect width="720" height="600" rx="20" fill="white" opacity="0.95" filter="url(#sh21)"/>
    <text x="360" y="50" font-size="28" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ 간단한 질문</text>
    <g transform="translate(60,100)">
      <rect width="600" height="100" rx="15" fill="#e8f5e9"/>
      <text x="300" y="35" font-size="22" fill="#333" text-anchor="middle">"김치찌개 레시피 알려줘"</text>
      <text x="300" y="70" font-size="20" fill="#666" text-anchor="middle">→ 단일 정보 요청, 명확함</text>
    </g>
    <text x="360" y="250" font-size="32" fill="#2e7d32" text-anchor="middle">⬇️</text>
    <rect x="80" y="280" width="560" height="120" rx="15" fill="#c8e6c9"/>
    <text x="360" y="325" font-size="24" fill="#1b5e20" text-anchor="middle" font-weight="bold">Naive RAG</text>
    <text x="360" y="360" font-size="20" fill="#666" text-anchor="middle">빠른 Vector Search</text>
    <text x="360" y="390" font-size="20" fill="#666" text-anchor="middle">0.5초 응답</text>
    <rect x="80" y="440" width="560" height="130" rx="15" fill="#fff3e0"/>
    <text x="360" y="480" font-size="22" fill="#e65100" text-anchor="middle" font-weight="bold">💰 비용 절감</text>
    <text x="360" y="515" font-size="20" fill="#666" text-anchor="middle">간단한 질문에 복잡한</text>
    <text x="360" y="545" font-size="20" fill="#666" text-anchor="middle">기법 쓸 필요 없음!</text>
  </g>
  <g transform="translate(1000,280)">
    <rect width="720" height="600" rx="20" fill="white" opacity="0.95" filter="url(#sh21)"/>
    <text x="360" y="50" font-size="28" fill="#c62828" text-anchor="middle" font-weight="bold">⚠️ 복잡한 질문</text>
    <g transform="translate(60,100)">
      <rect width="600" height="120" rx="15" fill="#ffebee"/>
      <text x="300" y="30" font-size="22" fill="#333" text-anchor="middle">"김치찌개를 맛있게 만드는</text>
      <text x="300" y="60" font-size="22" fill="#333" text-anchor="middle">재료와 조리 시간은?"</text>
      <text x="300" y="95" font-size="20" fill="#666" text-anchor="middle">→ 다중 정보, 애매함</text>
    </g>
    <text x="360" y="270" font-size="32" fill="#c62828" text-anchor="middle">⬇️</text>
    <rect x="80" y="300" width="560" height="120" rx="15" fill="#ffcdd2"/>
    <text x="360" y="345" font-size="24" fill="#c62828" text-anchor="middle" font-weight="bold">Advanced RAG</text>
    <text x="360" y="380" font-size="20" fill="#666" text-anchor="middle">Sub-Q + Hybrid + Rerank</text>
    <text x="360" y="410" font-size="20" fill="#666" text-anchor="middle">2초 응답</text>
    <rect x="80" y="460" width="560" height="110" rx="15" fill="#e3f2fd"/>
    <text x="360" y="500" font-size="22" fill="#1976d2" text-anchor="middle" font-weight="bold">🎯 정확도 우선</text>
    <text x="360" y="535" font-size="20" fill="#666" text-anchor="middle">복잡한 질문엔 강력한 기법!</text>
  </g>
  <g transform="translate(200,920)">
    <rect width="1520" height="100" rx="20" fill="#667eea" filter="url(#sh21)"/>
    <text x="760" y="60" font-size="28" fill="white" text-anchor="middle" font-weight="bold">💡 적절한 전략 = 속도 & 비용 최적화!</text>
  </g>
</svg>""",

    "022": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg22" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a8edea;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#fed6e3;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh22"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg22)"/>
  <text x="960" y="120" font-size="64" fill="#333" text-anchor="middle" font-weight="bold">Self-RAG 🔍</text>
  <text x="960" y="190" font-size="32" fill="#666" text-anchor="middle">답변 품질 자가 평가 후 결정</text>
  <g transform="translate(300,280)">
    <rect width="1320" height="650" rx="20" fill="white" opacity="0.95" filter="url(#sh22)"/>
    <text x="660" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">Self-RAG 흐름</text>
    <g transform="translate(150,120)">
      <circle cx="30" cy="20" r="25" fill="#1976d2"/>
      <text x="30" y="28" font-size="20" fill="white" text-anchor="middle" font-weight="bold">1</text>
      <text x="80" y="28" font-size="24" fill="#666">질문 입력 → 초기 검색 & 답변 생성</text>
      <circle cx="30" cy="100" r="25" fill="#7b1fa2"/>
      <text x="30" y="108" font-size="20" fill="white" text-anchor="middle" font-weight="bold">2</text>
      <text x="80" y="108" font-size="24" fill="#666">LLM이 자신의 답변 품질 평가 (점수 부여)</text>
      <g transform="translate(0,160)">
        <rect width="500" height="100" rx="15" fill="#e8f5e9"/>
        <text x="250" y="35" font-size="22" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ 점수 높음 (확신)</text>
        <text x="250" y="70" font-size="20" fill="#666" text-anchor="middle">→ 답변 그대로 반환</text>
      </g>
      <g transform="translate(550,160)">
        <rect width="500" height="100" rx="15" fill="#ffebee"/>
        <text x="250" y="35" font-size="22" fill="#c62828" text-anchor="middle" font-weight="bold">❌ 점수 낮음 (불확실)</text>
        <text x="250" y="70" font-size="20" fill="#666" text-anchor="middle">→ 재검색 실행!</text>
      </g>
      <circle cx="30" cy="320" r="25" fill="#e65100"/>
      <text x="30" y="328" font-size="20" fill="white" text-anchor="middle" font-weight="bold">3</text>
      <text x="80" y="328" font-size="24" fill="#666">재검색 시: Query Refinement 적용 (Multi-Query)</text>
      <circle cx="30" cy="400" r="25" fill="#2e7d32"/>
      <text x="30" y="408" font-size="20" fill="white" text-anchor="middle" font-weight="bold">4</text>
      <text x="80" y="408" font-size="24" fill="#666">새 문서로 답변 재생성 → 최종 답변</text>
    </g>
  </g>
  <g transform="translate(300,970)">
    <rect width="1320" height="80" rx="20" fill="#4caf50" filter="url(#sh22)"/>
    <text x="660" y="52" font-size="28" fill="white" text-anchor="middle" font-weight="bold">💡 "답변이 불확실하면 다시 찾는다" → 정확도 향상!</text>
  </g>
</svg>""",

    "023": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg23" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fbc2eb;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#a6c1ee;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh23"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg23)"/>
  <text x="960" y="120" font-size="64" fill="white" text-anchor="middle" font-weight="bold">CRAG ⚖️</text>
  <text x="960" y="190" font-size="32" fill="white" text-anchor="middle" opacity="0.9">Corrective RAG - 3가지 액션</text>
  <g transform="translate(150,280)">
    <g transform="translate(0,0)">
      <rect width="520" height="530" rx="20" fill="white" opacity="0.95" filter="url(#sh23)"/>
      <text x="260" y="50" font-size="28" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ Correct</text>
      <text x="260" y="85" font-size="22" fill="#666" text-anchor="middle">(관련성 높음)</text>
      <g transform="translate(40,130)">
        <text x="0" y="0" font-size="22" fill="#666" font-weight="bold">평가:</text>
        <text x="0" y="40" font-size="20" fill="#2e7d32">"문서가 질문과</text>
        <text x="0" y="70" font-size="20" fill="#2e7d32">매우 관련있음"</text>
        <text x="0" y="130" font-size="22" fill="#666" font-weight="bold">액션:</text>
        <text x="0" y="170" font-size="20" fill="#666">→ 그대로 사용</text>
        <text x="0" y="200" font-size="20" fill="#666">→ 답변 생성</text>
        <rect x="-20" y="240" width="480" height="120" rx="15" fill="#e8f5e9"/>
        <text x="220" y="280" font-size="18" fill="#999" text-anchor="middle">예시:</text>
        <text x="220" y="310" font-size="18" fill="#999" text-anchor="middle">"김치찌개 레시피" 질문에</text>
        <text x="220" y="335" font-size="18" fill="#999" text-anchor="middle">김치찌개 문서 발견</text>
      </g>
    </g>
    <g transform="translate(580,0)">
      <rect width="520" height="530" rx="20" fill="white" opacity="0.95" filter="url(#sh23)"/>
      <text x="260" y="50" font-size="28" fill="#f57f17" text-anchor="middle" font-weight="bold">❓ Ambiguous</text>
      <text x="260" y="85" font-size="22" fill="#666" text-anchor="middle">(애매함)</text>
      <g transform="translate(40,130)">
        <text x="0" y="0" font-size="22" fill="#666" font-weight="bold">평가:</text>
        <text x="0" y="40" font-size="20" fill="#f57f17">"불확실함,</text>
        <text x="0" y="70" font-size="20" fill="#f57f17">더 필요할 수 있음"</text>
        <text x="0" y="130" font-size="22" fill="#666" font-weight="bold">액션:</text>
        <text x="0" y="170" font-size="20" fill="#666">→ 웹 검색 추가</text>
        <text x="0" y="200" font-size="20" fill="#666">→ 외부 지식 보충</text>
        <rect x="-20" y="240" width="480" height="120" rx="15" fill="#fff9c4"/>
        <text x="220" y="280" font-size="18" fill="#999" text-anchor="middle">예시:</text>
        <text x="220" y="310" font-size="18" fill="#999" text-anchor="middle">"최신 트렌드" 질문 →</text>
        <text x="220" y="335" font-size="18" fill="#999" text-anchor="middle">웹에서 추가 검색</text>
      </g>
    </g>
    <g transform="translate(1160,0)">
      <rect width="520" height="530" rx="20" fill="white" opacity="0.95" filter="url(#sh23)"/>
      <text x="260" y="50" font-size="28" fill="#c62828" text-anchor="middle" font-weight="bold">❌ Incorrect</text>
      <text x="260" y="85" font-size="22" fill="#666" text-anchor="middle">(무관함)</text>
      <g transform="translate(40,130)">
        <text x="0" y="0" font-size="22" fill="#666" font-weight="bold">평가:</text>
        <text x="0" y="40" font-size="20" fill="#c62828">"완전히 무관,</text>
        <text x="0" y="70" font-size="20" fill="#c62828">잘못된 문서"</text>
        <text x="0" y="130" font-size="22" fill="#666" font-weight="bold">액션:</text>
        <text x="0" y="170" font-size="20" fill="#666">→ 재검색</text>
        <text x="0" y="200" font-size="20" fill="#666">→ 또는 "모름" 반환</text>
        <rect x="-20" y="240" width="480" height="120" rx="15" fill="#ffebee"/>
        <text x="220" y="280" font-size="18" fill="#999" text-anchor="middle">예시:</text>
        <text x="220" y="310" font-size="18" fill="#999" text-anchor="middle">"김치찌개" 질문에</text>
        <text x="220" y="335" font-size="18" fill="#999" text-anchor="middle">"자동차" 문서 → 재검색</text>
      </g>
    </g>
  </g>
  <g transform="translate(150,850)">
    <rect width="1620" height="140" rx="20" fill="#667eea" filter="url(#sh23)"/>
    <text x="810" y="50" font-size="32" fill="white" text-anchor="middle" font-weight="bold">💡 CRAG: 문서 품질을 3단계로 평가하고 각각 다른 액션!</text>
    <text x="810" y="95" font-size="26" fill="white" text-anchor="middle">→ 신뢰도 향상, 불확실한 답변 방지</text>
  </g>
</svg>""",

    "024": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg24" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fa709a;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#fee140;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh24"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg24)"/>
  <text x="960" y="120" font-size="64" fill="white" text-anchor="middle" font-weight="bold">RAGAS 📊</text>
  <text x="960" y="190" font-size="32" fill="white" text-anchor="middle" opacity="0.9">RAG 성능 평가 프레임워크</text>
  <g transform="translate(200,280)">
    <rect width="1520" height="200" rx="20" fill="white" opacity="0.95" filter="url(#sh24)"/>
    <text x="760" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">RAGAS = RAG Assessment Score</text>
    <text x="760" y="100" font-size="26" fill="#666" text-anchor="middle">LLM 기반 자동 평가 지표 (4가지)</text>
    <text x="760" y="145" font-size="24" fill="#999" text-anchor="middle">답변 품질 2개 + 검색 품질 2개</text>
  </g>
  <g transform="translate(150,520)">
    <g transform="translate(0,0)">
      <rect width="780" height="380" rx="20" fill="white" opacity="0.95" filter="url(#sh24)"/>
      <text x="390" y="50" font-size="32" fill="#2e7d32" text-anchor="middle" font-weight="bold">답변 품질</text>
      <g transform="translate(60,100)">
        <rect width="660" height="110" rx="15" fill="#e8f5e9"/>
        <text x="330" y="35" font-size="24" fill="#1b5e20" text-anchor="middle" font-weight="bold">Faithfulness</text>
        <text x="330" y="70" font-size="20" fill="#666" text-anchor="middle">답변이 문서에만 기반?</text>
        <text x="330" y="95" font-size="18" fill="#999" text-anchor="middle">(환각 방지)</text>
        <rect x="0" y="130" width="660" height="110" rx="15" fill="#c8e6c9"/>
        <text x="330" y="165" font-size="24" fill="#2e7d32" text-anchor="middle" font-weight="bold">Answer Relevancy</text>
        <text x="330" y="200" font-size="20" fill="#666" text-anchor="middle">답변이 질문과 관련있는가?</text>
        <text x="330" y="225" font-size="18" fill="#999" text-anchor="middle">(질문-답변 일치도)</text>
      </g>
    </g>
    <g transform="translate(840,0)">
      <rect width="780" height="380" rx="20" fill="white" opacity="0.95" filter="url(#sh24)"/>
      <text x="390" y="50" font-size="32" fill="#1976d2" text-anchor="middle" font-weight="bold">검색 품질</text>
      <g transform="translate(60,100)">
        <rect width="660" height="110" rx="15" fill="#e3f2fd"/>
        <text x="330" y="35" font-size="24" fill="#0d47a1" text-anchor="middle" font-weight="bold">Context Precision</text>
        <text x="330" y="70" font-size="20" fill="#666" text-anchor="middle">검색 문서가 실제 관련있는가?</text>
        <text x="330" y="95" font-size="18" fill="#999" text-anchor="middle">(노이즈 적음)</text>
        <rect x="0" y="130" width="660" height="110" rx="15" fill="#bbdefb"/>
        <text x="330" y="165" font-size="24" fill="#1976d2" text-anchor="middle" font-weight="bold">Context Recall</text>
        <text x="330" y="200" font-size="20" fill="#666" text-anchor="middle">필요한 문서 모두 찾았는가?</text>
        <text x="330" y="225" font-size="18" fill="#999" text-anchor="middle">(누락 없음)</text>
      </g>
    </g>
  </g>
  <g transform="translate(200,940)">
    <rect width="1520" height="90" rx="20" fill="#4caf50" filter="url(#sh24)"/>
    <text x="760" y="57" font-size="28" fill="white" text-anchor="middle" font-weight="bold">💡 4가지 지표로 RAG 시스템 종합 평가!</text>
  </g>
</svg>""",

    "025": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg25" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh25"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg25)"/>
  <text x="960" y="120" font-size="64" fill="white" text-anchor="middle" font-weight="bold">Tuning 파라미터 ⚙️</text>
  <text x="960" y="190" font-size="32" fill="white" text-anchor="middle" opacity="0.9">성능 최적화 3대 파라미터</text>
  <g transform="translate(200,270)">
    <g transform="translate(0,0)">
      <rect width="490" height="560" rx="20" fill="white" opacity="0.95" filter="url(#sh25)"/>
      <text x="245" y="50" font-size="32" fill="#1976d2" text-anchor="middle" font-weight="bold">chunk_size</text>
      <g transform="translate(50,100)">
        <rect width="390" height="80" rx="15" fill="#e3f2fd"/>
        <text x="195" y="30" font-size="22" fill="#333" text-anchor="middle" font-weight="bold">권장 범위</text>
        <text x="195" y="60" font-size="24" fill="#1976d2" text-anchor="middle" font-weight="bold">200-500 글자</text>
        <text x="0" y="120" font-size="22" fill="#666">✓ 작을수록: 정확도 ↑</text>
        <text x="0" y="160" font-size="22" fill="#666">✓ 클수록: 문맥 ↑</text>
        <rect x="0" y="200" width="390" height="110" rx="15" fill="#fff9c4"/>
        <text x="195" y="235" font-size="20" fill="#f57f17" text-anchor="middle" font-weight="bold">💡 Best</text>
        <text x="195" y="270" font-size="20" fill="#666" text-anchor="middle">300-400 글자</text>
        <text x="195" y="295" font-size="18" fill="#999" text-anchor="middle">+ overlap 50-100</text>
      </g>
    </g>
    <g transform="translate(515,0)">
      <rect width="490" height="560" rx="20" fill="white" opacity="0.95" filter="url(#sh25)"/>
      <text x="245" y="50" font-size="32" fill="#7b1fa2" text-anchor="middle" font-weight="bold">top_k</text>
      <g transform="translate(50,100)">
        <rect width="390" height="80" rx="15" fill="#f3e5f5"/>
        <text x="195" y="30" font-size="22" fill="#333" text-anchor="middle" font-weight="bold">권장 범위</text>
        <text x="195" y="60" font-size="24" fill="#7b1fa2" text-anchor="middle" font-weight="bold">3-10 개</text>
        <text x="0" y="120" font-size="22" fill="#666">✓ 적을수록: 정확도 ↑</text>
        <text x="0" y="160" font-size="22" fill="#666">✓ 많을수록: Recall ↑</text>
        <rect x="0" y="200" width="390" height="110" rx="15" fill="#fff9c4"/>
        <text x="195" y="235" font-size="20" fill="#f57f17" text-anchor="middle" font-weight="bold">💡 Best</text>
        <text x="195" y="270" font-size="20" fill="#666" text-anchor="middle">Naive: 5개</text>
        <text x="195" y="295" font-size="18" fill="#999" text-anchor="middle">Rerank: 10개</text>
      </g>
    </g>
    <g transform="translate(1030,0)">
      <rect width="490" height="560" rx="20" fill="white" opacity="0.95" filter="url(#sh25)"/>
      <text x="245" y="50" font-size="32" fill="#e65100" text-anchor="middle" font-weight="bold">threshold</text>
      <g transform="translate(50,100)">
        <rect width="390" height="80" rx="15" fill="#fff3e0"/>
        <text x="195" y="30" font-size="22" fill="#333" text-anchor="middle" font-weight="bold">권장 범위</text>
        <text x="195" y="60" font-size="24" fill="#e65100" text-anchor="middle" font-weight="bold">0.3-0.7</text>
        <text x="0" y="120" font-size="22" fill="#666">✓ 높을수록: 정확도 ↑</text>
        <text x="0" y="160" font-size="22" fill="#666">✓ 낮을수록: Recall ↑</text>
        <rect x="0" y="200" width="390" height="110" rx="15" fill="#fff9c4"/>
        <text x="195" y="235" font-size="20" fill="#f57f17" text-anchor="middle" font-weight="bold">💡 Best</text>
        <text x="195" y="270" font-size="20" fill="#666" text-anchor="middle">0.5-0.6</text>
        <text x="195" y="295" font-size="18" fill="#999" text-anchor="middle">(균형있게)</text>
      </g>
    </g>
  </g>
  <g transform="translate(200,870)">
    <rect width="1520" height="140" rx="20" fill="#4caf50" filter="url(#sh25)"/>
    <text x="760" y="45" font-size="32" fill="white" text-anchor="middle" font-weight="bold">💡 파라미터 튜닝 팁</text>
    <text x="760" y="90" font-size="24" fill="white" text-anchor="middle">기본값으로 시작 → RAGAS로 측정 → 점진적 조정</text>
    <text x="760" y="125" font-size="22" fill="white" text-anchor="middle" opacity="0.9">한 번에 하나씩 바꿔가며 테스트!</text>
  </g>
</svg>"""
}

import os
svg_dir = "/Users/gim-yujin/workspace/lecture_cj/day2-RAG/presentation_v4/svg"
for slide_num, content in slides.items():
    with open(os.path.join(svg_dir, f"slide_{slide_num}.svg"), 'w') as f:
        f.write(content)
    print(f"Created slide_{slide_num}.svg")
print(f"\n✅ Created {len(slides)} slides (021-025)")
print("\n🎉 ALL V4 SLIDES COMPLETED! (26 slides total)")
