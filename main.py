from fastapi import FastAPI


from app.config import settings

from app.routers.auth import router as auth_router

app = FastAPI(
    title="PrepMate AI",
    description="AI-powered mock interviewer",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "PrepMate AI is running!",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}