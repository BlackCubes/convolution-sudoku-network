from datetime import datetime

from pydantic import BaseModel


class DateTimeExampleBase:
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class SudokuExample(BaseModel, DateTimeExampleBase):
    steps: list[list[int]]
    length: int
