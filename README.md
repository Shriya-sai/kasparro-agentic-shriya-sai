# Kasparro Applied AI Engineer Challenge  
## Multi-Agent Content Generation System

This repository contains a **modular, agent-based content generation system** designed to transform raw product data into structured, reusable marketing content.

The focus of this project is **system design, explicit orchestration, validation, and reusability** — not prompt-heavy or monolithic AI scripts.

---

## 🎯 Objective

Design a production-oriented **agentic content system** that:

- Uses clear agent boundaries  
- Exposes reusable logic blocks  
- Orchestrates execution explicitly  
- Applies validation and quality gates  
- Produces structured, deterministic outputs from non-deterministic LLMs  

---

## 🧠 System Overview

The system is composed of multiple agents, each with a single responsibility:

| Component | Description |
|---------|-------------|
| **ProductParserAgent** | Normalizes raw product input into a stable internal schema |
| **QuestionGenerationAgent** | Uses a LangChain-backed LLM to generate categorized customer FAQs with schema validation |
| **ContentLogicAgent** | Produces reusable, deterministic content blocks |
| **TemplateAgents** | Assemble page-level outputs from reusable blocks |
| **OrchestratorAgent** | Controls execution flow, agent coordination, and data passing |
| **main.py** | Entry point for end-to-end execution |

All agents are coordinated through an explicit orchestration layer rather than implicit chaining.

---

## 🤖 LLM & Agent Architecture

The system uses **LangChain-backed agents** powered by a **Groq-hosted LLaMA 3.1 LLM** for content generation tasks.

Key characteristics:

- Non-deterministic LLM outputs are constrained using:
  - Prompt structure
  - JSON schema validation (Pydantic)
  - Quality gates (minimum FAQ count enforcement)
- Agents maintain conversational memory where appropriate
- LLM usage is isolated to generation tasks; deterministic logic remains outside the model

This design mirrors real-world applied AI systems where **LLMs are components, not the system itself**.

---

## 🔁 Execution Flow

Raw Product Input
↓
ProductParserAgent
↓
Internal Product Schema
↓
QuestionGenerationAgent (LLM-backed)
↓
ContentLogicAgent (Reusable Blocks)
↓
TemplateAgents
↓
Structured JSON Outputs

---

## 📂 Project Structure

kasparro-agentic-shriya-sai/
│
├── agents/ # Core agent logic
├── templates/ # Page-level templates
├── data/ # Raw input data
├── outputs/ # Generated JSON outputs
├── docs/ # System documentation
├── main.py # Entry point
└── README.md

---

## 📦 Outputs

Running the system generates three structured outputs:

- `faq.json` — Categorized customer FAQs  
- `product_page.json` — Product overview and details  
- `comparison_page.json` — Product A vs Product B comparison  

All outputs are **CMS- and frontend-friendly** and designed for downstream consumption.

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

### 2. Set environment variables
GROQ_API_KEY=your_api_key_here

### 3. Run the system

python main.py

Successful execution will generate the output JSON files inside the outputs/ directory.


