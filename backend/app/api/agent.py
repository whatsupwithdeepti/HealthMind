from fastapi import APIRouter
from app.agents.health_agent import build_health_agent

router = APIRouter(prefix="/agent", tags=["agent"])

agent = build_health_agent()


@router.post("/ask")
def ask_agent(user_input: str):
    state = {
        "user_input": user_input,
        "memories": [],
        "analysis": "",
        "decision": "",
        "response": "",
    }

    result = agent.invoke(state)
    return {"response": result["response"]}
