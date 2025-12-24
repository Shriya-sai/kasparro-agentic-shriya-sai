"""
Comparison Page Template

Assembles comparison page using comparison block.
"""

class ComparisonPageTemplate:
    def __init__(self):
        pass

    def assemble(self, comparison_block: dict) -> dict:
        return {
            "page_type": "Comparison",
            "comparison": comparison_block
        }
