from pydantic import BaseModel
from typing import Optional

class HealthProfileCreate(BaseModel):
    sleep_goal_hours: Optional[int] = None
    stress_level: Optional[int] = None
    focus_goal: Optional[str] = None
    