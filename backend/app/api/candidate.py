
from fastapi import APIRouter, Depends
from app.exceptions.custom_exceptions import CandidateNotFoundException
from app.dependencies.candidate import get_candidate_service
from fastapi import HTTPException


from app.schemas.candidate import (
    CandidateCreate,
    CandidateResponse,
    CandidateUpdate 
)
from app.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"],
)




@router.post("/", response_model=CandidateResponse)
def create_candidate(
    candidate: CandidateCreate,
    service: CandidateService = Depends(get_candidate_service),
):

    return service.create_candidate(candidate)






@router.get("/", response_model=list[CandidateResponse])
def get_candidates(
    service: CandidateService = Depends(get_candidate_service),
):

    return service.get_candidates()






@router.get("/{candidate_id}", response_model=CandidateResponse)
def get_candidate(
    candidate_id: int,
    service: CandidateService = Depends(get_candidate_service),
):

    candidate = service.get_candidate(candidate_id)

    if candidate is None:
        raise CandidateNotFoundException(candidate_id)

    return candidate





@router.put(
    "/{candidate_id}",
    response_model=CandidateResponse,
)
def update_candidate(
    candidate_id: int,
    candidate: CandidateUpdate,
    service: CandidateService = Depends(get_candidate_service),
):

    updated_candidate = service.update_candidate(
        candidate_id,
        candidate,
    )

    if updated_candidate is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found",
        )

    return updated_candidate


@router.delete("/{candidate_id}")
def delete_candidate(
    candidate_id: int,
    service: CandidateService = Depends(get_candidate_service),
):

    deleted = service.delete_candidate(candidate_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found",
        )

    return {
        "message": "Candidate deleted successfully"
    }    