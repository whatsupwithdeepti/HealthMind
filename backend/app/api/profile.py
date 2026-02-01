from fastapi import APIRouter, Depends
from app.schemas.profile import HealthProfileCreate
from app.models.profile import user_profiles

router = APIRouter(prefix='/profile', tags=['profile'])

@router.post("/")
def create_or_update_profile(
    profile: HealthProfileCreate,
    user_email: str = "demo_user@example.com"
):
    user_profiles[user_email] = profile.dict()
    return {"messages": "Profile saved", "profile": user_profiles[user_email]}
