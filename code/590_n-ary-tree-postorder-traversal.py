# Given an n-ary tree, return the postorder traversal of its nodes' values.

# For example, given a 3-ary tree:
#      1
#    / | \
#   3  2  4
#  / \
# 5   6

# Return its postorder traversal as: [5,6,3,2,4,1].

# Note: Recursive solution is trivial, could you do it iteratively?

# ----------------------------------------------
# Ideas: do preorder right first to get (root, right, left)
#  then reverse to (left, right, root) 

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def reverse_preorder(root):  # root, right child, .... left child
            result = []
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    result.append(node.val)
                    stack.extend(node.children)
            return result

        return reverse_preorder(root)[::-1]  # left child, ... right child, root


