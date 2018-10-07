# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]

# ----------------------------------------------
# Ideas: values in array = array idx + 1 ---> can
#   use array index to store: array[3] < 0 if 
#   has seen num = 4

# Considerations: 

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums:
            if nums[abs(num) - 1] < 0:  # seen before
                result.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1  # mark as seen
        return result