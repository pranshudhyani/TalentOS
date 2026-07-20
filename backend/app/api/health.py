from fastapi import APIRouter
from app.config.settings import settings

router = APIRouter(tags=["Health"])


@router.get("/health", summary="System Health Check")
def health_check():
    """Diagnostic health probe returning status, app name, and environment."""
    return {
        "status": "healthy",
        "app": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "env": settings.ENV,
    }
