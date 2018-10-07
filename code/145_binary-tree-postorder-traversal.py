# Given a binary tree, return the postorder traversal of its nodes' values.

# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [3,2,1]

# Follow up: Recursive solution is trivial, could you do it iteratively?

# ----------------------------------------------
# Ideas:
# - method 1: do preorder right first to get (root, right, left)
#  then reverse to (left, right, root)
# - method 2: process each node twice, but only recorded in result
#  after its left and right branches have been processed

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
    def postorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorder(root, result):
            if root:
                postorder(root.left, result)
                postorder(root.right, result)
                result.append(root.val)

        result = []
        postorder(root, result)
        return result


    def postorderTraversal_iterative1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorderRightFirst(root):  # (root, right, left)
            result, stack = [], [root]
            while stack:
                node = stack.pop()
                if node:
                    result.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            return result

        result = preorderRightFirst(root)
        return result[::-1]  # (left, right, root)


    def postorderTraversal_iterative2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            node, seen = stack.pop()
            if seen:
                result.append(node.val)
            elif node:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return result



