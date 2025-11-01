#!/usr/bin/env python3
"""Generate final 3 slides (036-038)"""

slides = {
    "036": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad036" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow036"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad036)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.3"/>
    <text x="100" y="35" font-size="24" fill="white" text-anchor="middle" font-weight="bold">Part 7</text>
  </g>
  <text x="960" y="140" font-size="56" fill="white" text-anchor="middle" font-weight="bold">전체 성능 비교 📊</text>
  <text x="960" y="200" font-size="32" fill="white" text-anchor="middle" opacity="0.9">Naive → Advanced → Modular RAG 여정</text>
  <g transform="translate(300, 280)">
    <rect x="0" y="0" width="1320" height="650" rx="20" fill="white" opacity="0.95" filter="url(#shadow036)"/>
    <text x="660" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">RAG 진화 단계별 성능</text>
    <g transform="translate(100, 120)">
      <circle cx="100" cy="100" r="80" fill="#ef5350"/>
      <text x="100" y="115" font-size="48" fill="white" text-anchor="middle" font-weight="bold">35%</text>
      <text x="100" y="240" font-size="28" fill="#666" text-anchor="middle" font-weight="bold">Naive RAG</text>
      <g transform="translate(20, 280)">
        <text x="0" y="0" font-size="20" fill="#999">• Vector Search만</text>
        <text x="0" y="35" font-size="20" fill="#999">• Top-K만 사용</text>
        <text x="0" y="70" font-size="20" fill="#999">• 필터링 없음</text>
      </g>
      <circle cx="400" cy="100" r="90" fill="#fbc02d"/>
      <text x="400" y="115" font-size="48" fill="white" text-anchor="middle" font-weight="bold">65%</text>
      <text x="400" y="240" font-size="28" fill="#666" text-anchor="middle" font-weight="bold">Query Refinement</text>
      <g transform="translate(280, 280)">
        <text x="0" y="0" font-size="20" fill="#999">• Prompt Engineering</text>
        <text x="0" y="35" font-size="20" fill="#999">• Multi-Query/HyDE</text>
        <text x="0" y="70" font-size="20" fill="#999">• Metadata Filtering</text>
      </g>
      <circle cx="750" cy="100" r="100" fill="#1976d2"/>
      <text x="750" y="115" font-size="48" fill="white" text-anchor="middle" font-weight="bold">75%</text>
      <text x="750" y="240" font-size="28" fill="#666" text-anchor="middle" font-weight="bold">Hybrid Search</text>
      <g transform="translate(630, 280)">
        <text x="0" y="0" font-size="20" fill="#999">• Vector + BM25</text>
        <text x="0" y="35" font-size="20" fill="#999">• RRF 통합</text>
        <text x="0" y="70" font-size="20" fill="#999">• 속도 & 정확도</text>
      </g>
      <circle cx="1050" cy="100" r="110" fill="#2e7d32"/>
      <text x="1050" y="120" font-size="56" fill="white" text-anchor="middle" font-weight="bold">85%+</text>
      <text x="1050" y="240" font-size="28" fill="#666" text-anchor="middle" font-weight="bold">Modular RAG</text>
      <g transform="translate(920, 280)">
        <text x="0" y="0" font-size="20" fill="#999">• Cross-Encoder Rerank</text>
        <text x="0" y="35" font-size="20" fill="#999">• Self-RAG + CRAG</text>
        <text x="0" y="70" font-size="20" fill="#999">• 최고 정확도</text>
      </g>
    </g>
  </g>
  <g transform="translate(300, 960)">
    <rect x="0" y="0" width="1320" height="80" rx="20" fill="#4caf50" filter="url(#shadow036)"/>
    <text x="660" y="50" font-size="32" fill="white" text-anchor="middle" font-weight="bold">🎉 35% → 85%+, 무려 150% 성능 향상!</text>
  </g>
  <text x="960" y="1065" font-size="20" fill="white" text-anchor="middle" opacity="0.8">Slide 36 / 38</text>
</svg>""",

    "037": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad037" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fa709a;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fee140;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow037"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad037)"/>
  <g transform="translate(150, 80)">
    <rect x="0" y="0" width="200" height="50" rx="25" fill="white" opacity="0.3"/>
    <text x="100" y="35" font-size="24" fill="white" text-anchor="middle" font-weight="bold">Part 7</text>
  </g>
  <text x="960" y="140" font-size="56" fill="white" text-anchor="middle" font-weight="bold">실무 적용 가이드 💼</text>
  <text x="960" y="200" font-size="32" fill="white" text-anchor="middle" opacity="0.9">어떤 기법을 언제 쓸까?</text>
  <g transform="translate(200, 270)">
    <rect x="0" y="0" width="1520" height="680" rx="20" fill="white" opacity="0.95" filter="url(#shadow037)"/>
    <text x="760" y="50" font-size="32" fill="#333" text-anchor="middle" font-weight="bold">상황별 RAG 전략</text>
    <g transform="translate(80, 110)">
      <rect x="0" y="0" width="680" height="220" rx="15" fill="#e8f5e9"/>
      <text x="340" y="40" font-size="28" fill="#2e7d32" text-anchor="middle" font-weight="bold">🚀 빠른 프로토타입 (1-2일)</text>
      <g transform="translate(40, 75)">
        <text x="0" y="0" font-size="22" fill="#666" font-weight="bold">추천 구성:</text>
        <text x="0" y="40" font-size="20" fill="#666">✓ Naive RAG + Prompt Engineering</text>
        <text x="0" y="75" font-size="20" fill="#666">✓ chunk_size=400, top_k=5</text>
        <text x="0" y="120" font-size="20" fill="#2e7d32" font-weight="bold">→ 55-60% 정확도, 빠른 구현</text>
      </g>
      <rect x="760" y="0" width="680" height="220" rx="15" fill="#fff9c4"/>
      <text x="1100" y="40" font-size="28" fill="#f57f17" text-anchor="middle" font-weight="bold">⚡ 균형잡힌 성능 (1주)</text>
      <g transform="translate(800, 75)">
        <text x="0" y="0" font-size="22" fill="#666" font-weight="bold">추천 구성:</text>
        <text x="0" y="40" font-size="20" fill="#666">✓ Hybrid Search (Vector + BM25)</text>
        <text x="0" y="75" font-size="20" fill="#666">✓ Multi-Query + Metadata Filter</text>
        <text x="0" y="120" font-size="20" fill="#f57f17" font-weight="bold">→ 70-75% 정확도, 적절한 속도</text>
      </g>
      <rect x="0" y="250" width="680" height="220" rx="15" fill="#e3f2fd"/>
      <text x="340" y="290" font-size="28" fill="#1976d2" text-anchor="middle" font-weight="bold">🎯 최고 정확도 (2-3주)</text>
      <g transform="translate(40, 325)">
        <text x="0" y="0" font-size="22" fill="#666" font-weight="bold">추천 구성:</text>
        <text x="0" y="40" font-size="20" fill="#666">✓ Hybrid + Cross-Encoder Rerank</text>
        <text x="0" y="75" font-size="20" fill="#666">✓ RAG-Fusion + Self-RAG</text>
        <text x="0" y="120" font-size="20" fill="#1976d2" font-weight="bold">→ 80-85%+ 정확도, 비용↑</text>
      </g>
      <rect x="760" y="250" width="680" height="220" rx="15" fill="#fff3e0"/>
      <text x="1100" y="290" font-size="28" fill="#e65100" text-anchor="middle" font-weight="bold">💎 프로덕션 (지속)</text>
      <g transform="translate(800, 325)">
        <text x="0" y="0" font-size="22" fill="#666" font-weight="bold">추천 구성:</text>
        <text x="0" y="40" font-size="20" fill="#666">✓ Modular RAG (Router + CRAG)</text>
        <text x="0" y="75" font-size="20" fill="#666">✓ RAGAS 지속 모니터링</text>
        <text x="0" y="120" font-size="20" fill="#e65100" font-weight="bold">→ 85%+, 상황별 adaptive</text>
      </g>
    </g>
  </g>
  <g transform="translate(200, 980)">
    <rect x="0" y="0" width="1520" height="70" rx="20" fill="#667eea" filter="url(#shadow037)"/>
    <text x="760" y="47" font-size="28" fill="white" text-anchor="middle" font-weight="bold">💡 단계별로 구축! 먼저 Naive → 성능 측정 → 점진적 개선</text>
  </g>
  <text x="960" y="1065" font-size="20" fill="white" text-anchor="middle" opacity="0.8">Slide 37 / 38</text>
</svg>""",

    "038": """<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad038" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow038"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/></filter>
  </defs>
  <rect width="1920" height="1080" fill="url(#bgGrad038)"/>
  <text x="960" y="140" font-size="72" fill="white" text-anchor="middle" font-weight="bold">Day 2 완료! 🎉</text>
  <text x="960" y="220" font-size="40" fill="white" text-anchor="middle" opacity="0.9">Advanced RAG Systems</text>
  <g transform="translate(300, 300)">
    <rect x="0" y="0" width="1320" height="550" rx="20" fill="white" opacity="0.95" filter="url(#shadow038)"/>
    <text x="660" y="60" font-size="36" fill="#333" text-anchor="middle" font-weight="bold">오늘 배운 내용 요약</text>
    <g transform="translate(100, 130)">
      <circle cx="30" cy="15" r="25" fill="#1976d2"/>
      <text x="30" y="23" font-size="20" fill="white" text-anchor="middle" font-weight="bold">1</text>
      <text x="80" y="23" font-size="26" fill="#666">기초 이론: Embedding, Chunking, Cosine Similarity</text>
      <circle cx="30" cy="75" r="25" fill="#7b1fa2"/>
      <text x="30" y="83" font-size="20" fill="white" text-anchor="middle" font-weight="bold">2</text>
      <text x="80" y="83" font-size="26" fill="#666">문제 인식: Naive RAG 5가지 실패 패턴</text>
      <circle cx="30" cy="135" r="25" fill="#e65100"/>
      <text x="30" y="143" font-size="20" fill="white" text-anchor="middle" font-weight="bold">3</text>
      <text x="80" y="143" font-size="26" fill="#666">Query 개선: Prompt, Multi-Query, HyDE, RAG-Fusion</text>
      <circle cx="30" cy="195" r="25" fill="#2e7d32"/>
      <text x="30" y="203" font-size="20" fill="white" text-anchor="middle" font-weight="bold">4</text>
      <text x="80" y="203" font-size="26" fill="#666">검색 개선: Metadata, BM25, Hybrid, Cross-Encoder</text>
      <circle cx="30" cy="255" r="25" fill="#f57f17"/>
      <text x="30" y="263" font-size="20" fill="white" text-anchor="middle" font-weight="bold">5</text>
      <text x="80" y="263" font-size="26" fill="#666">자가 평가: Query Router, Self-RAG, CRAG</text>
      <circle cx="30" cy="315" r="25" fill="#c62828"/>
      <text x="30" y="323" font-size="20" fill="white" text-anchor="middle" font-weight="bold">6</text>
      <text x="80" y="323" font-size="26" fill="#666">평가 & 튜닝: RAGAS, chunk_size, top_k, threshold</text>
    </g>
  </g>
  <g transform="translate(300, 880)">
    <rect x="0" y="0" width="1320" height="140" rx="20" fill="#263238" filter="url(#shadow038)"/>
    <text x="660" y="45" font-size="32" fill="#81c784" text-anchor="middle" font-weight="bold">🚀 Next Steps: Day 3 - LangGraph Agents</text>
    <text x="660" y="90" font-size="26" fill="#e0e0e0" text-anchor="middle">ReAct Agents, Tool Registry, Multi-Agent Handoffs</text>
  </g>
  <text x="960" y="1065" font-size="24" fill="white" text-anchor="middle" opacity="0.9">수고하셨습니다! 💚 Slide 38 / 38</text>
</svg>"""
}

# Write final 3 slides
import os
svg_dir = "/Users/gim-yujin/workspace/lecture_cj/day2-RAG/presentation_v3/svg"
for slide_num, svg_content in slides.items():
    filepath = os.path.join(svg_dir, f"slide_{slide_num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Created slide_{slide_num}.svg")

print(f"\nCreated {len(slides)} slides (036-038)")
print("\n🎉 ALL 38 SLIDES COMPLETED!")
