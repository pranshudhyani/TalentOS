from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.db.base import Base


class Application(Base):

    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    candidate_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )

    job_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("jobs.id"),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Applied",
        nullable=False,
    )

    candidate = relationship(
    "Candidate",
    back_populates="applications",
)

    job = relationship(
        "Job",
        back_populates="applications",
)
