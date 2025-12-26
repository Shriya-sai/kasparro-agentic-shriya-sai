import logging
from agents.question_generator import QuestionGenerationAgent


def faq_generation_node(state: dict) -> dict:
    logging.info("FAQ Agent started")

    try:
        agent = QuestionGenerationAgent()
        state["faqs"] = agent.generate(state["product"])
    except Exception as e:
        state["errors"].append(str(e))

    return state
