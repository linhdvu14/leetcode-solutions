# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
#     You receive a valid board, made of only battleships or empty slots.
#     Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
#     At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.

# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

# ----------------------------------------------
# Ideas: count only first cell of each ship, i.e.
#    cells with up and left neighbors != 'X'

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0 or len(board[0]) == 0:
            return 0
        nr, nc = len(board), len(board[0])

        result = 0
        for r in range(nr):
            for c in range(nc):
                if board[r][c] == 'X' and (r == 0 or board[r - 1][c] != 'X') and (c == 0 or board[r][c - 1] != 'X'):
                    result += 1
        return result
        