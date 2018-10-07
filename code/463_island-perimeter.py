# You are given a map in form of a two-dimensional integer grid where 1 represents 
# land and 0 represents water. Grid cells are connected horizontally/vertically 
# (not diagonally). The grid is completely surrounded by water, and there is exactly 
# one island (i.e., one or more connected land cells). The island doesn't have "lakes" 
# (water inside that isn't connected to the water around the island). One cell is a 
# square with side length 1. The grid is rectangular, width and height don't exceed 
# 100. Determine the perimeter of the island.

# Example:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below

# ----------------------------------------------
# Ideas: count 4 for each 1 cell + remove internal edges

# Considerations: 

# Complexity: O(mn) time, O(1) space
# ----------------------------------------------

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        nr, nc = len(grid), len(grid[0])
        result = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]:
                    result += 4
                    if r - 1 >= 0 and grid[r - 1][c]:
                        result -= 2  # internal horizontal edge
                    if c - 1 >= 0 and grid[r][c - 1]:
                        result -= 2  # internal vertical edge
        return result
