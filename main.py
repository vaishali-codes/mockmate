from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="PrepMate AI",
    description="AI-powered mock interviewer",
    vrsion="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "PrepMate AI is running!",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}