# Given an array A of non-negative integers, return an array consisting of all the even
# elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Note:
#     1 <= A.length <= 5000
#     0 <= A[i] <= 5000

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lo, hi = 0, len(A) - 1
        while lo < hi:
            if A[lo] % 2 == 0:
                lo += 1
            else:
                A[lo], A[hi] = A[hi], A[lo]
                hi -= 1
        return A