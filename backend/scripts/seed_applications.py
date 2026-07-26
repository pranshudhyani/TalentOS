from app.db.session import SessionLocal
from app.models.application import Application

db = SessionLocal()

applications = [
    Application(
        candidate_id=1,
        job_id=1,
        status="Applied",
    ),
    Application(
        candidate_id=1,
        job_id=3,
        status="Interview",
    ),
    Application(
        candidate_id=2,
        job_id=2,
        status="Applied",
    ),
    Application(
        candidate_id=3,
        job_id=1,
        status="Rejected",
    ),
]

db.add_all(applications)
db.commit()

print("Applications seeded!")

db.close()