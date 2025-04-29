"""Module providing utilities for the sudoku package."""


class SudokuAlgo:
    """
    Contains the logic for solving a sudoku puzzle.
    """

    def __init__(self):
        self.solution = {"steps": []}

    def solve(self, board):
        """
        Solve the sudoku puzzle.
        """
        self.solution = {"steps": []}

        self.__solve_sudoku(board, 0, 0)

    def get_solution(self):
        """
        Returns the solution
        """
        return self.solution

    def __solve_sudoku(self, board, row, col):
        if row == 8 and col == 9:
            return True

        if col == 9:
            row += 1
            col = 0

        if board[row][col] != 0:
            return self.__solve_sudoku(board, row, col + 1)

        for num in range(1, 10):
            if self.__is_safe(board, row, col, num):
                board[row][col] = num

                if self.__solve_sudoku(board, row, col + 1):
                    self.solution["steps"].append((row, col, num))
                    return True

                board[row][col] = 0

        return False

    def __is_safe(self, board, row, col, num):
        """
        Check if it is safe to place a number in a cell.
        """

        for j in range(9):
            if board[row][j] == num:
                return False

        for i in range(9):
            if board[i][col] == num:
                return False

        start_row = row - row % 3
        start_col = col - col % 3

        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False

        return True
