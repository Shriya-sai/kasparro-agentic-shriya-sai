"""
QuestionGenerationAgent (LLM-backed)

Uses LangChain + Gemini to generate categorized customer questions.
Includes memory and programmatic validation.
"""
import json
import re

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel, ValidationError
from typing import List, Dict


class FAQSchema(BaseModel):
    Informational: List[str]
    Usage: List[str]
    Safety: List[str]
    Purchase: List[str]
    Comparison: List[str]


class QuestionGenerationAgent:
    def __init__(self, llm):
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        self.prompt = PromptTemplate(
            input_variables=["input"],
            template="""
You are an AI agent generating customer FAQ questions for a product.

Product Information:
{input}

Generate at least 15 total customer questions, grouped strictly into the following categories:
- Informational
- Usage
- Safety
- Purchase
- Comparison

Rules:
- Each category must contain at least 3 questions
- Output MUST be valid JSON
- Do not include explanations or extra text

JSON format:
{{
  "Informational": ["..."],
  "Usage": ["..."],
  "Safety": ["..."],
  "Purchase": ["..."],
  "Comparison": ["..."]
}}
"""
        )

        self.chain = LLMChain(
            llm=llm,
            prompt=self.prompt,
            memory=self.memory
        )

    def generate(self, product: dict) -> Dict:
        input_text = f"Name: {product['name']}\nCategory: {product['category']}"

        raw_response = self.chain.run(input=input_text)

        # --- QUALITY GATE: Extract FAQ JSON only ---
        json_match = re.search(
           r'\{\s*"Informational"\s*:.*?\}\s*$',
           raw_response,
           re.DOTALL
        )

        if not json_match:
           raise ValueError("LLM did not return valid FAQ JSON block")

        json_str = json_match.group(0)

        try:
           data = FAQSchema.parse_raw(json_str)
        except ValidationError as e:
           raise ValueError(f"Invalid FAQ JSON generated: {e}")

        total_questions = sum(len(v) for v in data.dict().values())
        if total_questions < 15:
           raise ValueError("FAQ generation failed to meet minimum question count")

        return data.dict()
