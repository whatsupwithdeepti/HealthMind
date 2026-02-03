from fastapi import APIRouter
from app.schemas.checkin import DailyCheckIn
from app.models.checkin import user_checkins
from app.memory.summarizer import summarize_checkins
from app.memory.store import add_to_memory

router = APIRouter(prefix="/checkin", tags=["checkin"])

@router.post("/")
def submit_checkin(
    checkin: DailyCheckIn,
    user_email: str = "demo_user@example.com"
):
    user_checkins.setdefault(user_email, []).append(checkin.dict())

    summary = summarize_checkins(user_checkins[user_email])

    dummy_embedding = [0.0] * 384
    add_to_memory(dummy_embedding, summary)

    return {"message": "Check-in recorded", "summary": summary}