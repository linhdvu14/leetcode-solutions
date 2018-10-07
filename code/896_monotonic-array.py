# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is 
# monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

# Example 1:
# Input: [1,2,2,3]
# Output: true

# Example 2:
# Input: [6,5,4,4]
# Output: true

# Example 3:
# Input: [1,3,2]
# Output: false

# Example 4:
# Input: [1,2,4,5]
# Output: true

# Example 5:
# Input: [1,1,1]
# Output: true

# Note:
#     1 <= A.length <= 50000
#     -100000 <= A[i] <= 100000


# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        known_dir = False
        increase = True
        for i in range(1, len(A), 1):
            diff = A[i] - A[i - 1]
            if diff == 0:
                continue
            elif not known_dir:
                increase = diff > 0
                known_dir = True
            elif (increase and diff < 0) or (not increase and diff > 0):
                return False
        return True
