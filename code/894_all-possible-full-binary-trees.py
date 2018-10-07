# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

# Return a list of all possible full binary trees with N nodes.  Each element of the 
# answer is the root node of one possible tree.

# Each node of each tree in the answer must have node.val = 0.

# You may return the final list of trees in any order.

# Example 1:
# Input: 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

# Note:
#     1 <= N <= 20

# ----------------------------------------------
# Ideas: Recurrence FPT(N) = all trees with left = FPT(x)
#   and right = FPT(N - 1 - x) where x = 0..N - 1

# Considerations: 
# - N is odd

# Complexity: time, space
# ----------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    memo = {0: [], 1: [TreeNode(0)]}
    
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N not in Solution.memo:
            result = []
            for x in range(N - 1):  # note x = 0: still get 1 root node
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)
            Solution.memo[N] = result
        return Solution.memo[N] 