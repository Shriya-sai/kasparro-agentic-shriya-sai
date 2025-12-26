from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional

from graph.nodes.parser import parser_node
from graph.nodes.faq_agent import faq_generation_node
from graph.nodes.validation import faq_validation_node
from graph.nodes.content import content_node
from graph.nodes.templates import template_node


class GraphState(TypedDict):
    product: dict
    faqs: Optional[dict]
    outputs: dict
    errors: list[str]


"""
LangGraph State Schema:

state = {
    "product": dict,        # Parsed product data
    "faqs": dict | None,    # Generated FAQs
    "outputs": dict,        # Final JSON outputs
    "errors": list[str]     # Collected errors
}
"""
def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("parser", parser_node)
    graph.add_node("faq", faq_generation_node)
    graph.add_node("validate", faq_validation_node)
    graph.add_node("content", content_node)
    graph.add_node("templates", template_node)

    graph.set_entry_point("parser")

    graph.add_edge("parser", "faq")
    graph.add_edge("faq", "validate")

    graph.add_conditional_edges(
        "validate",
        lambda state: "retry" if state["errors"] else "ok",
        {
            "retry": "faq",
            "ok": "content"
        }
    )

    graph.add_edge("content", "templates")
    graph.add_edge("templates", END)

    return graph.compile()
