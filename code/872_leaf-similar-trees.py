# Consider all the leaves of a binary tree.  From left to right order, the 
# values of those leaves form a leaf value sequence.

#      3
#     / \
#    5   1
#  / |   | \
# 6  2   9  8
#   / \
#  7   4

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Note:
#     Both of the given trees will have between 1 and 100 nodes.

# ----------------------------------------------
# Ideas: pre-order traversal to get leaves

# Considerations: 

# Complexity: O(n) time, O(n) space
# ----------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaves(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return get_leaves(root.left) + get_leaves(root.right)
        
        return get_leaves(root1) == get_leaves(root2)