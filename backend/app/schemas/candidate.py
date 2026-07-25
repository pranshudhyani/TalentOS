
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import List


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

    linkedin_url: HttpUrl | None = None

    github_url: str | None = None



class CandidateResponse(CandidateCreate):  # Used for sending responses back from server
    id: int



class CandidateUpdate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    years_of_experience: int
    skills: List[str]
    linkedin_url: HttpUrl | None = None
    github_url: str | None = None