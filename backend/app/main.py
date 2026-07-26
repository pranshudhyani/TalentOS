from fastapi import FastAPI
from app.config.settings import settings
from app.config.logging import setup_logging
from app.middleware.cors import setup_cors
from app.middleware.logging import RequestLoggingMiddleware
from app.api import health_router
from app.exceptions.handlers import register_exception_handlers
from app.api import job

# Initialize application logging configuration
setup_logging()

# Initialize FastAPI application with settings metadata
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="TalentOS AI Talent Platform API Engine",
    docs_url="/docs",
    redoc_url="/redoc",
)

register_exception_handlers(app)

# Attach Middlewares
setup_cors(app)
app.add_middleware(RequestLoggingMiddleware)


# Root Endpoint
@app.get("/", summary="Root Welcome Endpoint", tags=["Root"])
def read_root():
    """Welcome endpoint returning API metadata and navigational links."""
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "version": settings.VERSION,
        "docs": "/docs",
        "health": f"{settings.API_V1_STR}/health",
    }


# Mount API Routers
app.include_router(health_router,
prefix= settings.API_V1_STR)


from app.api import (
    health_router,
    candidate_router,
    application_router,
)

app.include_router(
    health_router,
    prefix=settings.API_V1_STR,
)

app.include_router(
    candidate_router,
    prefix=settings.API_V1_STR,
)

app.include_router(
    job.router,
    prefix=settings.API_V1_STR,
)

app.include_router(
    application_router,
    prefix=settings.API_V1_STR,
)