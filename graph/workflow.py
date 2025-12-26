from langgraph.graph import StateGraph, END
from graph.state import AgentState

from graph.nodes.parser import parser_node
from graph.nodes.faq_agent import faq_generation_node
from graph.nodes.validation import faq_validation_node
from graph.nodes.content import content_node
from graph.nodes.templates import template_node

def build_graph():
    graph = StateGraph(AgentState)

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
