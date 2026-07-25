from app.db.session import SessionLocal
from app.models.candidate import Candidate


print("hello from seed")
db = SessionLocal()

candidates = [
    Candidate(
        name="Alice",
        email="alice45678@test.com",
        phone="9999999999",
        years_of_experience=4,
        skills=["Python", "FastAPI"],
        linkedin_url="https://linkedin.com/in/alice"
    ),
    Candidate(
        name="Bob",
        email="bob@test.com",
        phone="8888888888",
        years_of_experience=6,
        skills=["SQL", "Azure"],
        linkedin_url="https://linkedin.com/in/bob"
    ),
]

db.add_all(candidates)
db.commit()

print("Database seeded successfully!")

db.close()