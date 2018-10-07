# Given an n-ary tree, return the preorder traversal of its nodes' values.

# For example, given a 3-ary tree:
#      1
#    / | \
#   3  2  4
#  / \
# 5   6

# Return its preorder traversal as: [1,3,5,6,2,4].

# Note: Recursive solution is trivial, could you do it iteratively?

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.extend(node.children[::-1])
        return result
