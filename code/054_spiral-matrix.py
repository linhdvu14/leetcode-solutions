# Given a matrix of m x n elements (m rows, n columns), return all 
# elements of the matrix in spiral order.

# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# ----------------------------------------------
# Ideas: E.g. for a 5x3 matrix, start at cell [-1, 0] and
# - walk right 5 times
# - walk down 2 times
# - walk left 4 times
# - walk up 1 time
# - walk right 3 times
# - walk down 0 time --> quit

# --> Note that:
# - walk direction follows order: right, down, left, up
# - in total, walk (5, 4, 3) steps horizontally, and (2, 1, 0)
#   steps vertically

# Considerations:

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        nrows, ncols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        i = 0  # direction index: i % 2 == 0 means vertical
        rem_steps = [ncols, nrows - 1]  # num remaining steps
        r, c = 0, -1  # start position

        result = []
        while rem_steps[i % 2] > 0:
            # walk entire remaining row/col
            num_steps = rem_steps[i % 2]
            for _ in range(num_steps):
                r += directions[i][0]
                c += directions[i][1]
                result.append(matrix[r][c])

            # direction for next walk
            rem_steps[i % 2] -= 1
            i = (i + 1) % 4

        return result
