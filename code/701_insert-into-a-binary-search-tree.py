# Given the root node of a binary search tree (BST) and a value to be inserted 
# into the tree, insert the value into the BST. Return the root node of the BST 
# after the insertion. It is guaranteed that the new value does not exist in the 
# original BST.

# Note that there may exist multiple valid ways for the insertion, as long as the 
# tree remains a BST after insertion. You can return any of them.

# For example, 
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5

# You can return this binary search tree:
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5

# This tree is also valid:
#          5
#        /   \
#       2     7
#      / \   
#     1   3
#          \
#           4

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
    def insertIntoBST_recursive(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST_recursive(root.right, val)
        else:
            root.left = self.insertIntoBST_recursive(root.left, val)
        return root
        
    
    def insertIntoBST_iterative(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        
        prev, curr = None, root
        while curr:
            prev = curr
            curr = curr.left if val < curr.val else curr.right
        if val > prev.val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root