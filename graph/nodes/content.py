import logging

def content_node(state: dict) -> dict:
    logging.info("Content logic agent started")

    state["product_page"] = {
        "name": state["product"]["name"],
        "faqs": state["faqs"]
    }

    return state
