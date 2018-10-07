# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth, level = 0, [root]
        while level:
            depth += 1
            level = [child for node in level for child in (node.left, node.right) if child]
        return depth