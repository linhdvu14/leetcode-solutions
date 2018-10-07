# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# Output: [1, 3, 9]

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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result, level = [], [root]
        while level:
            result.append(max(node.val for node in level))
            level = [child for node in level for child in (node.left, node.right) if child]
        return result