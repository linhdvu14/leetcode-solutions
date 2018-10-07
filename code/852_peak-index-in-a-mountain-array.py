# Let's call an array A a mountain if the following properties hold:
#     A.length >= 3
#     There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:
# Input: [0,1,0]
# Output: 1

# Example 2:
# Input: [0,2,1,0]
# Output: 1

# Note:
#     3 <= A.length <= 10000
#     0 <= A[i] <= 10^6
#     A is a mountain, as defined above.


# ----------------------------------------------
# Ideas:
# - linear time O(n): find first i where A[i] > A[i+1]
# - log time O(log n): find smallest i where A[i] > A[i+1]

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def peakIndexInMountainArray_linear(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                return i
    
    def peakIndexInMountainArray_log(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low, high = 0, len(A) - 1
        while low < high:
            mid = (low + high) // 2
            if A[mid] < A[mid + 1]:  # peak is after mid
                low = mid + 1
            else:  # peak is before or at mid
                high = mid
        return low