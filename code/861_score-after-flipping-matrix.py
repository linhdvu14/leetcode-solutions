# We have a two dimensional matrix A where each value is 0 or 1.

# A move consists of choosing any row or column, and toggling each value in that row or 
# column: changing all 0s to 1s, and all 1s to 0s.

# After making any number of moves, every row of this matrix is interpreted as a binary 
# number, and the score of the matrix is the sum of these numbers.

# Return the highest possible score.

# Example 1:
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

# Note:
#     1 <= A.length <= 20
#     1 <= A[0].length <= 20
#     A[i][j] is 0 or 1.


# ----------------------------------------------
# Ideas:
# - toggle each row s.t. first cell is 1
# - toggle each col s.t. over half rows is 1

# Considerations: 

# Complexity: O(rc) time, O(1) space
# ----------------------------------------------

class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        nr, nc = len(A), len(A[0])
        
        # First col: should toggle each row s.t. row[0] = 1
        result = (1 << nc - 1) * nr
        
        # Remaining cols: should toggle each col s.t. over half = 1
        for c in range(1, nc, 1):
            # col c = 1 if col c equals col 0 at beginning
            one_rows = sum([A[r][c] == A[r][0] for r in range(nr)]) 
            result += (1 << nc - c - 1) * max(one_rows, nr - one_rows)
        
        return result