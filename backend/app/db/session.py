from collections.abc import Generator
from sqlalchemy.orm import sessionmaker, Session
from app.db.database import engine

# Create a sessionmaker instance for database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def get_db() -> Generator[Session, None, None]:
    """
    Dependency generator that yields a database session and ensures
    it is closed after the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
