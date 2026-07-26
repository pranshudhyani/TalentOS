from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class Job(Base):

    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(100)
    )

    company: Mapped[str] = mapped_column(
        String(100)
    )

    location: Mapped[str] = mapped_column(
        String(100)
    )

    salary: Mapped[int]

    description: Mapped[str] = mapped_column(
        String(500)
    )

    applications = relationship(
    "Application",
    back_populates="job",
    cascade="all, delete-orphan",
)