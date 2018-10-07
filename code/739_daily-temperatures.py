# Given a list of daily temperatures, produce a list that, for each day in 
# the input, tells you how many days you would have to wait until a warmer 
# temperature. If there is no future day for which this is possible, put 0 
# instead.

# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], 
# your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each 
# temperature will be an integer in the range [30, 100]. 

# ----------------------------------------------
# Ideas: stack holds decreasing temp sequence; push idx only

# Considerations: 

# Complexity: O(n) time, O(n) space
# ----------------------------------------------

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                last_i = stack.pop()
                result[last_i] = i - last_i
            stack.append(i)
        return result