"""
ContentLogicAgent

Responsibility:
- Provide reusable content logic blocks
- Generate structured content sections from internal product schema
- Remain independent of page templates and orchestration
"""

class ContentLogicAgent:
    def __init__(self):
        pass

    def generate_overview_block(self, product: dict) -> dict:
        return {
            "title": "Product Overview",
            "content": {
                "name": product.get("name"),
                "brand": product.get("brand"),
                "category": product.get("category")
            }
        }

    def generate_benefits_block(self, product: dict) -> dict:
        return {
            "title": "Key Benefits",
            "items": product.get("benefits", [])
        }

    def generate_usage_block(self, product: dict) -> dict:
        return {
            "title": "How to Use",
            "instructions": product.get("usage")
        }

    def generate_safety_block(self, product: dict) -> dict:
        return {
            "title": "Safety & Side Effects",
            "notes": product.get("side_effects"),
            "skin_type": product.get("skin_type", [])
        }

    def generate_pricing_block(self, product: dict) -> dict:
        return {
            "title": "Pricing",
            "price_inr": product.get("price_inr")
        }

    def generate_comparison_block(self, product_a: dict, product_b: dict) -> dict:
        return {
            "title": "Product Comparison",
            "comparison": {
                "product_a": {
                    "name": product_a.get("name"),
                    "price_inr": product_a.get("price_inr"),
                    "ingredients": product_a.get("ingredients"),
                    "benefits": product_a.get("benefits")
                },
                "product_b": {
                    "name": product_b.get("name"),
                    "price_inr": product_b.get("price_inr"),
                    "ingredients": product_b.get("ingredients"),
                    "benefits": product_b.get("benefits")
                }
            }
        }
