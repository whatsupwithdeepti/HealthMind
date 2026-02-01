from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DailyCheckIn(BaseModel):
    mood: int # 1-10
    sleep_hours: float
    stress: int # 1-10
    notes: Optional[str] = None
    timestamp: datetime = datetime.utcnow()