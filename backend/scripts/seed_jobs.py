from app.db.session import SessionLocal
from app.models.job import Job

db = SessionLocal()

jobs = [
    Job(
        title="Backend Engineer",
        company="Google",
        location="Hyderabad",
        salary=2800000,
        description="Build scalable backend APIs.",
    ),
    Job(
        title="Data Engineer",
        company="Microsoft",
        location="Bangalore",
        salary=2400000,
        description="Build modern data pipelines.",
    ),
    Job(
        title="GenAI Engineer",
        company="OpenAI",
        location="Remote",
        salary=5000000,
        description="Develop production AI systems.",
    ),
]

db.add_all(jobs)
db.commit()

print("Jobs seeded!")

db.close()