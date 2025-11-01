#!/usr/bin/env python3
"""v4에 누락된 핵심 슬라이드 추가 (015-025)"""

slides = {
    "015": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg15" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a8edea;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#fed6e3;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh15"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg15)"/>
  <text x="960" y="120" font-size="64" fill="#333" text-anchor="middle" font-weight="bold">Sub-Question 🧩</text>
  <text x="960" y="190" font-size="32" fill="#666" text-anchor="middle">복잡한 질문을 작은 질문들로 분해</text>
  <g transform="translate(200,260)">
    <rect width="1520" height="180" rx="20" fill="white" opacity="0.9" filter="url(#sh15)"/>
    <text x="760" y="60" font-size="28" fill="#c62828" text-anchor="middle" font-weight="bold">복잡한 질문</text>
    <rect x="250" y="85" width="1020" height="70" rx="15" fill="#ffebee"/>
    <text x="760" y="135" font-size="24" fill="#333" text-anchor="middle">"김치찌개를 맛있게 만들려면 어떤 김치를 쓰고, 얼마나 끓여야 해?"</text>
  </g>
  <text x="960" y="520" font-size="48" fill="#667eea" text-anchor="middle">⬇️</text>
  <g transform="translate(150,580)">
    <rect width="520" height="140" rx="20" fill="white" opacity="0.9" filter="url(#sh15)"/>
    <text x="260" y="45" font-size="24" fill="#1976d2" text-anchor="middle" font-weight="bold">Sub-Q 1</text>
    <text x="260" y="85" font-size="20" fill="#666" text-anchor="middle">"김치찌개에 어떤</text>
    <text x="260" y="115" font-size="20" fill="#666" text-anchor="middle">김치를 써야 해?"</text>
  </g>
  <g transform="translate(700,580)">
    <rect width="520" height="140" rx="20" fill="white" opacity="0.9" filter="url(#sh15)"/>
    <text x="260" y="45" font-size="24" fill="#7b1fa2" text-anchor="middle" font-weight="bold">Sub-Q 2</text>
    <text x="260" y="85" font-size="20" fill="#666" text-anchor="middle">"김치찌개는 얼마나</text>
    <text x="260" y="115" font-size="20" fill="#666" text-anchor="middle">끓여야 해?"</text>
  </g>
  <g transform="translate(1250,580)">
    <rect width="520" height="140" rx="20" fill="white" opacity="0.9" filter="url(#sh15)"/>
    <text x="260" y="45" font-size="24" fill="#e65100" text-anchor="middle" font-weight="bold">Sub-Q 3</text>
    <text x="260" y="85" font-size="20" fill="#666" text-anchor="middle">"맛있게 만드는</text>
    <text x="260" y="115" font-size="20" fill="#666" text-anchor="middle">팁은?"</text>
  </g>
  <g transform="translate(200,780)">
    <rect width="1520" height="220" rx="20" fill="#4caf50" filter="url(#sh15)"/>
    <text x="760" y="50" font-size="32" fill="white" text-anchor="middle" font-weight="bold">💡 장점</text>
    <text x="760" y="100" font-size="26" fill="white" text-anchor="middle">각 질문을 독립적으로 검색 → 더 정확한 답변 조각 획득</text>
    <text x="760" y="145" font-size="26" fill="white" text-anchor="middle">3개 답변 통합 → 완전하고 상세한 최종 답변</text>
    <text x="760" y="190" font-size="24" fill="white" text-anchor="middle" opacity="0.9">복잡한 질문에 효과적!</text>
  </g>
</svg>""",

    "016": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg16" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fbc2eb;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#a6c1ee;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh16"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg16)"/>
  <text x="960" y="120" font-size="64" fill="white" text-anchor="middle" font-weight="bold">RAG-Fusion 🔗</text>
  <text x="960" y="190" font-size="32" fill="white" text-anchor="middle" opacity="0.9">Multi-Query + RRF로 결과 통합</text>
  <g transform="translate(250,260)">
    <rect width="420" height="150" rx="20" fill="white" opacity="0.95" filter="url(#sh16)"/>
    <text x="210" y="45" font-size="24" fill="#1976d2" text-anchor="middle" font-weight="bold">Query 1</text>
    <text x="210" y="85" font-size="20" fill="#666" text-anchor="middle">김치찌개</text>
    <text x="210" y="115" font-size="20" fill="#666" text-anchor="middle">만드는 법</text>
  </g>
  <g transform="translate(750,260)">
    <rect width="420" height="150" rx="20" fill="white" opacity="0.95" filter="url(#sh16)"/>
    <text x="210" y="45" font-size="24" fill="#7b1fa2" text-anchor="middle" font-weight="bold">Query 2</text>
    <text x="210" y="85" font-size="20" fill="#666" text-anchor="middle">김치찌개</text>
    <text x="210" y="115" font-size="20" fill="#666" text-anchor="middle">조리법</text>
  </g>
  <g transform="translate(1250,260)">
    <rect width="420" height="150" rx="20" fill="white" opacity="0.95" filter="url(#sh16)"/>
    <text x="210" y="45" font-size="24" fill="#e65100" text-anchor="middle" font-weight="bold">Query 3</text>
    <text x="210" y="85" font-size="20" fill="#666" text-anchor="middle">김치찌개</text>
    <text x="210" y="115" font-size="20" fill="#666" text-anchor="middle">요리 방법</text>
  </g>
  <text x="960" y="480" font-size="36" fill="white" text-anchor="middle">각각 Top-3 검색 ⬇️</text>
  <g transform="translate(300,550)">
    <rect width="1320" height="180" rx="20" fill="#fff9c4" filter="url(#sh16)"/>
    <text x="660" y="50" font-size="28" fill="#f57f17" text-anchor="middle" font-weight="bold">🔗 RRF (Reciprocal Rank Fusion)</text>
    <text x="660" y="95" font-size="24" fill="#666" text-anchor="middle">순위 기반으로 점수 계산: score = 1 / (60 + rank)</text>
    <text x="660" y="135" font-size="24" fill="#666" text-anchor="middle">3개 결과 리스트를 하나로 통합 → 민주적 순위 결정!</text>
  </g>
  <g transform="translate(300,770)">
    <rect width="1320" height="210" rx="20" fill="#e8f5e9" filter="url(#sh16)"/>
    <text x="660" y="50" font-size="32" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ 최종 결과</text>
    <g transform="translate(100,90)">
      <text x="0" y="0" font-size="24" fill="#666">1위: 김치찌개 레시피 (3개 쿼리 모두 상위 등장)</text>
      <text x="0" y="45" font-size="24" fill="#666">2위: 백종원 김치찌개 (여러 쿼리에서 발견)</text>
      <text x="0" y="90" font-size="24" fill="#666">→ 편향 감소, 다양한 관점 반영!</text>
    </g>
  </g>
</svg>""",

    "017": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg17" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fa709a;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#fee140;stop-opacity:1"/>
    </linearGradient>
    <filter id="sh17"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg17)"/>
  <text x="960" y="120" font-size="64" fill="white" text-anchor="middle" font-weight="bold">HyDE 💡</text>
  <text x="960" y="190" font-size="32" fill="white" text-anchor="middle" opacity="0.9">가짜 답변 생성 후 검색</text>
  <g transform="translate(200,260)">
    <rect width="750" height="650" rx="20" fill="white" opacity="0.95" filter="url(#sh17)"/>
    <text x="375" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">Step 1: 가짜 답변 생성</text>
    <rect x="50" y="90" width="650" height="90" rx="15" fill="#e3f2fd"/>
    <text x="375" y="125" font-size="22" fill="#1976d2" text-anchor="middle" font-weight="bold">질문</text>
    <text x="375" y="160" font-size="20" fill="#666" text-anchor="middle">"김치찌개 레시피 알려줘"</text>
    <text x="375" y="230" font-size="36" fill="#667eea" text-anchor="middle">⬇️ LLM</text>
    <rect x="50" y="270" width="650" height="350" rx="15" fill="#fff3e0"/>
    <text x="375" y="310" font-size="22" fill="#e65100" text-anchor="middle" font-weight="bold">가짜 답변 (Hypothetical Doc)</text>
    <g transform="translate(80,340)">
      <text x="0" y="0" font-size="19" fill="#666">"김치찌개는 배추김치 200g과</text>
      <text x="0" y="35" font-size="19" fill="#666">돼지고기 150g을 준비합니다.</text>
      <text x="0" y="70" font-size="19" fill="#666">냄비에 김치를 넣고 중불에서</text>
      <text x="0" y="105" font-size="19" fill="#666">20분간 끓이면 완성됩니다.</text>
      <text x="0" y="140" font-size="19" fill="#666">두부와 파를 추가하면</text>
      <text x="0" y="175" font-size="19" fill="#666">더욱 맛있습니다."</text>
      <text x="0" y="225" font-size="18" fill="#999" font-style="italic">(실제 문서처럼 길고 상세함)</text>
    </g>
  </g>
  <g transform="translate(970,260)">
    <rect width="750" height="650" rx="20" fill="white" opacity="0.95" filter="url(#sh17)"/>
    <text x="375" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">Step 2: 가짜 답변으로 검색</text>
    <text x="375" y="120" font-size="24" fill="#666" text-anchor="middle">가짜 답변 임베딩 ↔️ 문서 임베딩</text>
    <rect x="50" y="160" width="650" height="130" rx="15" fill="#e8f5e9"/>
    <text x="375" y="195" font-size="22" fill="#2e7d32" text-anchor="middle" font-weight="bold">✅ 검색 결과</text>
    <text x="375" y="235" font-size="20" fill="#666" text-anchor="middle">1위: 김치찌개 레시피 (0.94)</text>
    <text x="375" y="270" font-size="20" fill="#666" text-anchor="middle">2위: 김치찌개 조리법 (0.91)</text>
    <rect x="50" y="320" width="650" height="300" rx="15" fill="#fff9c4"/>
    <text x="375" y="360" font-size="26" fill="#f57f17" text-anchor="middle" font-weight="bold">💡 왜 효과적?</text>
    <g transform="translate(80,395)">
      <text x="0" y="0" font-size="22" fill="#666">✓ 질문: 짧고 단순</text>
      <text x="0" y="40" font-size="22" fill="#666">   "레시피 알려줘" (10자)</text>
      <text x="0" y="90" font-size="22" fill="#666">✓ 문서: 길고 상세</text>
      <text x="0" y="130" font-size="22" fill="#666">   "배추김치 200g..." (500자)</text>
      <text x="0" y="180" font-size="22" fill="#2e7d32" font-weight="bold">→ 형식 차이 극복!</text>
    </g>
  </g>
</svg>"""
}

# Write slides
import os
svg_dir = "/Users/gim-yujin/workspace/lecture_cj/day2-RAG/presentation_v4/svg"
for slide_num, content in slides.items():
    with open(os.path.join(svg_dir, f"slide_{slide_num}.svg"), 'w') as f:
        f.write(content)
    print(f"Created slide_{slide_num}.svg")
print(f"\n✅ Created {len(slides)} slides (015-017)")
