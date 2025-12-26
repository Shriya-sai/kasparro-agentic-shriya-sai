from dotenv import load_dotenv
load_dotenv()

from typing import Dict
import json
import re

from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, ValidationError


class FAQSchema(BaseModel):
    Informational: list[str]
    Usage: list[str]
    Safety: list[str]
    Purchase: list[str]
    Comparison: list[str]


class QuestionGenerationAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.7,
        )

        self.prompt = PromptTemplate(
            input_variables=["product"],
            template="""
You are an AI agent generating customer FAQ questions for a product.

Product information:
{product}

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

        # LangChain 0.3 style runnable
        self.chain = self.prompt | self.llm

    def generate(self, product: Dict) -> Dict:
        response = self.chain.invoke(
            {"product": json.dumps(product, indent=2)}
        )

        text = response.content

        # Extract JSON safely
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise ValueError("LLM did not return valid JSON")

        try:
            parsed = FAQSchema.model_validate_json(match.group())
        except ValidationError as e:
            raise ValueError(f"Invalid FAQ JSON: {e}")

        total = sum(len(v) for v in parsed.model_dump().values())
        if total < 15:
            raise ValueError("FAQ count < 15")

        return parsed.model_dump()
