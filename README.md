Kasparro Applied AI Engineer Challenge
LangGraph-based Multi-Agent Content Generation System

This repository contains a LangGraph-orchestrated, agent-based content generation system that transforms raw product data into structured, reusable marketing outputs.

The system demonstrates real agent orchestration, explicit state management, validation, and controlled LLM usage, aligned with production-style applied AI systems.

🎯 Objective

Design a production-oriented agentic content system that:

Uses a framework-based orchestration layer (LangGraph)

Defines clear agent responsibilities

Passes and mutates explicit shared state

Integrates LLM-based reasoning where appropriate

Applies validation and quality gates

Produces structured, deterministic outputs from non-deterministic LLMs

🧠 System Overview

The system is composed of multiple agents, each implemented as a LangGraph node with a single responsibility:

Component	Responsibility
ProductParserAgent	Normalizes raw product input into a stable internal schema
QuestionGenerationAgent	Uses a Groq-hosted LLaMA 3.1 LLM (via LangChain) to generate categorized customer FAQs
ValidationAgent	Enforces schema validity and minimum FAQ count constraints
ContentLogicAgent	Produces reusable, deterministic content blocks
TemplateAgent	Assembles page-level JSON outputs
Orchestrator (LangGraph)	Controls execution flow, state transitions, and agent coordination
main.py	Entry point for end-to-end execution

All agents operate on a shared LangGraph state object, ensuring explicit data flow and traceability.

🤖 LLM & Agent Architecture

Framework: LangGraph (stateful agent orchestration)

LLM Integration: LangChain + Groq (LLaMA 3.1)

LLM Usage Scope: Limited strictly to generative tasks (FAQ creation)

Deterministic Logic: Validation, enforcement, templating, and orchestration are handled outside the LLM

Output Control Mechanisms

Non-deterministic LLM outputs are constrained using:

Structured prompts

Pydantic schema validation

Minimum question count enforcement

Explicit failure handling in the graph

This mirrors real-world applied AI systems where LLMs are components, not the system itself.

🔁 Execution Flow
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


The flow is implemented as a LangGraph state graph, not a sequential Python script.

📂 Project Structure
kasparro-agentic-shriya-sai/
│
├── agents/        # Agent implementations
├── graph/         # LangGraph workflow and nodes
├── templates/     # Output templates
├── data/          # Raw product input data
├── outputs/       # Generated JSON outputs
├── docs/          # Documentation
├── main.py        # Entry point
└── README.md

📦 Outputs

Running the system generates:

faq.json — Categorized customer FAQs

product_page.json — Product overview content

comparison_page.json — Product comparison output

All outputs are JSON-only, CMS- and frontend-ready.

▶️ How to Run
1. Install dependencies
pip install -r requirements.txt

2. Set environment variables
export GROQ_API_KEY=your_api_key_here


(or use a .env file)

3. Run the pipeline
python main.py


Successful execution logs each agent step and ends with:

✅ Pipeline completed

🧪 Testing & Validation

The system is tested at the pipeline level, focusing on correctness, robustness, and reproducibility.

Validation includes:

Pydantic schema validation of LLM outputs

Enforcement of minimum FAQ count

Controlled failure propagation through LangGraph state

Deterministic output structure

This approach reflects real applied AI systems, where integration correctness matters more than isolated unit tests.

🧩 Design Notes

The system prioritizes clarity over cleverness

Agents are small, composable, and framework-backed

Orchestration is explicit and inspectable

The architecture is designed for extension (new agents, branching flows, alternate LLMs)

✅ Status

This implementation uses real LangGraph orchestration, real LLM execution, and explicit validation, addressing all Phase 1 evaluation concerns.

End of README