# Applied AI Engineer Challenge  
## Multi-Agent Content Generation System

---

## 1. Problem Statement

Modern e-commerce and marketing systems require scalable, reusable, and structured content generation pipelines rather than one-off AI scripts or prompt wrappers.

The goal of this assignment is to design a **modular, agent-based content system** that:
- Converts raw product data into structured internal representations
- Generates reusable content components
- Assembles multiple marketing pages (FAQ, Product Page, Comparison Page)
- Uses explicit orchestration and clear engineering boundaries

This system intentionally prioritizes **clarity, extensibility, and maintainability** over clever hacks or monolithic scripts.

---

## 2. Solution Overview

The solution is implemented as a **multi-agent pipeline**, where each agent has a single, well-defined responsibility.

At a high level, the system:
1. Accepts raw product input data
2. Normalizes it into a stable internal schema
3. Generates categorized customer questions
4. Produces reusable content logic blocks
5. Assembles final page outputs using templates
6. Outputs structured JSON suitable for downstream consumption

All agents are coordinated through a central orchestrator to ensure deterministic execution flow.

---

## 3. Scopes & Assumptions

### Scope
- Input data is assumed to be provided in a structured dictionary format
- Product B for comparison is fictional and used only for demonstration
- Outputs are generated as structured JSON (no UI rendering)

### Assumptions
- No external APIs or live data sources are used
- Content generation focuses on structure and system design, not copywriting quality
- The system is designed to be extended with LLM-backed agents later without breaking contracts

---

## 4. System Architecture

### Agent Responsibilities

| Agent | Responsibility |
|------|---------------|
| ProductParserAgent | Normalize raw input into an internal schema |
| QuestionGenerationAgent | Generate categorized customer questions |
| ContentLogicAgent | Produce reusable content blocks |
| TemplateAgents | Assemble page-specific structures |
| OrchestratorAgent | Control execution flow and data passing |

---

### Orchestration Flow

Raw Product Input
↓
ProductParserAgent
↓
Internal Product Schema
↓
QuestionGenerationAgent
↓
ContentLogicAgent (Reusable Blocks)
↓
TemplateAgents
↓
Structured JSON Outputs

The **OrchestratorAgent** acts as the single source of truth for execution order and data flow.

---

## 5. Design Decisions

### Separation of Concerns
Each agent performs exactly one responsibility.  
Business logic, orchestration, and presentation are intentionally decoupled.

### Reusable Content Blocks
ContentLogicAgent exposes pure functions that return structured blocks.  
These blocks can be reused across multiple pages without duplication.

### Deterministic Outputs
The system avoids hidden behavior and implicit state.  
Given the same input, outputs are predictable and reproducible.

### Extensibility
LLM-based generation can be introduced later by swapping logic inside individual agents without changing downstream consumers.

---

## 6. Output Structure

The system generates three outputs:

- `faq.json`  
- `product_page.json`  
- `comparison_page.json`  

Each output follows a predictable schema and can be consumed by CMS systems, frontends, or downstream pipelines.

---

## 7. Conclusion

This project demonstrates how agentic systems can be designed as **maintainable engineering systems**, not just AI-powered scripts.

The focus is on:
- Clear abstractions
- Explicit orchestration
- Reusable logic
- Production-friendly structure

This approach mirrors how internal AI content systems are built in real-world environments.
