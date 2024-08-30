from fastapi import FastAPI
from src.controllers import router

app = FastAPI(
    title = "AI Fraud Detector",
    description="This is a simple API to detect fraud in transactions using AI",
    version='1.0.0'
)
app.include_router(router)