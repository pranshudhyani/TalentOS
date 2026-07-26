from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy database models.
    """
    pass

# Import all models to ensure they are registered on the Base metadata
from app.models.candidate import Candidate  # noqa: F401
from app.models.job import Job  # noqa: F401
from app.models.application import Application  # noqa: F401

