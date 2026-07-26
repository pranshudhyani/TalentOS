from fastapi import HTTPException

from app.repositories.application_repository import ApplicationRepository
from app.repositories.candidate_repository import CandidateRepository
from app.repositories.job_repository import JobRepository

from app.schemas.application import (
    ApplicationCreate,
    ApplicationUpdate,
)


class ApplicationService:

    def __init__(
        self,
        application_repository: ApplicationRepository,
        candidate_repository: CandidateRepository,
        job_repository: JobRepository,
    ):
        self.application_repository = application_repository
        self.candidate_repository = candidate_repository
        self.job_repository = job_repository

    def create_application(self, application: ApplicationCreate):

        candidate = self.candidate_repository.get_by_id(
            application.candidate_id
        )

        if candidate is None:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found",
            )

        job = self.job_repository.get_by_id(
            application.job_id
        )

        if job is None:
            raise HTTPException(
                status_code=404,
                detail="Job not found",
            )

        return self.application_repository.create(application)

    def get_applications(self):
        return self.application_repository.get_all()

    def get_application(self, application_id: int):
        return self.application_repository.get_by_id(application_id)

    def update_application(
        self,
        application_id: int,
        application: ApplicationUpdate,
    ):
        return self.application_repository.update(
            application_id,
            application,
        )

    def delete_application(self, application_id: int):
        return self.application_repository.delete(application_id)