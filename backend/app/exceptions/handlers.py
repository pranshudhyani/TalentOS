from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import CandidateNotFoundException


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(CandidateNotFoundException)
    async def candidate_not_found_handler(
        request: Request,
        exc: CandidateNotFoundException,
    ):

        return JSONResponse(
            status_code=404,
            content={
                "error": f"Candidate with id {exc.candidate_id} not found",
                "status": 404,
            },
        )