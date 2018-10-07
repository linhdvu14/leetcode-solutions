# Given an integer, write a function to determine if it is a power of two.

# Example 1:
# Input: 1
# Output: true 
# Explanation: 20 = 1

# Example 2:
# Input: 16
# Output: true
# Explanation: 24 = 16

# Example 3:
# Input: 218
# Output: false

# ----------------------------------------------
# Ideas: power of two iff 1 bit set iff n&(n-1) == 0

# Considerations:
# - edge cases: n = 1, n < 0 

# Complexity: O(1) time, O(1) space
# ----------------------------------------------


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0