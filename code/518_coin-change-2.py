# You are given coins of different denominations and a total amount of money. 
# Write a function to compute the number of combinations that make up that amount. 
# You may assume that you have infinite number of each kind of coin.
# Note: You can assume that
#     0 <= amount <= 5000
#     1 <= coin <= 5000
#     the number of coins is less than 500
#     the answer is guaranteed to fit into signed 32-bit integer

# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Example 3:
# Input: amount = 10, coins = [10] 
# Output: 1

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def change_1d(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp[c][a] = num ways to make changes for amount a, using all coins
        # Initialization: dp[0] = 1
        # Complexity: O(ac) time, O(a) space
        dp = [0 for a in range(amount + 1)]
        dp[0] = 1        
        
        for c in range(1, len(coins) + 1, 1):
            for a in range(1, amount + 1, 1):
                if a - coins[c - 1] >= 0:
                    dp[a] += dp[a - coins[c - 1]]
        return dp[-1]


    def change_2d(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp[c][a] = num ways to make changes for amount a, using only first c coins
        # dp[c][a] = dp[c - 1][a] + dp[c - 1][a - coins[c]]: either use highest denom or not
        # Initialization: dp[*][0] = 1
        # Complexity: O(ac) time, O(ac) space
        dp = [[0 for a in range(amount + 1)] for c in range(len(coins) + 1)]
        dp[0][0] = 1

        for c in range(1, len(coins) + 1, 1):
            dp[c][0] = 1
            for a in range(1, amount + 1, 1):
                if a - coins[c - 1] >= 0:
                    dp[c][a] = dp[c - 1][a] + dp[c][a - coins[c - 1]]
                else:
                    dp[c][a] = dp[c - 1][a]
        
        return dp[-1][-1]
        