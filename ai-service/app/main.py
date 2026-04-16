from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="PhishGuard AI Service",
    version="0.1.0",
    description="MVP phishing URL risk scoring service.",
)

app.include_router(router)
