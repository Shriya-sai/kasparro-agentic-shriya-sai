"""
OrchestratorAgent

Responsibility:
- Coordinate execution of all agents
- Manage data flow
- Produce final structured outputs
"""

from agents.product_parser import ProductParserAgent
from agents.question_generator import QuestionGenerationAgent
from agents.content_logic import ContentLogicAgent

from templates.faq_template import FAQTemplate
from templates.product_template import ProductPageTemplate
from templates.comparison_template import ComparisonPageTemplate


class OrchestratorAgent:
    def __init__(self):
        self.product_parser = ProductParserAgent()
        self.question_generator = QuestionGenerationAgent()
        self.content_logic = ContentLogicAgent()

        self.faq_template = FAQTemplate()
        self.product_template = ProductPageTemplate()
        self.comparison_template = ComparisonPageTemplate()

    def run(self, raw_product_a: dict, raw_product_b: dict) -> dict:
        # Step 1: Parse raw product data
        product_a = self.product_parser.parse(raw_product_a)
        product_b = self.product_parser.parse(raw_product_b)

        # Step 2: Generate questions
        questions = self.question_generator.generate(product_a)

        # Step 3: Generate reusable content blocks
        overview_block = self.content_logic.generate_overview_block(product_a)
        benefits_block = self.content_logic.generate_benefits_block(product_a)
        usage_block = self.content_logic.generate_usage_block(product_a)
        safety_block = self.content_logic.generate_safety_block(product_a)
        pricing_block = self.content_logic.generate_pricing_block(product_a)

        comparison_block = self.content_logic.generate_comparison_block(
            product_a, product_b
        )

        # Step 4: Assemble pages using templates
        faq_page = self.faq_template.assemble(questions)

        product_page = self.product_template.assemble([
            overview_block,
            benefits_block,
            usage_block,
            safety_block,
            pricing_block
        ])

        comparison_page = self.comparison_template.assemble(comparison_block)

        return {
            "faq": faq_page,
            "product_page": product_page,
            "comparison_page": comparison_page
        }
