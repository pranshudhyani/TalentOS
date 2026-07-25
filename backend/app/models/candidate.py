from sqlalchemy import Integer, String, JSON    
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Candidate(Base):

    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(100))

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
    )

    phone: Mapped[str] = mapped_column(String(15))

    years_of_experience: Mapped[int]

    skills: Mapped[list[str]] = mapped_column(JSON)

    linkedin_url: Mapped[str | None] = mapped_column(
    String(255),
    nullable=True,
    )

    github_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )