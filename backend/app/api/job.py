
from app.dependencies.job import get_job_service
from fastapi import APIRouter, Depends
# from app.exceptions.custom_exceptions import CandidateNotFoundException
from app.dependencies.candidate import get_candidate_service
from fastapi import HTTPException


from app.schemas.job import (
    JobCreate,
    JobResponse,
    JobUpdate 
)
from app.services.job_service import JobService

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)




@router.post("/", response_model=JobResponse)
def create_job(
    job: JobCreate,
    service: JobService = Depends(get_job_service),
):

    return service.create_job(job)






@router.get("/", response_model=list[JobResponse])
def get_jobs(
    service: JobService = Depends(get_job_service),
):

    return service.get_jobs()






@router.get("/{job_id}", response_model=JobResponse)
def get_job(
    job_id: int,
    service: JobService = Depends(get_job_service),
):

    job = service.get_job(job_id)

    if job is None:
        raise CandidateNotFoundException(job_id)

    return job





@router.put(
    "/{job_id}",
    response_model=JobResponse,
)
def update_job(
    job_id: int,
    job: JobUpdate,
    service: JobService = Depends(get_job_service),
):

    updated_job = service.update_job(
    job_id,
    job,
    )

    if updated_job is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found",
        )

    return updated_job


@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    service: JobService = Depends(get_job_service),
):

    deleted = service.delete_job(job_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found",
        )

    return {
        "message": "Candidate deleted successfully"
    }    