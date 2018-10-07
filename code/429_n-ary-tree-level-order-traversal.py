# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example, given a 3-ary tree:
#      1
#    / | \
#   3  2  4
#  / \
# 5   6

# We should return its level order traversal:
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]

# Note:
#     The depth of the tree is at most 1000.
#     The total number of nodes is at most 5000.


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
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result, level = [], [root]
        while level:
            result.append([node.val for node in level])
            level = [child for node in level for child in node.children]
        return result
        
