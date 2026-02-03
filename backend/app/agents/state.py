from typing import TypedDict, List

class HealthState(TypedDict):
    user_input: str
    memories: List[str]
    analysis: str
    decision: str
    response: str
    