# Given an array nums and a value val, remove all instances of that 
# value in-place and return the new length.
# Do not allocate extra space for another array, you must do this 
# by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you 
# leave beyond the new length.

# Example 1:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements being 2.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, with the first five elements
# containing 0, 1, 3, 0, and 4.
# Note that the order of those five elements can be arbitrary.
# It doesn't matter what values are set beyond the returned length.

# ----------------------------------------------
# Ideas: 
# - maintain length of new array
# - swap element equal to val with end of new array 

# Considerations: 
# - edge cases: [3, 3, 3] and 3, [3, 1, 3, 3] and 3

# Complexity: O(n) time, O(1) space
# ----------------------------------------------


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            if nums[lo] == val:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                hi -= 1
            else:
                lo += 1  # incremented for each num != val

        return lo
