from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.fastapi_backend.middleware import setup_logging
from src.fastapi_backend.routes.health import router as health_router
import logging

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permissive for MVP
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
# Logging Middleware
setup_logging(app)

# Routes
app.include_router(health_router)
