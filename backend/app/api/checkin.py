from fastapi import APIRouter
from app.schemas.checkin import DailyCheckIn
from app.models.checkin import user_checkins

router = APIRouter(prefix="/checkin", tags=["checkin"])

@router.post("/")
def submit_checkin(
    checkin: DailyCheckIn,
    user_email: str = "demo_user@example.com"
):
    user_checkins.setdefault(user_email, []).append(checkin.dict())
    return {"message": "Check-in recorded"}