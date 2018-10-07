# A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can 
# receive one of three possible types of commands:
#     -2: turn left 90 degrees
#     -1: turn right 90 degrees
#     1 <= x <= 9: move forward x units

# Some of the grid squares are obstacles. 

# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

# If the robot would try to move onto them, the robot stays on the previous 
# grid square instead (but still continues following the rest of the route.)

# Return the square of the maximum Euclidean distance that the robot will be 
# from the origin. 

# Example 1:
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: robot will go to (3, 4)

# Example 2:
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)

# Note:
#     0 <= commands.length <= 10000
#     0 <= obstacles.length <= 10000
#     -30000 <= obstacle[i][0] <= 30000
#     -30000 <= obstacle[i][1] <= 30000
#     The answer is guaranteed to be less than 2 ^ 31.

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(m) time, O(n) space where m = len(commands), n = len(obstacles)
# ----------------------------------------------

class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacles = set(map(tuple, obstacles))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # turn left = step left on dir array
        result = x = y = i = 0  # i = dirs index; x, y = coords
            
        for c in commands:
            if c == -2:
                i = (i - 1) % 4
            elif c == -1:
                i = (i + 1) % 4
            else:
                for _ in range(c):
                    dx, dy = dirs[i]
                    if (x + dx, y + dy) not in obstacles:
                        x += dx
                        y += dy
                        result = max(result, x * x + y * y)       
        return result