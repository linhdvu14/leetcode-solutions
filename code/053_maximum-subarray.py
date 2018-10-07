# Given an integer array nums, find the contiguous subarray (containing at 
# least one number) which has the largest sum and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution using 
# the divide and conquer approach, which is more subtle.

# ----------------------------------------------
# Ideas: Kadane's

# Considerations: 

# Complexity: O(n) time, O(1) space
# ----------------------------------------------


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0

        max_ending_here = max_so_far = nums[0]
        for num in nums[1:]:
            max_ending_here = max(max_ending_here, 0) + num
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far