# Given a sorted array nums, remove the duplicates in-place such that 
# each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by 
# modifying the input array in-place with O(1) extra memory.

# Example 1:
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements 
# of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5, with the first five elements 
# of nums being modified to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.

# ----------------------------------------------
# Ideas:
# - maintain slow, fast pointers
# - increment fast if nums[fast] == nums[slow], else 
# replace nums[slow] with nums[fast]

# Considerations: 
# - edge cases: [], [1], [1, 1], [1, 1, 2]

# Complexity: O(n) time, O(1) space
# ----------------------------------------------


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        slow = 0
        for fast in range(1, len(nums), 1):
            if nums[slow] != nums[fast]:  # new val
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
