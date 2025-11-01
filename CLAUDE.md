# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a 3-day educational workshop on fine-tuning, RAG systems, and LangGraph agents, with all content in Jupyter notebooks (.ipynb). The repository is structured as an instructional curriculum progressing from foundational concepts to advanced implementations.

## Repository Structure

```
lecture_cj/
├── day1-finetune/          # Day 1: EXAONE 3.5 fine-tuning with RAFT
│   ├── main-practice/      # 4 sequential notebooks (01-04)
│   ├── prerequisites/      # Foundation notebooks (00.01-00.06)
│   └── processed_data/     # Generated training data
├── day2-RAG/               # Day 2: Naive → Advanced → Modular RAG
│   ├── main-practice/      # 8 notebooks (01-08) showing RAG evolution
│   └── prerequisites/      # RAG basics
└── day3-agent-langgraph/   # Day 3: LangGraph agent patterns
    ├── main-practice/      # Guide + Lab pairs (00-01, 01-01, 02-01, 03-01)
    ├── prerequisites/      # LangGraph fundamentals
    └── legacy/             # Old implementations (kept for reference)
```

## Working with Jupyter Notebooks

### Critical: Notebook Cell Format

**Jupyter notebooks MUST have proper line breaks in source cells.** Each line of code must be a separate list item ending with `\n`:

```python
# CORRECT format
cell['source'] = [
    "import os\n",
    "import sys\n",
    "\n",
    "def foo():\n",
    "    return 42"  # Last line without \n
]

# WRONG format (will cause display issues)
cell['source'] = "import os\nimport sys\n\ndef foo():\n    return 42"
```

### Reading Notebooks Safely

Notebook files are large (often >25000 tokens). Use these strategies:

```python
# Use Python json.load for large files
import json
with open('notebook.ipynb', 'r') as f:
    nb = json.load(f)

# Access specific cells
cell3 = nb['cells'][2]
cell_content = ''.join(cell3['source'])

# Or use offset/limit with Read tool
Read(file_path="path.ipynb", offset=1, limit=100)
```

### Editing Notebook Cells

When modifying cell content:

```python
def split_properly(text):
    """Convert text to proper notebook format"""
    lines = text.split('\n')
    return [line + '\n' for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])

# Apply to cell
notebook['cells'][5]['source'] = split_properly(new_content)
```

### Common Notebook Issues

1. **Cells with code on one line**: Previous batch operations may have removed line breaks
   - Fix: Use `split_properly()` function above

2. **Markdown cells with code blocks**: Should NOT use triple backticks for examples meant to be explanatory
   - Recipe examples in markdown: OK to use code blocks
   - Instructions to run code: Should be plain text, not code blocks

3. **Korean font configuration**: Often unnecessary and causes errors
   - Safe to remove matplotlib Korean font setup if it's failing

## Day 1: Fine-tuning Architecture

### Key Files
- `01_data_preprocessing_and_validation.ipynb`: RAFT preprocessing (neural-bridge/rag-dataset-12000)
- `02_data_quality_check.ipynb`: Token distribution, validation
- `03_fine_tuning_with_lora.ipynb`: QLoRA (4-bit quantization + LoRA)
- `04_evaluation_and_comparison.ipynb`: ROUGE, BLEU, perplexity metrics

### Dependencies
```bash
# Install evaluation metrics
pip install sentence-transformers evaluate rouge-score sacrebleu
```

### Technical Details
- **Model**: LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct
- **Method**: QLoRA (4-bit quantization + Low-Rank Adaptation)
- **Dataset**: RAFT format with positive/negative samples
- **Goal**: 15-25% ROUGE-L improvement, 10-20% BLEU improvement

## Day 2: RAG System Evolution

### Progression Path
01. **Naive RAG Baseline**: FAISS + simple vector search
02. **Failure Analysis**: 5 failure patterns (semantic gap, context fragmentation, ambiguous queries, stale data, low relevance)
03. **Query Refinement**: Multi-Query, Sub-Question, RAG-Fusion
04. **Metadata Filtering**: Time-based, category-based filtering
05. **Hybrid Search**: BM25 + Vector + Cross-encoder reranking
06. **Modular RAG**: Query routing, Self-RAG, adaptive selection
07. **Evaluation**: Comprehensive metrics and comparison
08. **Tuning & Customization**: Parameter optimization (chunk_size, top_k, threshold)

### Recipe Domain (Notebook 08)

Notebook 08 uses **13 Korean recipe documents** (not legal documents):
- 5 core recipes: 김치찌개, 된장찌개, 제육볶음, 불고기, 비빔밥
- 5 confusers: TV show variations (백종원, 흑백요리사)
- 3 noise docs: 조리 용어, 보관법, 칼질

### Hybrid Evaluation Approach (Notebook 08)

**Critical:** The notebook uses a hybrid evaluation system:

```python
# Precision: Cosine similarity based (threshold=0.3)
def calculate_context_precision(query, retrieved_docs, embeddings_model, threshold=0.3):
    # Relevance = cosine_similarity(query, doc) >= threshold

# Recall: Keyword matching based (metadata)
def calculate_context_recall(required_recipes, retrieved_docs):
    # Exact match: recipe_name in required_recipes
```

**Function signatures:**
```python
precision, rel_count = calculate_context_precision(query, results, embeddings, threshold=0.3)
recall, found_count = calculate_context_recall(required_recipes, results)
```

**Output messages:**
- Precision: "문서가 관련 있음 (유사도 >= 0.3)"
- Recall: "필요 레시피 찾음" (exact match)

### Key Dependencies
```python
# LangChain ecosystem
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sklearn.metrics.pairwise import cosine_similarity

# Embedding model
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")
```

## Day 3: LangGraph Patterns

### Guide + Lab Structure

Each module has two notebooks:
- **Guide** (`XX-01-*-guide.ipynb`): Complete implementation with explanations
- **Lab** (`XX-02-*-lab.ipynb`): TODO exercises for hands-on practice

### Modules
1. **LangGraph Fundamentals** (00): State, Node, Graph, interrupt/resume for Human-in-the-Loop
2. **Advanced Integration** (01): Routing, Fan-out/Fan-in, Summarization patterns
3. **ReAct Agent** (02): Tool registry + observation-thought-action loop
4. **Multi-Agent Handoffs** (03): Sequential agent collaboration with deterministic LangGraph

### Critical LangGraph Concepts

**Human in the Loop with interrupt/resume:**
```python
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import MemorySaver

# In node: pause workflow
feedback = interrupt({"message": "Review needed", "data": draft})

# Resume with feedback
result = app.invoke(Command(resume=feedback), config=config)
```

**State Management:**
```python
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[List, add_messages]  # Reducer for safe merging
    user_input: str
```

**Fan-out/Fan-in Pattern:**
- Use `START` and `END` constants
- Parallel edges from one node to multiple: automatic fan-out
- Multiple edges to one node: automatic fan-in with state reduction

## Common Development Workflows

### Fixing Notebook Line Breaks

```bash
python3 << 'EOF'
import json

with open('notebook.ipynb', 'r') as f:
    nb = json.load(f)

# Fix all cells with improper formatting
for i, cell in enumerate(nb['cells']):
    if isinstance(cell['source'], str):
        # Convert string to list with proper line breaks
        lines = cell['source'].split('\n')
        cell['source'] = [line + '\n' for line in lines[:-1]] + [lines[-1]]

with open('notebook.ipynb', 'w') as f:
    json.dump(nb, ensure_ascii=False, indent=1)
EOF
```

### Updating Notebook Function Calls

When changing function signatures across many cells, use Python script:

```python
import json
import re

with open('notebook.ipynb', 'r') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        # Update function call pattern
        updated = re.sub(
            r'old_function\(([^)]+)\)',
            r'new_function(\1, new_param)',
            source
        )
        cell['source'] = updated.split('\n')

with open('notebook.ipynb', 'w') as f:
    json.dump(nb, ensure_ascii=False, indent=1)
```

### Running Notebook Tests

```bash
# Execute notebook and check for errors
jupyter nbconvert --to notebook --execute notebook.ipynb --output test_output.ipynb

# Run specific cells (in Python)
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

with open('notebook.ipynb') as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': './'}})
```

## Educational Context

### Pedagogy Notes

1. **Progressive Complexity**: Each day builds on previous concepts
   - Day 1: Model-level (fine-tuning)
   - Day 2: System-level (RAG)
   - Day 3: Orchestration-level (agents)

2. **Practical Focus**: Every notebook is hands-on with real implementations
   - No theoretical-only content
   - All code is executable
   - Visual outputs (charts, diagrams) for understanding

3. **Korean Language Support**: All UI text, comments, and examples in Korean
   - Students are Korean speakers
   - Recipe examples use Korean food culture
   - Error messages should remain in English for debugging

### Student Interaction Patterns

When students report issues:
1. They may show screenshots of broken cells
2. They expect immediate fixes without long explanations
3. They prefer seeing TODO markers like "# 여기를 수정하세요! 👇"
4. They need visual confirmation (print statements, charts)

## Critical Rules for This Repository

1. **Never remove "# 여기를 수정하세요!" comments** - these mark student exercise points
2. **Always maintain Korean text** - this is for Korean students
3. **Preserve notebook cell execution order** - notebooks are sequential tutorials
4. **Keep visual outputs** - charts and diagrams are pedagogical tools
5. **Test notebooks can execute** - broken notebooks block student progress
6. **Maintain consistent naming** - `recipe_docs_raw`, `required_recipes`, `embeddings`, etc.
7. **Respect the hybrid evaluation** - Precision uses cosine similarity, Recall uses exact match

## Troubleshooting

### GPU Memory Issues (Day 1)
```python
# Reduce batch size
per_device_train_batch_size=1
gradient_accumulation_steps=8
```

### FAISS Loading Issues (Day 2)
```python
# Proper save/load
vector_store.save_local("faiss_index")
vector_store = FAISS.load_local("faiss_index", embeddings)
```

### LangGraph State Conflicts (Day 3)
```python
# Use Annotated with reducers for parallel updates
from typing import Annotated
import operator

class State(TypedDict):
    results: Annotated[List[str], operator.add]  # Safe merging
```

## Environment Requirements

- Python 3.8+
- Jupyter notebook/lab
- For Day 1: GPU recommended (Colab T4 sufficient)
- For Day 2-3: CPU sufficient
- All notebooks use Korean language - no font configuration needed (often breaks)

## Version Control Notes

This repo uses git with:
- Main branch: `main`
- Large notebooks tracked normally (no LFS)
- `.DS_Store` files should be ignored but currently tracked
- Some legacy folders preserved for reference
