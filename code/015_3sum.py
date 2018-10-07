# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# ----------------------------------------------
# Ideas:
# - Sort array
# - Try all possible a
# - For (b, c), shrink the sliding window (a+1, len(nums)-1)

# Considerations: 
# - a, b, c might not be distinct
# - Edge cases: [0, 0, 0], [-1, -1, 0, 1]

# Complexity: O(n^2)
# ----------------------------------------------


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        nums.sort()
        ia = 0
        while ia < len(nums) - 2: 
            ib, ic = ia + 1, len(nums) - 1
            while ib < ic:                
                s = nums[ia] + nums[ib] + nums[ic] 
                if s < 0:
                    ib += 1
                elif s > 0:
                    ic -= 1
                else:
                    a, b, c = nums[ia], nums[ib], nums[ic]
                    while nums[ib] == b and ib < ic:  # skip duplicate of b
                        ib += 1
                    while nums[ic] == c and ib < ic:
                        ic -= 1
                    result.append([a, b, c])
                
            a = nums[ia]
            while ia < len(nums) - 2 and nums[ia] == a:
                ia += 1
                
        return result