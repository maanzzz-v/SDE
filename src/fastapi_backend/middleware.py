# middleware.py
import logging
import time
from fastapi import FastAPI, Request

api_logger = logging.getLogger("api")

def setup_logging(app: FastAPI):
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        api_logger.info(f"{request.method} {request.url.path} - {response.status_code} - {duration:.4f}s")
        return response
