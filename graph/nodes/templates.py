import json
import os
import logging

OUTPUT_DIR = "outputs"


def template_node(state: dict) -> dict:
    logging.info("Template agent started")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    outputs = state.get("outputs", {})

    with open(f"{OUTPUT_DIR}/product_page.json", "w") as f:
        json.dump(outputs.get("product_page", {}), f, indent=2)

    with open(f"{OUTPUT_DIR}/faq.json", "w") as f:
        json.dump(outputs.get("faq", {}), f, indent=2)

    with open(f"{OUTPUT_DIR}/comparison_page.json", "w") as f:
        json.dump(outputs.get("comparison_page", {}), f, indent=2)

    return state
