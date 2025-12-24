"""
ProductParserAgent

Responsibility:
- Accept raw product input
- Normalize it into an internal, stable schema
- Shield downstream agents from raw input structure
"""

class ProductParserAgent:
    def __init__(self):
        pass

    def parse(self, raw_product: dict) -> dict:
        """
        Converts raw product data into internal product schema.
        """

        internal_product = {
            "name": raw_product.get("name"),
            "brand": raw_product.get("brand"),
            "category": raw_product.get("category"),
            "ingredients": raw_product.get("key_ingredients", []),
            "benefits": raw_product.get("benefits", []),
            "skin_type": raw_product.get("skin_type", []),
            "usage": raw_product.get("usage_instructions"),
            "side_effects": raw_product.get("side_effects"),
            "price_inr": raw_product.get("price_inr")
        }

        return internal_product
