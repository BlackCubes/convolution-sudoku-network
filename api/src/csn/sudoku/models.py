from datetime import datetime

from pydantic import BaseModel


class DateTimeBase:
    created_at: datetime
    updated_at: datetime


class SudokuExample(BaseModel, DateTimeBase):
    steps: list[list[int]]
    length: int
