from fastapi import APIRouter

from .models import SudokuExample
from .service import example

router = APIRouter()


@router.get("/example", response_model=SudokuExample)
def get_example():
    return example()
