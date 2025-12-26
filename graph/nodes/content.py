import logging

def content_node(state: dict) -> dict:
    logging.info("Content logic agent started")

    state["outputs"] = {
        "product_page": {
            "name": state["product"]["name"],
            "category": state["product"]["category"],
            "faqs": state["faqs"]
        },
        "faq": state["faqs"],
        "comparison_page": {
            "product": state["product"]["name"],
            "competitor": "Competitor Product",
            "summary": "Comparison content generated"
        }
    }

    return state
