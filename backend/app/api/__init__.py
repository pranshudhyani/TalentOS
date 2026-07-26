from app.api.health import router as health_router
from app.api.candidate import router as candidate_router
from app.api.application import router as application_router

__all__ = [
    "health_router",
    "candidate_router",
    "application_router",
]