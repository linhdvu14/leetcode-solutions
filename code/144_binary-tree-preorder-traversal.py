# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,2,3]

# Follow up: Recursive solution is trivial, could you do it iteratively?

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
    def preorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root, result):
            if root:
                result.append(root.val)
                preorder(root.left, result)
                preorder(root.right, result)

        result = []
        preorder(root, result)
        return result


    def preorderTraversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result


        
