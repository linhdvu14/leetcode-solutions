# On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

# Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

# Now, we walk in a clockwise spiral shape to visit every position in this grid. 

# Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

# Eventually, we reach all R * C spaces of the grid.

# Return a list of coordinates representing the positions of the grid in the order they were visited.

# Example 1:
# Input: R = 1, C = 4, r0 = 0, c0 = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]

# Example 2:
# Input: R = 5, C = 6, r0 = 1, c0 = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

# Note:
#     1 <= R <= 100
#     1 <= C <= 100
#     0 <= r0 < R
#     0 <= c0 < C


# ----------------------------------------------
# Ideas:
# - direction: right, down, left, up, right, ...
# - step size: 1, 1, 2, 2, 3, 3
#   --> inc step when move left and right

# Considerations: 
# - R = C = 1

# Complexity: time, space
# ----------------------------------------------

# 1,4,0,0

class Solution:
    def spiralMatrixIII(self, R, C, r, c):
        """
        :type R: int
        :type C: int
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idir = step = 0
        result = [[r, c]]

        while len(result) < R*C:
            dr, dc = dirs[idir]
            if idir % 2 == 0:  # inc step size if move left/right
                step += 1
            for _ in range(step):
                r += dr
                c += dc
                if 0 <= r < R and 0 <= c < C:
                    result.append([r, c])
            idir = (idir + 1) % 4
        return result
