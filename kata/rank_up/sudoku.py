"""
There are several difficulty of sudoku games, we can estimate the difficulty of a sudoku game based on how many
cells are given of the 81 cells of the game.

Easy sudoku generally have over 32 givens
Medium sudoku have around 30–32 givens
Hard sudoku have around 28–30 givens
Very Hard sudoku have less than 28 givens
Note: The minimum of givens required to create a unique (with no multiple solutions) sudoku game is 17.

A hard sudoku game means that at start no cell will have a single candidates and thus require guessing
and trial and error. A very hard will have several layers of multiple candidates for any empty cell.

Task:
Write a function that solves sudoku puzzles of any difficulty. The function will take a sudoku grid
and it should return a 9x9 array with the proper answer for the puzzle.

Or it should raise an error in cases of: invalid grid (not 9x9, cell with values not in the range 1~9);
multiple solutions for the same puzzle or the puzzle is unsolvable
"""


class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)  # number of rows

    def solve(self):
        if self._solve_sudoku():
            return self.puzzle
        else:
            return None

    def _solve_sudoku(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.puzzle[row][col] == 0:
                    for num in range(1, self.size + 1):  # 1-9
                        if self._is_valid(row, col, num):
                            self.puzzle[row][col] = num

                            if self._solve_sudoku():
                                return True

                            self.puzzle[row][col] = 0

                    return False

        return True

    def _is_valid(self, row, col, num):
        return (
                self._is_row_valid(row, num)
                and self._is_col_valid(col, num)
                and self._is_box_valid(row - row % 3, col - col % 3, num)
        )

    def _is_row_valid(self, row, num):
        for col in range(self.size):
            if self.puzzle[row][col] == num:
                return False
        return True

    def _is_col_valid(self, col, num):
        for row in range(self.size):
            if self.puzzle[row][col] == num:
                return False
        return True

    def _is_box_valid(self, start_row, start_col, num):
        for row in range(3):
            for col in range(3):
                if self.puzzle[row + start_row][col + start_col] == num:
                    return False
        return True


def sudoku(puzzle):
    solver = SudokuSolver(puzzle)
    return solver.solve()


def test_sudoku():
    assert sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                   [6, 0, 0, 1, 9, 5, 0, 0, 0],
                   [0, 9, 8, 0, 0, 0, 0, 6, 0],
                   [8, 0, 0, 0, 6, 0, 0, 0, 3],
                   [4, 0, 0, 8, 0, 3, 0, 0, 1],
                   [7, 0, 0, 0, 2, 0, 0, 0, 6],
                   [0, 6, 0, 0, 0, 0, 2, 8, 0],
                   [0, 0, 0, 4, 1, 9, 0, 0, 5],
                   [0, 0, 0, 0, 8, 0, 0, 7, 9]]) == [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    assert sudoku([[6, 0, 0, 1, 0, 8, 2, 0, 3],
                   [0, 2, 0, 0, 4, 0, 0, 9, 0],
                   [8, 0, 3, 0, 0, 5, 4, 0, 0],
                   [5, 0, 4, 6, 0, 7, 0, 0, 9],
                   [0, 3, 0, 0, 0, 0, 0, 5, 0],
                   [7, 0, 0, 8, 0, 3, 1, 0, 2],
                   [0, 0, 1, 7, 0, 0, 9, 0, 6],
                   [0, 8, 0, 0, 3, 0, 0, 2, 0],
                   [3, 0, 2, 9, 0, 4, 0, 0, 5]]) == [[6, 4, 5, 1, 9, 8, 2, 7, 3],
                                                     [1, 2, 7, 3, 4, 6, 5, 9, 8],
                                                     [8, 9, 3, 2, 7, 5, 4, 6, 1],
                                                     [5, 1, 4, 6, 2, 7, 3, 8, 9],
                                                     [2, 3, 8, 4, 1, 9, 6, 5, 7],
                                                     [7, 6, 9, 8, 5, 3, 1, 4, 2],
                                                     [4, 5, 1, 7, 8, 2, 9, 3, 6],
                                                     [9, 8, 6, 5, 3, 1, 7, 2, 4],
                                                     [3, 7, 2, 9, 6, 4, 8, 1, 5]]

    assert sudoku([[0, 1, 9, 0, 6, 0, 5, 4, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [8, 2, 0, 9, 7, 4, 0, 3, 6],
                   [0, 0, 1, 5, 0, 3, 8, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 2, 7, 0, 1, 6, 0, 0],
                   [7, 5, 0, 1, 3, 8, 0, 9, 2],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 8, 3, 0, 4, 0, 7, 1, 0]]) == [[3, 1, 9, 8, 6, 2, 5, 4, 7],
                                                     [4, 6, 7, 3, 1, 5, 2, 8, 9],
                                                     [8, 2, 5, 9, 7, 4, 1, 3, 6],
                                                     [6, 7, 1, 5, 9, 3, 8, 2, 4],
                                                     [5, 3, 8, 4, 2, 6, 9, 7, 1],
                                                     [9, 4, 2, 7, 8, 1, 6, 5, 3],
                                                     [7, 5, 6, 1, 3, 8, 4, 9, 2],
                                                     [1, 9, 4, 2, 5, 7, 3, 6, 8],
                                                     [2, 8, 3, 6, 4, 9, 7, 1, 5]]

    assert sudoku([[0, 0, 8, 0, 3, 0, 5, 4, 0],
                   [3, 0, 0, 4, 0, 7, 9, 0, 0],
                   [4, 1, 0, 0, 0, 8, 0, 0, 2],
                   [0, 4, 3, 5, 0, 2, 0, 6, 0],
                   [5, 0, 0, 0, 0, 0, 0, 0, 8],
                   [0, 6, 0, 3, 0, 9, 4, 1, 0],
                   [1, 0, 0, 8, 0, 0, 0, 2, 7],
                   [0, 0, 5, 6, 0, 3, 0, 0, 4],
                   [0, 2, 9, 0, 7, 0, 8, 0, 0]]) == [[9, 7, 8, 2, 3, 1, 5, 4, 6],
                                                     [3, 5, 2, 4, 6, 7, 9, 8, 1],
                                                     [4, 1, 6, 9, 5, 8, 3, 7, 2],
                                                     [8, 4, 3, 5, 1, 2, 7, 6, 9],
                                                     [5, 9, 1, 7, 4, 6, 2, 3, 8],
                                                     [2, 6, 7, 3, 8, 9, 4, 1, 5],
                                                     [1, 3, 4, 8, 9, 5, 6, 2, 7],
                                                     [7, 8, 5, 6, 2, 3, 1, 9, 4],
                                                     [6, 2, 9, 1, 7, 4, 8, 5, 3]]
