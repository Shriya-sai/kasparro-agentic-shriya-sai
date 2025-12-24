"""
QuestionGenerationAgent (LLM-backed)

Uses LangChain + Gemini to generate categorized customer questions.
Includes memory and programmatic validation.
"""

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
            input_variables=["product_name", "category"],
            template="""
You are an AI agent generating customer FAQ questions for a product.

Product Name: {product_name}
Category: {category}

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
        response = self.chain.run(
            product_name=product["name"],
            category=product["category"]
        )

        try:
            data = FAQSchema.parse_raw(response)
        except ValidationError as e:
            raise ValueError(f"Invalid FAQ JSON generated: {e}")

        total_questions = sum(len(v) for v in data.dict().values())
        if total_questions < 15:
            raise ValueError("FAQ generation failed to meet minimum question count")

        return data.dict()
