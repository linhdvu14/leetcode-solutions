# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 5
# Output: false

# Follow up: Could you solve it without loops/recursion?

# ----------------------------------------------
# Ideas: 
# - 1 bit set at odd pos
#  e.g. 1 = 1b, 4 = 100b, 16 = 10000b
# - 1 bit set, and num - 1 % 3 == 0

# Considerations:

# Complexity: 
# ----------------------------------------------


class Solution:
    def isPowerOfFour_loop(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
        	return False
        while num % 4 == 0:
        	num //= 4
        return num == 1


    def isPowerOfFour_noloop(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0
        