from fastapi import FastAPI

app = FastAPI(
    title="HealthMind API",
    description="Backend service for HealthMind",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}