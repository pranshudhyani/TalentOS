from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class AuthenticationMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        # Authentication middleware logic placeholder
        response = await call_next(request)
        return response
