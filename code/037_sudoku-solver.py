# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[str]
        :rtype: List[str]
        """
        self._solve(board, 0):


    def _solve(self, board, idx):
        """ Recursively solve board
        :type board: List[str]
        :type idx: int
        :rtype: boolean
        """
        if idx >= 81:
            return True
        r, c = divmod(idx, 9)

        # Cell solved, move on
        if board[r][c] != '.':
            return self._solve(board, idx + 1)

        # Cell unsolved, try 1-9
        for num in range(1, 10, 1):
            if self.isValid(board, r, c, str(num)):
                board[r][c] = str(num)
                if self._solve(board, idx + 1):
                    return True
                board[r][c] = '.'  # unmark if num doesn't work

        return False


    def isValid(self, board, r, c, num):
        """ Is putting num at board[r][c] valid?
        :type board: List[str]
        :type r: int
        :type c: int
        :type num: str
        :rtype: boolean
        """
        # same row, same col
        for i in range(9):
            if board[r][i] == num or board[i][c] == num:
                return False

        # same 3x3 grid
        grid_top_row = r - (r % 3)
        grid_top_col = c - (c % 3)
        for i in range(3):
            for j in range(3):
                if board[grid_top_row + i][grid_top_col + j] == num:
                    return False

        return True

