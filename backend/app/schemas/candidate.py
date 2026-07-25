
from pydantic import BaseModel, EmailStr, Field


class CandidateCreate(BaseModel): # used when the client send data 

    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=15,
    )

    years_of_experience: int = Field(
        ge=0,
        le=50,
    )

    skills: list[str] = Field(
        min_length=1,
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=15,
    )

    years_of_experience: int = Field(
        ge=0,
        le=50,
    )

    skills: list[str] = Field(
        min_length=1,
    )



class CandidateResponse(CandidateCreate):  # Used for sending responses back from server
    id: int


class CandidateUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    years_of_experience: int | None = None
    skills: list[str] | None = None