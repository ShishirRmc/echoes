import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.endpoints import quotes as quotes_v1_router
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up Quote API...")
    yield
    # Shutdown
    logger.info("Shutting down Quote API...")


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "OK"}


# Include version 1 API router
app.include_router(
    quotes_v1_router.router, prefix=settings.API_V1_STR, tags=["Quotes V1"]
)


# Root endpoint
@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint that provides API information.
    """
    return {
        "app_name": settings.APP_NAME,
        "version": "1.0",
        "description": "A FastAPI service providing inspirational quotes",
        "docs_url": "/docs",
        "endpoints": {
            "health": "/health",
            "quotes_v1": {
                "random_quote": f"{settings.API_V1_STR}/quote",
                "all_quotes": f"{settings.API_V1_STR}/quotes",
            },
        },
    }
    return {"message": f"Welcome to {settings.APP_NAME}"}
