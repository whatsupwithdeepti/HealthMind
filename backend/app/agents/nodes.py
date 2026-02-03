from app.agents.state import HealthState
from app.memory.embeddings import embed_texts
from app.memory.store import retrieve_similar_memories

def retrieve_memory_node(state: HealthState) -> HealthState:
    embedding = embed_texts(state["user_input"])
    memories = retrieve_similar_memories(embedding)
    state["memories"] = memories
    return state

def analyze_behavior_node(state: HealthState) -> HealthState:
    if not state["memories"]:
        state["analysis"] = "No significant past patterns detected."
    else:
        state["analysis"] = (
            "User shows recurring patterns related to sleep, stress, or mood."
        )
    return state


def decision_node(state: HealthState) -> HealthState:
    if "stress" in state["analysis"].lower():
        state["decision"] = "suggest stress reduction"
    else:
        state["decision"] = "maintain routine"
    return state


def response_node(state: HealthState) -> HealthState:
    state["response"] = (
        f"Based on your recent patterns, I recommend to {state['decision']}."
    )
    return state