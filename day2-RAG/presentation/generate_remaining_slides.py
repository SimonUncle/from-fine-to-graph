#!/usr/bin/env python3
"""
Day 2 RAG 강의 SVG 슬라이드 자동 생성 스크립트

이미 제작된 핵심 슬라이드:
- 001-003: 인트로
- 004-008: Naive RAG
- 009: 실패 분석
- 019: Multi-Query
- 026: Quiz
- 033: Hybrid Search
- 048: RAGAS
- 063: 마무리

나머지 슬라이드를 템플릿으로 생성합니다.
"""

import os
from pathlib import Path

# SVG 템플릿 함수들
def create_svg_template(slide_num, section_name, section_color, title, subtitle, content_type="text"):
    """기본 SVG 슬라이드 템플릿"""

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <rect width="1920" height="1080" fill="#FFFFFF"/>

  <rect x="80" y="60" width="{len(section_name) * 20 + 80}" height="50" rx="25" fill="{section_color}" opacity="0.2"/>
  <text x="{(len(section_name) * 20 + 80) / 2 + 80}" y="92" font-family="system-ui, sans-serif" font-size="22" font-weight="600" fill="{section_color}" text-anchor="middle">{section_name}</text>

  <text x="960" y="160" font-family="system-ui, sans-serif" font-size="64" font-weight="bold" fill="#2C3E50" text-anchor="middle">{title}</text>
  <text x="960" y="220" font-family="system-ui, sans-serif" font-size="28" fill="#7F8C8D" text-anchor="middle">"{subtitle}"</text>

  <g transform="translate(960, 240)">
    <circle cx="-60" cy="0" r="6" fill="#FF6B6B"/>
    <circle cx="-30" cy="0" r="6" fill="#4ECDC4"/>
    <circle cx="0" cy="0" r="6" fill="#45B7D1"/>
    <circle cx="30" cy="0" r="6" fill="#96CEB4"/>
    <circle cx="60" cy="0" r="6" fill="#FFEAA7"/>
  </g>

  <!-- Main content area -->
  <rect x="200" y="320" width="1520" height="580" rx="20" fill="#F8F9FA" stroke="#E0E0E0" stroke-width="2"/>
  <text x="960" y="400" font-family="system-ui, sans-serif" font-size="32" font-weight="bold" fill="#2C3E50" text-anchor="middle">
    📝 여기에 내용을 채워주세요
  </text>

  <text x="960" y="500" font-family="system-ui, sans-serif" font-size="24" fill="#7F8C8D" text-anchor="middle">
    이 슬라이드는 템플릿입니다.
  </text>
  <text x="960" y="540" font-family="system-ui, sans-serif" font-size="22" fill="#95A5A6" text-anchor="middle">
    핵심 슬라이드({slide_num:03d})를 참고하여 내용을 작성하세요.
  </text>

  <!-- Bottom tip -->
  <rect x="200" y="940" width="1520" height="100" rx="15" fill="#FFFFBA" opacity="0.3"/>
  <text x="960" y="1000" font-family="system-ui, sans-serif" font-size="22" fill="#2C3E50" text-anchor="middle">
    💡 Tip: 제공된 핵심 슬라이드(001-063 중 12개)를 복사하여 수정하면 빠르게 완성할 수 있습니다!
  </text>

  <text x="1850" y="1040" font-family="system-ui, sans-serif" font-size="24" fill="#BDC3C7" text-anchor="end">{slide_num} / 63</text>
</svg>'''

    return svg


# 슬라이드 정의
SLIDES_TO_GENERATE = {
    # Section 1: Naive RAG (007만 생성, 나머지는 이미 있음)
    7: ("Section 1: Naive RAG", "#FF6B6B", "실제 테스트 결과", "도박 빚 질문의 Before 결과"),

    # Section 2: 실패 분석 (010-014)
    10: ("Section 2: 실패 분석", "#FF6B6B", "실패 1: Semantic Gap", "키워드 불일치 문제 상세"),
    11: ("Section 2: 실패 분석", "#FF6B6B", "실패 2: Context 부족", "단편적 검색의 한계"),
    12: ("Section 2: 실패 분석", "#FF6B6B", "실패 3: 모호한 질문", "중의성 문제"),
    13: ("Section 2: 실패 분석", "#FF6B6B", "실패 4: 최신성 부족", "시간 메타데이터 필요성"),
    14: ("Section 2: 실패 분석", "#FF6B6B", "실패 5: 낮은 관련성", "Threshold 부재 문제"),

    # Section 3: 프롬프트 엔지니어링 (015-018)
    15: ("Section 3: 프롬프트 엔지니어링", "#4ECDC4", "프롬프트 개선 전략", "3가지 핵심 원칙"),
    16: ("Section 3: 프롬프트 엔지니어링", "#4ECDC4", "코드 예시", "System prompt 최적화"),
    17: ("Section 3: 프롬프트 엔지니어링", "#4ECDC4", "Before/After", "프롬프트 개선 효과"),
    18: ("Section 3: 프롬프트 엔지니어링", "#4ECDC4", "연습문제", "프롬프트 작성 실습"),

    # Section 4: Query Refinement (020-025, 027은 생략)
    20: ("Section 4: Query Refinement", "#4ECDC4", "HyDE 기법", "가상 답변 생성 방식"),
    21: ("Section 4: Query Refinement", "#4ECDC4", "HyDE 코드", "Hypothetical Document"),
    22: ("Section 4: Query Refinement", "#4ECDC4", "Step-Back 기법", "추상화 다이어그램"),
    23: ("Section 4: Query Refinement", "#4ECDC4", "Step-Back 코드", "일반화 예시"),
    24: ("Section 4: Query Refinement", "#4ECDC4", "성능 비교", "3가지 기법 비교 차트"),
    25: ("Section 4: Query Refinement", "#4ECDC4", "언제 사용하나요", "기법별 적용 시나리오"),

    # Section 5: Metadata Filtering (027-032)
    27: ("Section 5: Metadata Filtering", "#4ECDC4", "메타데이터란?", "시간, 카테고리, 출처"),
    28: ("Section 5: Metadata Filtering", "#4ECDC4", "필터링 전략", "Time-based, Category-based"),
    29: ("Section 5: Metadata Filtering", "#4ECDC4", "코드 예시", "filter 파라미터 사용법"),
    30: ("Section 5: Metadata Filtering", "#4ECDC4", "실전 시나리오", "2023년 이후 법률 검색"),
    31: ("Section 5: Metadata Filtering", "#4ECDC4", "성능 개선", "Precision +35% 차트"),
    32: ("Section 5: Metadata Filtering", "#4ECDC4", "연습문제", "메타데이터 쿼리 작성"),

    # Section 6: Hybrid Search (034-040)
    34: ("Section 6: Hybrid Search", "#45B7D1", "RRF 융합 방식", "Reciprocal Rank Fusion"),
    35: ("Section 6: Hybrid Search", "#45B7D1", "RRF 코드", "점수 계산 로직"),
    36: ("Section 6: Hybrid Search", "#45B7D1", "Cross-Encoder Reranking", "정밀 재정렬"),
    37: ("Section 6: Hybrid Search", "#45B7D1", "전체 파이프라인", "Query → Hybrid → RRF → Rerank"),
    38: ("Section 6: Hybrid Search", "#45B7D1", "성능 비교", "Naive vs Hybrid 차트"),
    39: ("Section 6: Hybrid Search", "#45B7D1", "코드 예시", "Hybrid Search 구현"),
    40: ("Section 6: Hybrid Search", "#45B7D1", "Quiz", "BM25가 유리한 경우는?"),

    # Section 7: Corrective RAG (041-047)
    41: ("Section 7: Corrective RAG", "#96CEB4", "CRAG란?", "검색 결과 품질 평가"),
    42: ("Section 7: Corrective RAG", "#96CEB4", "3가지 액션", "Correct/Incorrect/Ambiguous"),
    43: ("Section 7: Corrective RAG", "#96CEB4", "Action: Correct", "검색 성공 시"),
    44: ("Section 7: Corrective RAG", "#96CEB4", "Action: Incorrect", "Web Search 보완"),
    45: ("Section 7: Corrective RAG", "#96CEB4", "Action: Ambiguous", "재검색 + 필터링"),
    46: ("Section 7: Corrective RAG", "#96CEB4", "코드 예시", "evaluate_retrieval() 함수"),
    47: ("Section 7: Corrective RAG", "#96CEB4", "연습문제", "시나리오별 액션 선택"),

    # Section 8: RAGAS Evaluation (049-055)
    49: ("Section 8: RAGAS Evaluation", "#96CEB4", "Faithfulness 상세", "환각 측정 방법"),
    50: ("Section 8: RAGAS Evaluation", "#96CEB4", "Answer Relevancy 상세", "질문-답변 연관성"),
    51: ("Section 8: RAGAS Evaluation", "#96CEB4", "Context Precision 상세", "검색 정확도"),
    52: ("Section 8: RAGAS Evaluation", "#96CEB4", "Context Recall 상세", "검색 완성도"),
    53: ("Section 8: RAGAS Evaluation", "#96CEB4", "종합 평가 결과", "Naive vs Advanced 레이더"),
    54: ("Section 8: RAGAS Evaluation", "#96CEB4", "코드 예시", "RAGAS 계산 함수"),
    55: ("Section 8: RAGAS Evaluation", "#96CEB4", "Quiz", "Faithfulness 0.5는 위험?"),

    # Section 9: Tuning (056-060)
    56: ("Section 9: Tuning", "#FFEAA7", "튜닝 파라미터 3가지", "Chunk Size, Top-K, Threshold"),
    57: ("Section 9: Tuning", "#FFEAA7", "Chunk Size 실험", "256 vs 512 vs 1024"),
    58: ("Section 9: Tuning", "#FFEAA7", "Top-K 실험", "k=1 vs k=5 vs k=10"),
    59: ("Section 9: Tuning", "#FFEAA7", "Threshold 실험", "0.1 vs 0.3 vs 0.7"),
    60: ("Section 9: Tuning", "#FFEAA7", "최종 연습", "나만의 파라미터 찾기"),

    # Section 10: 마무리 (061-062)
    61: ("Section 10: 마무리", "#27AE60", "전체 요약", "핵심 8가지 기법"),
    62: ("Section 10: 마무리", "#27AE60", "성능 개선 요약", "Before/After 최종 비교"),
}


def main():
    # SVG 폴더 경로
    svg_dir = Path(__file__).parent / "svg"

    print("🎨 Day 2 RAG 강의 SVG 슬라이드 자동 생성 시작...")
    print(f"📁 저장 위치: {svg_dir}")
    print()

    generated_count = 0
    skipped_count = 0

    for slide_num, (section, color, title, subtitle) in SLIDES_TO_GENERATE.items():
        slide_path = svg_dir / f"slide_{slide_num:03d}.svg"

        # 이미 있으면 스킵
        if slide_path.exists():
            print(f"⏭️  Slide {slide_num:03d}: 이미 존재함 (스킵)")
            skipped_count += 1
            continue

        # SVG 생성
        svg_content = create_svg_template(slide_num, section, color, title, subtitle)

        # 파일 저장
        with open(slide_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)

        print(f"✅ Slide {slide_num:03d}: {title}")
        generated_count += 1

    print()
    print("="*60)
    print(f"🎉 완료!")
    print(f"   생성됨: {generated_count}개")
    print(f"   스킵됨: {skipped_count}개 (이미 존재)")
    print(f"   총 슬라이드: {len(list(svg_dir.glob('slide_*.svg')))}개")
    print()
    print("💡 Tip:")
    print("   1. 핵심 슬라이드(001,004,009,019,026,033,048,063)를 참고하세요")
    print("   2. 템플릿 슬라이드를 복사하여 내용만 수정하면 됩니다")
    print("   3. index.html로 모든 슬라이드를 쉽게 볼 수 있습니다")
    print("="*60)


if __name__ == "__main__":
    main()
