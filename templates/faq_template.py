"""
FAQ Template

Assembles FAQ page using generated questions.
"""

class FAQTemplate:
    def __init__(self):
        pass

    def assemble(self, questions: dict) -> dict:
        return {
            "page_type": "FAQ",
            "questions": questions
        }
