from app.db.session import SessionLocal
from app.models.candidate import Candidate

db = SessionLocal()

candidates = [
    Candidate(
        name="Alice Johnson",
        email="alice@test.com",
        phone="9999999991",
        years_of_experience=4,
        skills=["Python", "FastAPI"],
        linkedin_url="https://linkedin.com/in/alice",
        github_url="https://github.com/alice",
    ),
    Candidate(
        name="Bob Smith",
        email="bob@test.com",
        phone="9999999992",
        years_of_experience=6,
        skills=["Azure", "SQL"],
        linkedin_url="https://linkedin.com/in/bob",
        github_url="https://github.com/bob",
    ),
    Candidate(
        name="Charlie Brown",
        email="charlie@test.com",
        phone="9999999993",
        years_of_experience=2,
        skills=["React", "TypeScript"],
        linkedin_url="https://linkedin.com/in/charlie",
        github_url="https://github.com/charlie",
    ),
]

db.add_all(candidates)
db.commit()

print("Candidates seeded!")

db.close()