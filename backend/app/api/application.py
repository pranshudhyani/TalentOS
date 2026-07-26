from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.application import get_application_service
from app.schemas.application import (
    ApplicationCreate,
    ApplicationResponse,
    ApplicationUpdate,
)
from app.services.application_service import ApplicationService

router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


@router.post("/", response_model=ApplicationResponse)
def create_application(
    application: ApplicationCreate,
    service: ApplicationService = Depends(get_application_service),
):

    return service.create_application(application)


@router.get("/", response_model=list[ApplicationResponse])
def get_applications(
    service: ApplicationService = Depends(get_application_service),
):

    return service.get_applications()


@router.get("/{application_id}", response_model=ApplicationResponse)
def get_application(
    application_id: int,
    service: ApplicationService = Depends(get_application_service),
):

    application = service.get_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found",
        )

    return application


@router.put(
    "/{application_id}",
    response_model=ApplicationResponse,
)
def update_application(
    application_id: int,
    application: ApplicationUpdate,
    service: ApplicationService = Depends(get_application_service),
):

    updated_application = service.update_application(
        application_id,
        application,
    )

    if updated_application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found",
        )

    return updated_application


@router.delete("/{application_id}")
def delete_application(
    application_id: int,
    service: ApplicationService = Depends(get_application_service),
):

    deleted = service.delete_application(application_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Application not found",
        )

    return {
        "message": "Application deleted successfully"
    }
