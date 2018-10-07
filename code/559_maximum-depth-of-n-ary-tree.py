
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# For example, given a 3-ary tree:
#      1
#    / | \
#   3  2  4
#  / \
# 5   6
# We should return its max depth, which is 3.

# Note:
#     The depth of the tree is at most 1000.
#     The total number of nodes is at most 5000.

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(n) time, space
# ----------------------------------------------

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth_iterative(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        depth, level = 0, [root]
        while level:
            depth += 1
            level = [child for node in level for child in node.children]
        return depth


    def maxDepth_recursive(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth_recursive(child) for child in root.children)
