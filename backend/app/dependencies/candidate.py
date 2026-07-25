from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.candidate_repository import CandidateRepository
from app.services.candidate_service import CandidateService


def get_candidate_service(
    db: Session = Depends(get_db),
) -> CandidateService:

    repository = CandidateRepository(db)

    return CandidateService(repository)