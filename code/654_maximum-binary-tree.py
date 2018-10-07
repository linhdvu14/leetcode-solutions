# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#     The root is the maximum number in the array.
#     The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
#     The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

# Construct the maximum tree by the given array and output the root node of this tree.

# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1

# Note:
#     The size of the given array will be in the range [1,1000].

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(n^2) time, O(n) space
# ----------------------------------------------


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def construct(nums, low, high):
            if low > high:
                return None
            if low == high:
                return TreeNode(nums[low])
            max_i = low
            for i in range(low, high + 1, 1):
                if nums[i] > nums[max_i]:
                    max_i = i
            root = TreeNode(nums[max_i])
            root.left = construct(nums, low, max_i - 1)
            root.right = construct(nums, max_i + 1, high)
            return root
        
        return construct(nums, 0, len(nums) - 1)

        