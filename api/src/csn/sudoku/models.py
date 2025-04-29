from datetime import datetime


class Base:
    created_at: datetime
    updated_at: datetime


class SudokuExample(Base):
    steps: list[list[int]]
    length: int
