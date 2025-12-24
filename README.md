# Kasparro Applied AI Engineer Challenge  
## Multi-Agent Content Generation System

This repository contains a **modular, agent-based content generation system** designed to transform raw product data into structured marketing content.

The focus of this project is **system design, orchestration, and reusability** — not prompt-heavy or monolithic AI scripts.

---

## 🎯 Objective

Design a production-oriented **agentic content system** that:
- Uses clear agent boundaries
- Exposes reusable logic blocks
- Orchestrates execution explicitly
- Produces structured, deterministic outputs

---

## 🧠 System Overview

The system is composed of multiple agents, each with a single responsibility:

| Component | Description |
|---------|-------------|
| ProductParserAgent | Normalizes raw product input into a stable internal schema |
| QuestionGenerationAgent | Generates categorized customer questions |
| ContentLogicAgent | Produces reusable content blocks |
| TemplateAgents | Assemble page-level outputs |
| OrchestratorAgent | Controls execution flow and data passing |
| main.py | Entry point for execution |

All agents are coordinated through an explicit orchestration layer.

---

## 🔁 Execution Flow

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

These outputs are designed to be **CMS- and frontend-friendly**.

---

## ▶️ How to Run

```bash
python main.py
