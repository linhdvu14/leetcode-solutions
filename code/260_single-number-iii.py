# Given an array of numbers nums, in which exactly two elements appear only once and all 
# the other elements appear exactly twice. Find the two elements that appear only once.

# Example:
# Input:  [1,2,1,3,2,5]
# Output: [3,5]

# Note:
#     The order of the result is not important. So in the above example, [5, 3] is also correct.
#     Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

# ----------------------------------------------
# Ideas:
# - single1 and singl2 must differ in at least 1 bit
#   --> maintain 2 xor for numbers with that bit set
# - n & (n-1) clears rightmost set bit
#   --> n ^ (n & (n-1)) gives rightmost set bit

# Considerations: 

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pass 1: find differing bit
        xor = 0
        for num in nums:
            xor ^= num
        diff = xor ^ (xor & (xor - 1))  # rightmost bit where single1 != single2

        # pass 2
        xor1 = xor2 = 0
        for num in nums:
            if num & diff:
                xor1 ^= num
            else:
                xor2 ^= num
        return xor1, xor2
        