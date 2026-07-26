print("Starting job_repository")
from sqlalchemy.orm import Session
print("Imported Session")
from app.models.job import Job
print("Imported job")
from app.schemas.job import JobCreate
from app.schemas.job import JobUpdate


class JobRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, job: JobCreate):

        db_job = Job(
            title=job.title,
            company=job.company,
            location=job.location,
            salary=job.salary,
            description=job.description,
        )

        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)

        return db_job

    def get_all(self):

        return self.db.query(Job).all()

    def get_by_id(self, job_id: int):

        return (
            self.db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

    def update(self, job_id: int, job: JobUpdate):

        db_job = (
            self.db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

        if not db_job:
            return None

        update_data = job.model_dump(
            exclude_unset=True,
            mode="json"
        )

        for key, value in update_data.items():
            setattr(db_job, key, value)

        self.db.commit()
        self.db.refresh(db_job)

        return db_job

    def delete(self, job_id: int):

        db_job = (
            self.db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

        if not db_job:
            return None

        self.db.delete(db_job)
        self.db.commit()

        return db_job