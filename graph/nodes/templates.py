import json
import logging
from pathlib import Path

OUTPUT_DIR = Path("outputs")

def template_node(state: dict) -> dict:
    logging.info("Template agent started")

    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(OUTPUT_DIR / "faq.json", "w") as f:
        json.dump(state["faqs"], f, indent=2)

    with open(OUTPUT_DIR / "product_page.json", "w") as f:
        json.dump(state["product_page"], f, indent=2)

    return state
