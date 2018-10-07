# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

# Note:
#     The range of node's value is in the range of 32-bit signed integer.

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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result, level = [], [root]
        while level:
            result.append(sum(node.val for node in level) / len(level))
            level = [child for node in level for child in (node.left, node.right) if child]
        return result