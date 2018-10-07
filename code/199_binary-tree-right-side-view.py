# Given a binary tree, imagine yourself standing on the right side of it, return the 
# values of the nodes you can see ordered from top to bottom.

# Example:
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# ----------------------------------------------
# Ideas:
# - #1 level order traversal
# - #2 DFS: maintain dict of rightmost val at each level; 
#   visit right branch first
# - #3 DFS

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
    def rightSideView_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = {}
        max_depth = 0
        stack = [(root, 0)]
        while stack: 
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if depth not in result:
                result[depth] = node.val
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return [result[d] for d in range(max_depth + 1)]


    def rightSideView_level(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result, level = [], [root]
        while level:
            result.append(level[-1].val)
            level = [child for node in level for child in (node.left, node.right) if child]
        return result