import typing

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from csn.sudoku.router import router as sudoku_router


class ErrorMessage(BaseModel):
    msg: str


class ErrorResponse(BaseModel):
    detail: typing.Optional[typing.List[ErrorMessage]]


api_router = APIRouter(
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)


@api_router.get("/healthcheck", include_in_schema=False)
def healthcheck():
    return {"status": "ok"}


api_router.include_router(
    router=sudoku_router,
    prefix="/sudokus",
    tags=["sudokus"],
)
