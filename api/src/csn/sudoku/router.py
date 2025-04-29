from fastapi import APIRouter

from csn.sudoku.models import SudokuExample
from csn.sudoku.service import example

router = APIRouter()


@router.get("/example", response_model=SudokuExample)
def get_example():
    return example()
