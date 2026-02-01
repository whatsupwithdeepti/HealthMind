from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router
from app.api.checkin import router as checkin_router

app = FastAPI(
    title="HealthMind API",
    description="Backend service for HealthMind",
    version="0.1.0"
)
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(checkin_router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}