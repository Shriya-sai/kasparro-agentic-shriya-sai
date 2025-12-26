# Kasparro Applied AI Engineer Challenge  
## Multi-Agent Content Generation System

This repository contains a **modular, agent-based content generation system** designed to transform raw product data into structured, reusable marketing content.

The focus of this project is **system design, explicit orchestration, validation, and reusability** — not prompt-heavy or monolithic AI scripts.

---

## 🎯 Objective

Design a production-oriented **agentic content system** that:

- Uses clear agent boundaries  
- Exposes reusable logic blocks  
- Orchestrates execution explicitly using a framework  
- Applies validation and quality gates  
- Produces structured, deterministic outputs from non-deterministic LLMs  

---

## 🧠 System Overview

The system is composed of multiple agents, each with a single responsibility:

| Component | Description |
|---------|-------------|
| **ProductParserAgent** | Normalizes raw product input into a stable internal schema |
| **QuestionGenerationAgent** | Uses a LangChain-backed LLM (Groq-hosted LLaMA 3.1) to generate categorized customer FAQs with schema validation |
| **ValidationAgent** | Enforces output schema correctness and minimum FAQ count |
| **ContentLogicAgent** | Produces reusable, deterministic content blocks |
| **TemplateAgent** | Assembles page-level outputs from reusable blocks |
| **LangGraph Orchestrator** | Controls execution flow, shared state, and agent coordination |
| **main.py** | Entry point for end-to-end execution |

All agents are coordinated through an **explicit LangGraph orchestration layer**, rather than implicit chaining or sequential scripts.

---

## 🤖 LLM & Agent Architecture

The system uses **LangGraph for orchestration** and **LangChain for LLM integration**, with a **Groq-hosted LLaMA 3.1 model** for generative tasks.

### Key characteristics

- Non-deterministic LLM outputs are constrained using:
  - Structured prompts  
  - Pydantic-based JSON schema validation  
  - Quality gates (minimum FAQ count enforcement)
- LLM usage is isolated strictly to generative tasks
- Validation, enforcement, templating, and orchestration are handled deterministically

This mirrors real-world applied AI systems where **LLMs are components, not the system itself**.

---

## 🔁 Execution Flow

Raw Product Input
↓
ProductParserAgent
↓
QuestionGenerationAgent (LLM-backed)
↓
ValidationAgent (Schema + Quality Gates)
↓
ContentLogicAgent (Reusable Blocks)
↓
TemplateAgent
↓
Structured JSON Outputs


The execution flow is implemented as a **LangGraph state graph**, not a simple sequential Python script.

---

## 📂 Project Structure

kasparro-agentic-shriya-sai/
│
├── agents/ # Agent implementations
├── graph/ # LangGraph workflow and nodes
├── templates/ # Output templates
├── data/ # Raw product input data
├── outputs/ # Generated JSON outputs
├── docs/ # System documentation
├── main.py # Entry point
└── README.md


---

## 📦 Outputs

Running the system generates the following structured outputs:

- `faq.json` — Categorized customer FAQs  
- `product_page.json` — Product overview and details  
- `comparison_page.json` — Product comparison output  

All outputs are **JSON-only**, CMS- and frontend-friendly, and designed for downstream consumption.

LLM failures currently fail fast to surface quality issues; retry policies can be added at the orchestration layer if required.

---

## 🧪 Testing & Validation

The system is tested at the **pipeline level**, focusing on correctness, robustness, and reproducibility rather than isolated unit tests.

### End-to-End Execution Test

The primary test is running the full orchestration pipeline:

```bash
python main.py
```
Successful execution confirms that:

All agents are wired correctly

LangGraph orchestration executes without errors

LLM-backed and deterministic agents interact as expected

Structured output artifacts are generated

▶️ How to Run
1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Set environment variables

Create a .env file in the project root:

GROQ_API_KEY=your_api_key_here


(or export the variable directly)

3. Run the system
```bash
python main.py
```


Successful execution will generate output JSON files inside the outputs/ directory and log each agent’s execution.

🧩 Design Notes

The system prioritizes clarity over cleverness

Agents are intentionally small, composable, and framework-backed

Orchestration and state transitions are explicit and inspectable

Validation and failure handling are first-class concerns

The architecture is designed to be extended (new agents, branching flows, alternate LLMs)