import logging
from tools.faq_tools import validate_faq_count

def faq_validation_node(state: dict) -> dict:
    logging.info("Validation agent started")

    if not state.get("faqs") or not validate_faq_count(state["faqs"]):
        state["errors"].append("FAQ validation failed")

    return state
