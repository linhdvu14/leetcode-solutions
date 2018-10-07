# Initially, there is a Robot at position (0, 0). Given a sequence 
# of its moves, judge if this robot makes a circle, which means it 
# moves back to the original place.

# The move sequence is represented by a string. And each move is 
# represent by a character. The valid robot moves are R (Right), 
# L (Left), U (Up) and D (down). The output should be true or false 
# representing whether the robot makes a circle.

# Example 1:
# Input: "UD"
# Output: true

# Example 2:
# Input: "LL"
# Output: false

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        bal_x = bal_y = 0
        for d in moves:
            if d == 'U':
                bal_y -= 1
            elif d == 'D':
                bal_y += 1
            elif d == 'L':
                bal_x -= 1
            elif d == 'R':
                bal_x += 1
        return bal_x == 0 and bal_y == 0

        # one liner:
        # return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
