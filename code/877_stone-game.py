# Alex and Lee play a game with piles of stones.  There are an even number of piles arranged 
# in a row, and each pile has a positive integer number of stones piles[i].

# The objective of the game is to end with the most stones.  The total number of stones is odd, 
# so there are no ties.

# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile 
# of stones from either the beginning or the end of the row.  This continues until there are no 
# more piles left, at which point the person with the most stones wins.

# Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

# Example 1:
# Input: [5,3,4,5]
# Output: true
# Explanation: 
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

# Note:
#     2 <= piles.length <= 500
#     piles.length is even.
#     1 <= piles[i] <= 500
#     sum(piles) is odd.

# ----------------------------------------------
# Ideas: Alex always wins bc can choose odd or even piles

# Considerations: 

# Complexity: O(1) time, O(1) space
# ----------------------------------------------

class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True


    # dp[e] = Alex score - Lee score if Alex plays first, given piles s..e at iteration s
    # O(n^2) time, O(n) space
    def stoneGame_1d(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        N = len(piles)
        dp = [0 for e in range(N)]
        for s in range(N - 1, -1, -1):
            dp[s] = piles[s]
            for e in range(s + 1, N, 1):
                dp[e] = max(piles[s] - dp[e], piles[e] - dp[e - 1])
        return dp[0] > 0
        
        
    # dp[s][e] = Alex score - Lee score if Alex plays first, given piles s..e
    # dp[s][e] = max(piles[s] - dp[s+1][e], piles[e] - dp[s][e-1])
    # O(n^2) time, O(n^2) space
    def stoneGame_2d(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        N = len(piles)
        dp = [[0 for e in range(N)] for s in range(N)]
        
        for s in range(N - 1, -1, -1):
            dp[s][s] = piles[s]
            for e in range(s + 1, N, 1):
                dp[s][e] = max(piles[s] - dp[s + 1][e], piles[e] - dp[s][e - 1])
        return dp[0][N - 1] > 0
        