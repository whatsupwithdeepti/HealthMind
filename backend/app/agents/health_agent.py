from langgraph.graph import StateGraph, END
from app.agents.state import HealthState
from app.agents.nodes import llm_response_node
from app.agents.nodes import (
    retrieve_memory_node,
    analyze_behavior_node,
    decision_node,
    llm_response_node,
)


def build_health_agent():
    graph = StateGraph(HealthState)

    graph.add_node("retrieve_memory", retrieve_memory_node)
    graph.add_node("analyze", analyze_behavior_node)
    graph.add_node("decide", decision_node)
    graph.add_node("respond", llm_response_node)

    graph.set_entry_point("retrieve_memory")
    graph.add_edge("retrieve_memory", "analyze")
    graph.add_edge("analyze", "decide")
    graph.add_edge("decide", "respond")
    graph.add_edge("respond", END)

    return graph.compile()
