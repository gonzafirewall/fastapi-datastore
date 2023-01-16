from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from models import client


class GoogleCloudContextMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        with client.context():
            return await call_next(request)