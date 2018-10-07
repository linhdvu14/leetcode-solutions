# Given a binary tree, find the leftmost value in the last row of the tree.

# Example 1:
# Input:

#     2
#    / \
#   1   3
# Output: 1

# Example 2:
# Input:
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
# Output: 7

# Note: You may assume the tree (i.e., the given root node) is not NULL. 

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val, level = 0, [root]
        while level:
            val = level[0].val
            level = [child for node in level for child in (node.left, node.right) if child]
        return val