"""
Entry point for the Multi-Agent Content Generation System
"""

import json
import os

from data.product_input import PRODUCT_A, PRODUCT_B
from agents.orchestrator import OrchestratorAgent


def write_output(filename: str, data: dict):
    os.makedirs("outputs", exist_ok=True)
    path = os.path.join("outputs", filename)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Generated {filename}")


def main():
    orchestrator = OrchestratorAgent()

    results = orchestrator.run(
        raw_product_a=PRODUCT_A,
        raw_product_b=PRODUCT_B
    )

    write_output("faq.json", results["faq"])
    write_output("product_page.json", results["product_page"])
    write_output("comparison_page.json", results["comparison_page"])


if __name__ == "__main__":
    main()
