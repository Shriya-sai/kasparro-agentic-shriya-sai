import logging
from graph.workflow import build_graph
from data.product_input import PRODUCT_A


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

def main():
    graph = build_graph()

    initial_state = {
        "product": PRODUCT_A,
        "faqs": None,
        "product_page": None,
        "comparison_page": None,
        "errors": []
    }

    graph.invoke(initial_state)
    print("✅ Pipeline completed")

if __name__ == "__main__":
    main()
