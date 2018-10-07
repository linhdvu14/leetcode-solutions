# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# ----------------------------------------------
# Ideas for iterative:
# - initialize array with k elements of 0
# - loop:
#   +) increment curr element
#   +) if curr > n, walk left (so next loop increments prev)
#   +) elif curr is at pos k, add to result
#   +) else walk right and copy curr to next (so array ascends)
# - stop when at idx -1
# --> Essentially 2 passes: left-to-right increments each position;
#   right-to-left goes back to increment previous positions:
#       [1, 2, 3], [1, 2, 4], ... [1, 3, 4], ... [2, 3, 4]

# Demonstration on n = 4, k = 3: (* = curr idx here)
# Initialize: [0, 0, 0]
# [*1*, 0, 0] --> [1, *1*, 0]
# [1, *2*, 0] --> [1, 2, *2*]
# [1, 2, *3*] --> add to result
# [1, 2, *4*] --> add to result
# [1, 2, *5*] --> [1, *2*, 5]
# [1, *3*, 5] --> [1, 3, *3*]
# [1, 3, *4*] --> add to result
# [1, 3, *5*] --> [1, *3*, 5]
# [1, *4*, 5] --> [1, 4, *4*]
# [1, 4, *5*] --> [1, *4*, 5]
# [1, *5*, 5] --> [*1*, 5, 5]
# [*2*, 5, 5] --> [2, *2*, 5]
# [2, *3*, 5] --> [2, 3, *3*]
# [2, 3, *4*] --> add to result
# [2, 3, *5*] --> [2, *3*, 5]
# [2, *4*, 5] --> [2, 4, *4*]
# [2, 4, *5*] --> [2, *4*, 5]
# [2, *5*, 5] --> [*2*, 5, 5]
# [*3*, 5, 5] --> [3, *4*, 5]
# [3, *5*, 5] --> [*3*, 5, 5]
# [*4*, 5, 5] --> [4, *4*, 5]
# [4, *5*, 5] --> [*4*, 5, 5]
# [*5*, 5, 5] --> idx = -1, out of loop

# Considerations: 

# Complexity: time, space

# ----------------------------------------------

class Solution:
    def combine_iterative(self, n, k):
         """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        arr = [0] * k
        idx = 0
        while idx >= 0:
            arr[idx] += 1
            if arr[idx] > n:
                idx -= 1
            elif idx == k - 1:
                result.append(arr[:])
            else:
                idx += 1
                arr[idx] = arr[idx - 1]
        return result


    def combine_backtrack(self, n, k):
         """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(n, k, curr, result, start):  # start = can only add numbers >= start
            if k == 0:
                result.append(curr[:])  # new copy of curr
            else:
                for num in range(start, n + 1, 1):
                    if k - len(curr) > n - num + 1:  # not enough nums left
                        break
                    backtrack(n, k - 1, curr + [num], result, num + 1)
                
        result = []
        backtrack(n, k, [], result, 1)  # start with 1 bc 1..n
        return result
