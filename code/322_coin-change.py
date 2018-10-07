# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# Note: You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# ----------------------------------------------
# Ideas:
# - dp[i] = min num coins to make amount i
# - dp[i] = min(dp[i - coin] + 1) for coin in coins

# Considerations:

# Complexity: O(ac) time, O(a) space
# ----------------------------------------------

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount
        for a in range(1, amount + 1, 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[-1] if dp[-1] < float('inf') else -1
