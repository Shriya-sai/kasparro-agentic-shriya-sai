# Kasparro Applied AI Engineer Challenge  
### Multi-Agent Content Generation System

This repository contains a modular, agent-based system that generates
structured marketing content (FAQ, Product Page, and Comparison Page)
from raw product data.

The system emphasizes:
- Clear agent boundaries
- Reusable content logic blocks
- Deterministic orchestration
- Structured JSON outputs

## Project Structure
- `agents/` — Core agents handling parsing, generation, and orchestration
- `templates/` — Page-level content templates
- `data/` — Input product data
- `outputs/` — Generated structured outputs
- `docs/` — System design and documentation

## How to Run
```bash
python main.py
