# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Note:
#     Each element in the result should appear as many times as it shows in both arrays.
#     The result can be in any order.

# Follow up:
#     What if the given array is already sorted? How would you optimize your algorithm?
#     What if nums1's size is small compared to nums2's size? Which algorithm is better?
#     What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


# ----------------------------------------------
# Ideas:
# - hash table
# - follow-up 1: 2 pointers
# - follow-up 3:
#   +) if only nums2 cannot fit into memory, do intersect_0() and make memo of nums1
#   +) if neither nums1 or nums2 fit into the memory, sort both and read 1 element from each array each time

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def intersect_0(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # O(m + n) time, O(m) space
        memo = {}
        for num in nums1:
            memo[num] = memo.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if num in memo and memo[num] > 0:
                result.append(num)
                memo[num] -= 1
        return result


    def intersect_1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # O(min(m, n)) time excluding sorting, O(1) space
        nums1.sort()
        nums2.sort()
        result = []
        i1 = i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                result.append(nums1[i1])
                i1 += 1
                i2 += 1
        return result