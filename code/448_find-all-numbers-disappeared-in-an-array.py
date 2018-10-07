# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some 
# elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the 
# returned list does not count as extra space.

# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [5,6]

# ----------------------------------------------
# Ideas: Using array values as indices, mark
# nums[num - 1] as seen when encounter num

# Considerations: 

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        result = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        return result   