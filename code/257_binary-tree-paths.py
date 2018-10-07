# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:
# Input:
#    1
#  /   \
# 2     3
#  \
#   5
# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def traverse(curr_path, results, node):
            curr_path += str(node.val)
            if not node.left and not node.right:
                results.append(curr_path)
            if node.left:
                traverse(curr_path + '->', results, node.left)
            if node.right:
                traverse(curr_path + '->', results, node.right)
        
        if not root:
            return []
        results = []
        traverse('', results, root)
        return results