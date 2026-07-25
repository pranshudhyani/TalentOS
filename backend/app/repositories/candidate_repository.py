from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate
from app.schemas.candidate import CandidateUpdate

class CandidateRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, candidate: CandidateCreate):

        db_candidate = Candidate(
            name=candidate.name,
            email=candidate.email,
            phone=candidate.phone,
            years_of_experience=candidate.years_of_experience,
            skills=candidate.skills,
            linkedin_url=str(candidate.linkedin_url) if candidate.linkedin_url else None,
            github_url=str(candidate.github_url) if candidate.github_url else None,
        )

        self.db.add(db_candidate)
        self.db.commit()
        self.db.refresh(db_candidate)

        return db_candidate

    def get_all(self):

        return self.db.query(Candidate).all()

    def get_by_id(self, candidate_id: int):

        return (
            self.db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )
    
    def update(self, candidate_id: int, candidate: CandidateUpdate):

        db_candidate = (
            self.db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )

        if not db_candidate:
            return None

        update_data = candidate.model_dump(
            exclude_unset=True,
            mode="json"
        )

        for key, value in update_data.items():
            setattr(db_candidate, key, value)

        self.db.commit()
        self.db.refresh(db_candidate)

        return db_candidate


    def delete(self, candidate_id: int):

        candidate = (
            self.db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )

        if not candidate:
            return None

        self.db.delete(candidate)
        self.db.commit()

        return candidate