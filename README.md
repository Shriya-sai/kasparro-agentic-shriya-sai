# Kasparro Applied AI Engineer Challenge
Multi-Agent Content Generation System

This repository contains a modular, agent-based content generation system that transforms raw product data into structured marketing content.

The focus of this project is system design, reusable logic blocks, and explicit orchestration rather than prompt-heavy or monolithic AI scripts.

---

## Objective

Design a production-oriented agentic content system that:
- Uses clear agent responsibilities
- Exposes reusable content logic
- Orchestrates execution explicitly
- Produces structured, deterministic outputs

---

## System Overview

The system is composed of multiple agents, each with a single responsibility.

ProductParserAgent  
Normalizes raw product input into an internal schema.

QuestionGenerationAgent  
Generates categorized customer questions.

ContentLogicAgent  
Produces reusable content blocks.

TemplateAgents  
Assemble page-level outputs.

OrchestratorAgent  
Controls execution flow.

main.py  
Entry point for system execution.

---

## Execution Flow

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

yaml
Copy code

---

## Project Structure

kasparro-agentic-shriya-sai/
├── agents/
├── templates/
├── data/
├── outputs/
├── docs/
├── main.py
└── README.md

yaml
Copy code

---

## Outputs

The system generates three structured JSON files:

faq.json  
product_page.json  
comparison_page.json  

These outputs are designed for consumption by CMS systems or frontend applications.

---

## How to Run

python main.py

yaml
Copy code

Generated outputs will appear in the outputs directory.

---

## Design Philosophy

The system prioritizes:

Separation of concerns over monolithic scripts.  
Reusable content logic over page-specific generation.  
Explicit orchestration over implicit control flow.  
Extensible architecture that can support LLM-backed agents later.

---

## Documentation

Detailed system design and architectural decisions are available in:

docs/projectdocumentation.md

yaml
Copy code

---

## Closing Note

This project focuses on engineering clarity, maintainability, and system thinking.  
It is intentionally designed to be understandable, extensible, and production-friendly.