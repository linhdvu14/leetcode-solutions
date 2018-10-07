# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,3,2]

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
    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, result):
            if root:
                inorder(root.left, result)
                result.append(root.val)
                inorder(root.right, result)

        result = []
        inorder(root, result)
        return result


    def inorderTraversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left  # go all the way left
            if not stack:
                return result
            node = stack.pop()  # left outermost node
            root = node.right   # one step to the right
            result.append(node.val)


