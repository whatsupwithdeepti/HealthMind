from typing import List, Dict

def summarize_checkins(checkins: List[Dict]) -> str:
    if not checkins:
        return "No recent activity."
    
    avg_sleep = sum(c["sleep_hours"] for c in checkins) / len(checkins)
    avg_stress = sum(c["stress"] for c in checkins) / len(checkins)
    avg_mood = sum(c["mood"] for c in checkins) / len(checkins)

    return(
        f"Over your recent check-ins, you averaged {avg_sleep:.1f} hours of sleep, "
        f"with a stress level of {avg_stress:.1f} and a mood rating of {avg_mood:.1f}."
    )