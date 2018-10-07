# We have an array A of non-negative integers.

# For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the 
# bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].

# Return the number of possible results.  (Results that occur more than once are only counted 
# once in the final answer.) 

# Example 1:
# Input: [0]
# Output: 1
# Explanation: 
# There is only one possible result: 0.

# Example 2:
# Input: [1,1,2]
# Output: 3
# Explanation: 
# The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
# These yield the results 1, 1, 2, 1, 3, 3.
# There are 3 unique values, so the answer is 3.

# Example 3:
# Input: [1,2,4]
# Output: 6
# Explanation: 
# The possible results are 1, 2, 3, 4, 6, and 7.

# Note:
#     1 <= A.length <= 50000
#     0 <= A[i] <= 10^9


# ----------------------------------------------
# Ideas: keep B[k] = all possible results in subarray A[0..k]
# then B[k+1] = b | A[k+1] for b in B[k], plus A[k+1]

# Considerations: 
# - note len(B[k]) <= 32, because B[k] = B[0, k], B[1, k],... B([k, k]
#   is monotonically increasing, with at most 1 bit difference between elements

# Complexity: O(32n) time, space
# ----------------------------------------------

class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # curr = set holding B[k] = B[0, k], B[1, k],... B([k, k] at step k
        result, curr = set(), {0}
        for a in A:
            curr = {b | a for b in curr} | {a}
            result |= curr
        return len(result)
