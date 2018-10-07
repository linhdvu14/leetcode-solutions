# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

# Note:
#     Each element in the result must be unique.
#     The result can be in any order.

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(m + n) time, O(m + n) space
# ----------------------------------------------

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set, nums2_set = set(nums1), set(nums2)
        return [num for num in nums1_set if num in nums2_set]
        