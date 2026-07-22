from pydantic import BaseModel, EmailStr

class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    years_of_experience: int
    skills: list[str]