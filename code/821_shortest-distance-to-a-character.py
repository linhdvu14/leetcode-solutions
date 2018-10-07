# Given a string S and a character C, return an array of integers representing 
# the shortest distance from the character C in the string.

# Example 1:
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

# Note:
#     S string length is in [1, 10000].
#     C is a single character, and guaranteed to be in string S.
#     All letters in S and C are lowercase.


# ----------------------------------------------
# Ideas: 2 passes
# - forward pass: find min distance to C on left
# - backward pass: find min distance to C on right

# Considerations: 

# Complexity: O(n) time, O(n) space
# ----------------------------------------------

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        result = [n] * n
        last_C = -n  # so i - last_C >= n
        
        for i in range(n):
            if S[i] == C:
                last_C = i
            result[i] = min(result[i], abs(i - last_C))
        
        for i in range(n - 1, -1, -1):
            if S[i] == C:
                last_C = i
            result[i] = min(result[i], abs(i - last_C))
        
        return result