from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import quotes as quotes_v1_router
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.APP_NAME)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Quote API...")
    # You can load resources here, e.g., quote_service._load_quotes()
    # to ensure data is ready or connections are established.

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Quote API...")

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "OK"}

# Include version 1 API router
app.include_router(quotes_v1_router.router, prefix=settings.API_V1_STR, tags=["Quotes V1"])

# Root endpoint (optional)
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
