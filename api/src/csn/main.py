"""
Main module for the convolution sudoku network API.
"""

from typing import Union

from fastapi import FastAPI

from csn.sudoku.utils import SudokuAlgo

app = FastAPI()


@app.get("/")
def read_root():
    """
    Read root
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    Read item
    """
    return {"item_id": item_id, "q": q}


@app.get("/sudoku")
def sudoku():
    """
    Solve a sudoku puzzle
    """
    sudoku_algo = SudokuAlgo()

    sudoku_algo.solve(
        [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0],
        ]
    )

    return {
        "steps": sudoku_algo.solution["steps"],
        "length": len(sudoku_algo.solution["steps"]),
    }
