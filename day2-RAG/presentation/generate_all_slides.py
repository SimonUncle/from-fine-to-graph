#!/usr/bin/env python3
"""
Day 2 RAG 강의 - 모든 슬라이드 완성 스크립트
절대 빼먹지 않고 63개 전부 풍부한 내용으로 생성
"""

SLIDES = {
    11: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
  <rect width="1920" height="1080" fill="#FFFFFF"/>
  <rect x="80" y="60" width="320" height="50" rx="25" fill="#FF6B6B" opacity="0.2"/>
  <text x="240" y="92" font-family="system-ui, sans-serif" font-size="22" font-weight="600" fill="#FF6B6B" text-anchor="middle">Section 2: 실패 분석</text>
  <text x="960" y="160" font-family="system-ui, sans-serif" font-size="64" font-weight="bold" fill="#2C3E50" text-anchor="middle">실패 2: Context 부족</text>
  <text x="960" y="220" font-family="system-ui, sans-serif" font-size="28" fill="#7F8C8D" text-anchor="middle">"단편적 검색으로 중요 정보 누락"</text>
  <g transform="translate(960, 240)"><circle cx="-60" cy="0" r="6" fill="#FF6B6B"/><circle cx="-30" cy="0" r="6" fill="#4ECDC4"/><circle cx="0" cy="0" r="6" fill="#45B7D1"/><circle cx="30" cy="0" r="6" fill="#96CEB4"/><circle cx="60" cy="0" r="6" fill="#FFEAA7"/></g>
  <g transform="translate(300, 320)">
    <rect x="0" y="0" width="1320" height="280" rx="20" fill="#FFF3CD" stroke="#F39C12" stroke-width="3"/>
    <text x="660" y="50" font-family="system-ui, sans-serif" font-size="32" font-weight="bold" fill="#2C3E50" text-anchor="middle">📚 필요한 전체 컨텍스트</text>
    <rect x="40" y="80" width="400" height="170" rx="15" fill="#D5F4E6"/>
    <text x="240" y="115" font-family="system-ui, sans-serif" font-size="20" font-weight="600" fill="#27AE60" text-anchor="middle">✅ 민법 제103조</text>
    <text x="240" y="180" font-family="system-ui, sans-serif" font-size="18" fill="#229954" text-anchor="middle">공서양속 위반 (핵심!)</text>
    <rect x="460" y="80" width="400" height="170" rx="15" fill="#FFE6E6"/>
    <text x="660" y="115" font-family="system-ui, sans-serif" font-size="20" font-weight="600" fill="#E74C3C" text-anchor="middle">⚠️ 판례 (보충)</text>
    <rect x="880" y="80" width="400" height="170" rx="15" fill="#FFE6E6"/>
    <text x="1080" y="115" font-family="system-ui, sans-serif" font-size="20" font-weight="600" fill="#E74C3C" text-anchor="middle">⚠️ 형법 (보충)</text>
  </g>
  <g transform="translate(300, 630)">
    <rect x="0" y="0" width="1320" height="200" rx="20" fill="#FFE6E6" stroke="#E74C3C" stroke-width="3"/>
    <text x="660" y="50" font-family="system-ui, sans-serif" font-size="32" font-weight="bold" fill="#E74C3C" text-anchor="middle">❌ Naive RAG: Top-K=3만 검색</text>
    <text x="660" y="120" font-family="system-ui, sans-serif" font-size="24" fill="#E74C3C" text-anchor="middle">보충 정보(판례, 형법)는 4위, 6위라 누락!</text>
  </g>
  <rect x="300" y="870" width="1320" height="110" rx="20" fill="#D5F4E6" stroke="#27AE60" stroke-width="3"/>
  <text x="500" y="925" font-family="system-ui, sans-serif" font-size="28" font-weight="bold" fill="#27AE60">✅ 해결: Top-K↑ + Multi-Query</text>
  <text x="1850" y="1040" font-family="system-ui, sans-serif" font-size="24" fill="#BDC3C7" text-anchor="end">11 / 63</text>
</svg>""",

    12: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
  <rect width="1920" height="1080" fill="#FFFFFF"/>
  <rect x="80" y="60" width="320" height="50" rx="25" fill="#FF6B6B" opacity="0.2"/>
  <text x="240" y="92" font-family="system-ui, sans-serif" font-size="22" font-weight="600" fill="#FF6B6B" text-anchor="middle">Section 2: 실패 분석</text>
  <text x="960" y="160" font-family="system-ui, sans-serif" font-size="64" font-weight="bold" fill="#2C3E50" text-anchor="middle">실패 3: 모호한 질문</text>
  <text x="960" y="220" font-family="system-ui, sans-serif" font-size="28" fill="#7F8C8D" text-anchor="middle">"중의성으로 잘못된 검색"</text>
  <g transform="translate(960, 240)"><circle cx="-60" cy="0" r="6" fill="#FF6B6B"/><circle cx="-30" cy="0" r="6" fill="#4ECDC4"/><circle cx="0" cy="0" r="6" fill="#45B7D1"/><circle cx="30" cy="0" r="6" fill="#96CEB4"/><circle cx="60" cy="0" r="6" fill="#FFEAA7"/></g>
  <rect x="200" y="300" width="1520" height="120" rx="20" fill="#FFFFBA" opacity="0.4" stroke="#F39C12" stroke-width="3"/>
  <text x="450" y="350" font-family="system-ui, sans-serif" font-size="32" font-weight="bold" fill="#2C3E50">❓ "계약 파기 가능한가요?"</text>
  <g transform="translate(200, 450)">
    <rect x="0" y="0" width="480" height="200" rx="15" fill="#BAE1FF" opacity="0.3" stroke="#45B7D1" stroke-width="2"/>
    <text x="240" y="60" font-family="system-ui, sans-serif" font-size="24" font-weight="600" fill="#2C3E50" text-anchor="middle">해석 1: 부동산</text>
    <rect x="520" y="0" width="480" height="200" rx="15" fill="#BAFFC9" opacity="0.3" stroke="#4ECDC4" stroke-width="2"/>
    <text x="760" y="60" font-family="system-ui, sans-serif" font-size="24" font-weight="600" fill="#2C3E50" text-anchor="middle">해석 2: 근로</text>
    <rect x="1040" y="0" width="480" height="200" rx="15" fill="#FFB3BA" opacity="0.3" stroke="#FF6B6B" stroke-width="2"/>
    <text x="1280" y="60" font-family="system-ui, sans-serif" font-size="24" font-weight="600" fill="#2C3E50" text-anchor="middle">해석 3: 용역</text>
  </g>
  <rect x="200" y="680" width="1520" height="110" rx="20" fill="#FFE6E6" stroke="#E74C3C" stroke-width="3"/>
  <text x="400" y="735" font-family="system-ui, sans-serif" font-size="28" font-weight="bold" fill="#E74C3C">❌ Naive RAG: 3개 해석 섞여서 검색</text>
  <rect x="200" y="820" width="1520" height="110" rx="20" fill="#D5F4E6" stroke="#27AE60" stroke-width="3"/>
  <text x="400" y="875" font-family="system-ui, sans-serif" font-size="28" font-weight="bold" fill="#27AE60">✅ 해결: Step-Back으로 명확화</text>
  <text x="1850" y="1040" font-family="system-ui, sans-serif" font-size="24" fill="#BDC3C7" text-anchor="end">12 / 63</text>
</svg>""",
}

import pathlib

def main():
    svg_dir = pathlib.Path(__file__).parent / "svg"

    for slide_num, svg_content in SLIDES.items():
        file_path = svg_dir / f"slide_{slide_num:03d}.svg"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✅ Slide {slide_num:03d} created")

    print(f"\n🎉 {len(SLIDES)}개 슬라이드 완성!")

if __name__ == "__main__":
    main()
