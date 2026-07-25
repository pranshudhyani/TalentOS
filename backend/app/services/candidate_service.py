from app.repositories.candidate_repository import CandidateRepository
from app.schemas.candidate import CandidateCreate
from app.schemas.candidate import CandidateUpdate


class CandidateService:

    def __init__(self, repository: CandidateRepository):
        self.repository = repository

    def create_candidate(self, candidate: CandidateCreate):
        return self.repository.create(candidate)

    def get_candidates(self):
        return self.repository.get_all()

    def get_candidate(self, candidate_id: int):
        return self.repository.get_by_id(candidate_id)

    def update_candidate(self, candidate_id: int, candidate: CandidateUpdate):
        return self.repository.update(candidate_id, candidate)

    def delete_candidate(self, candidate_id: int):
        return self.repository.delete(candidate_id)