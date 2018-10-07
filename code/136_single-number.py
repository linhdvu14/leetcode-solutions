# Given a non-empty array of integers, every element appears 
# twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could 
# you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

# ----------------------------------------------
# Ideas: All bits are toggled an even number of times,
# except bits belonging to the single number

# Considerations: 

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        toggle = 0
        for num in nums:
            toggle ^= num
        return toggle