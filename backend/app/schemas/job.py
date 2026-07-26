from pydantic import BaseModel, Field


class JobCreate(BaseModel):

    title: str = Field(
        min_length=2,
        max_length=100,
    )

    company: str = Field(
        min_length=2,
        max_length=100,
    )

    location: str = Field(
        min_length=2,
        max_length=100,
    )

    salary: int = Field(
        ge=0,
    )

    description: str = Field(
        min_length=5,
        max_length=500,
    )


class JobResponse(JobCreate):
    id: int


class JobUpdate(BaseModel):

    title: str | None = None
    company: str | None = None
    location: str | None = None
    salary: int | None = None
    description: str | None = None