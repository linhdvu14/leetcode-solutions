# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# Example:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(board, nrows, ncols, r, c, word, idx):
            if idx >= len(word):
                return True
            if r < 0 or r >= nrows or c < 0 or c >= ncols:
                return False
            if word[idx] != board[r][c]:
                return False
            
            char, board[r][c] = board[r][c], '.'  # mark current char
            result = backtrack(board, nrows, ncols, r - 1, c, word, idx + 1) or \
                backtrack(board, nrows, ncols, r + 1, c, word, idx + 1) or \
                backtrack(board, nrows, ncols, r, c - 1, word, idx + 1) or \
                backtrack(board, nrows, ncols, r, c + 1, word, idx + 1)
            board[r][c] = char
            return result
        
        if len(board) == 0 or len(board[0]) == 0:
            return False
        nrows, ncols = len(board), len(board[0])
        for r in range(nrows):
            for c in range(ncols):
                if backtrack(board, nrows, ncols, r, c, word, 0):
                    return True
        return False



