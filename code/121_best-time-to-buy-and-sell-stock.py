# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell 
# one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity:
# ----------------------------------------------

class Solution:
    def maxProfit_1pass(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # One pass; find highest peak following lowest valley
        # O(n) time, O(1) space
        buy_time = max_profit = 0
        for i in range(1, len(prices), 1):
            if prices[i] < prices[buy_time]:
                buy_time = i
            else:
                max_profit = max(max_profit, prices[i] - prices[buy_time])
        return max_profit
        
    
    def maxProfit_dp(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Max sum subarray DP
        # O(n) time, O(n) space
        diff = [prices[i] - prices[i - 1] for i in range(1, len(prices), 1)]
        max_so_far = max_ending_here = 0
        for i in range(len(diff)):
            max_ending_here = max(0, max_ending_here) + diff[i]
            max_so_far = max(max_so_far, max_ending_here)
        return max(max_so_far, 0)
        