# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

# ----------------------------------------------
# Ideas: check digit root problem, congruence formula

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def addDigits_loop(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum(int(d) for d in str(num))
        return num
    
    
    def addDigits_noloop(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9;