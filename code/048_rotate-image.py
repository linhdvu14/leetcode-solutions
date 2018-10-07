# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Note: You have to rotate the image in-place, which means you have to modify the 
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

# Example 2:
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

# ----------------------------------------------
# Ideas:
# - Clockwise: Transpose then reverse rows:
#   1 2 3         1 4 7         7 4 1
#   4 5 6   -->   2 5 8   -->   8 5 2
#   7 8 9         3 6 9         9 6 3

# - Counter-clockwise: Transpose then reverse cols:
#   1 2 3         1 4 7         3 6 9
#   4 5 6   -->   2 5 8   -->   2 5 8
#   7 8 9         3 6 9         1 4 7

# Considerations:
# - To transpose, only need to flip upper right half

# Complexity: O(n^2) time, O(1) space
# ----------------------------------------------

class Solution:
    def rotateClockwise(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n, 1):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(n):
            matrix[r].reverse()


    def rotateCounterClockwise(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for r in range(n):
            for c in range(r + 1, n, 1):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        matrix.reverse()


