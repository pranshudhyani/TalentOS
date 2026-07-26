from pydantic import BaseModel, Field


class ApplicationCreate(BaseModel):

    candidate_id: int

    job_id: int

    status: str = Field(
        default="Applied",
        min_length=2,
        max_length=50,
    )


class ApplicationResponse(ApplicationCreate):
    id: int


class ApplicationUpdate(BaseModel):

    candidate_id: int | None = None
    job_id: int | None = None
    status: str | None = Field(
        default=None,
        min_length=2,
        max_length=50,
    )
