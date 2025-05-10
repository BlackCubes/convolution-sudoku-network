"""
Main module for the convolution sudoku network API.
"""

import logging

from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import RequestResponseEndpoint
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.responses import StreamingResponse

from .api import api_router
from .logging import configure_logging
from .rate_limiter import limiter
from .ws import ws_router

log = logging.getLogger(__name__)

configure_logging()


async def not_found(req, exec):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": [{"msg": "Not found"}]},
    )


exception_handlers = {404: not_found}

app = FastAPI(exception_handlers=exception_handlers, openapi_url="")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(middleware_class=GZipMiddleware, minimum_size=1000)

api = FastAPI(
    title="Convolution Sudoku Network",
    description="Welcome to the Convolution Sudoku Network API documentation!",
    root_path="/api/v1",
)
api.add_middleware(middleware_class=GZipMiddleware, minimum_size=1000)


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> StreamingResponse:
        try:
            response = await call_next(request)
        except ValidationError as e:
            log.exception(e)
            response = JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={"detail": e.errors()},
            )
        except ValueError as e:
            log.exception(e)
            response = JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "detail": [
                        {
                            "msg": "Unknown",
                            "loc": ["Unknown"],
                            "type": "Unknown",
                        }
                    ]
                },
            )
        except Exception as e:
            log.exception(e)
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "detail": [
                        {
                            "msg": "Unknown",
                            "loc": ["Unknown"],
                            "type": "Unknown",
                        }
                    ]
                },
            )

        return response


api.add_middleware(ExceptionMiddleware)

api.include_router(router=api_router)

ws = FastAPI(root_path="/ws/v1")

ws.include_router(router=ws_router)

app.mount(path="/api/v1", app=api)

app.mount(path="/ws/v1", app=ws)
