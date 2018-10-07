# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
# You have the following 3 operations permitted on a word:
#     Insert a character
#     Delete a character
#     Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------


class Solution:
    def minDistance_1d(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Idea: maintain only previous row and current row
        # prev[j] = min edit distance between word1[:i-1] and word2[:j]
        # curr[j] = min edit distance between word1[:i] and word2[:j]
        # After l1 iterations, curr[-1] = min edit distance between word1 and word2
        # Complexity: O(mn) time, O(m) space
        l1, l2 = len(word1), len(word2)
        prev = [j for j in range(l2 + 1)]
        for i in range(1, l1 + 1, 1):
            curr = [i] + [0] * l2
            for j in range(1, l2 + 1, 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = min(prev[j - 1], prev[j], curr[j - 1]) + 1
            prev = curr[:]

        return prev[-1]
        
    
    def minDistance_2d(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j] = min edit distance between word1[:i] and word2[:j] (first i/j chars)
        # dp[i][j] = dp[i-1][j-1] if word1[i] == word2[j]; otherwise
        # dp[i][j] = 1 + min(dp[i-1][j-1],    # replace
        #                    dp[i-1][j],      # delete a char in word1/insert a char in word2
        #                    dp[i][j-1])      # delete a char in word2/insert a char in word1
        # Initialization: dp[0][0] = 0, dp[0][j] = j, dp[i][0] = i
        # Complexity: O(mn) time, O(mn) space

        l1, l2 = len(word1), len(word2)
        dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]

        for i in range(1, l1 + 1, 1):
            for j in range(1, l2 + 1, 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]
