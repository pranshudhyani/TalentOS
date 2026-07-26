from sqlalchemy.orm import Session

from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationUpdate


class ApplicationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, application: ApplicationCreate):

        db_application = Application(
            candidate_id=application.candidate_id,
            job_id=application.job_id,
            status=application.status,
        )

        self.db.add(db_application)
        self.db.commit()
        self.db.refresh(db_application)

        return db_application

    def get_all(self):

        return self.db.query(Application).all()

    def get_by_id(self, application_id: int):

        return (
            self.db.query(Application)
            .filter(Application.id == application_id)
            .first()
        )

    def update(self, application_id: int, application: ApplicationUpdate):

        db_application = (
            self.db.query(Application)
            .filter(Application.id == application_id)
            .first()
        )

        if not db_application:
            return None

        update_data = application.model_dump(
            exclude_unset=True,
            mode="json"
        )

        for key, value in update_data.items():
            setattr(db_application, key, value)

        self.db.commit()
        self.db.refresh(db_application)

        return db_application

    def delete(self, application_id: int):

        db_application = (
            self.db.query(Application)
            .filter(Application.id == application_id)
            .first()
        )

        if not db_application:
            return None

        self.db.delete(db_application)
        self.db.commit()

        return db_application
