# Given a positive integer, check whether it has alternating bits: namely, 
# if two adjacent bits will always have different values.

# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101

# Example 2:
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.

# Example 3:
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.

# Example 4:
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.

# ----------------------------------------------
# Ideas:
# - #1: check last bit
# - #2: n XOR (n >> 2) has only 1 leading 1 bit
# - #3: n XOR (n >> 1) has all 1s

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def hasAlternatingBits_1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = n & 1  # is rightmost bit set
        while n > 0:
            n = n >> 1
            curr = n & 1
            if curr == last:
                return False
            last = curr
        return True
    
    # n XOR (n >> 2) has only 1 leading 1 bit?
    def hasAlternatingBits_2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not (n ^ (n >> 2)) & ((n ^ (n >> 2)) - 1)
    
    # n XOR (n >> 1) has all 1s?
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not ((n ^ (n >> 1)) + 1) & (n ^ (n >> 1))