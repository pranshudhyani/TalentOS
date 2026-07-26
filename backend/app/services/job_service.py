from app.repositories.job_repository import JobRepository
from app.schemas.job import JobCreate, JobUpdate


class JobService:

    def __init__(self, repository: JobRepository):
        self.repository = repository

    def create_job(self, job: JobCreate):
        return self.repository.create(job)

    def get_jobs(self):
        return self.repository.get_all()

    def get_job(self, job_id: int):
        return self.repository.get_by_id(job_id)

    def update_job(self, job_id: int, job: JobUpdate):
        return self.repository.update(job_id, job)

    def delete_job(self, job_id: int):
        return self.repository.delete(job_id)