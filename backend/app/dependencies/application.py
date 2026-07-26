from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.repositories.application_repository import ApplicationRepository
from app.repositories.candidate_repository import CandidateRepository
from app.repositories.job_repository import JobRepository

from app.services.application_service import ApplicationService


def get_application_service(
    db: Session = Depends(get_db),
) -> ApplicationService:

    application_repository = ApplicationRepository(db)
    candidate_repository = CandidateRepository(db)
    job_repository = JobRepository(db)

    return ApplicationService(
        application_repository,
        candidate_repository,
        job_repository,
    )