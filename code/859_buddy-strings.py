# Given two strings A and B of lowercase letters, return true if and only if we can swap 
# two letters in A so that the result equals B. 

# Example 1:
# Input: A = "ab", B = "ba"
# Output: true

# Example 2:
# Input: A = "ab", B = "ab"
# Output: false

# Example 3:
# Input: A = "aa", B = "aa"
# Output: true

# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true

# Example 5:
# Input: A = "", B = "aa"
# Output: false

# Note:
#     0 <= A.length <= 20000
#     0 <= B.length <= 20000
#     A and B consist only of lowercase letters.


# ----------------------------------------------
# Ideas:

# Considerations: 
# - 2 letters must be swapped, so (ab, ba) and (aa, aa) OK
#   but (ab, ab) not OK
# - (abcd, badc) not OK: note a-b == c-d
# - if A == B, can swap if A has duplicate letters

# Complexity: O(n) time, O(n) space (can reduce to O(1))
# ----------------------------------------------

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return len(A) > len(set(A))
        maps = list(set(a + b for a, b in zip(A, B) if a != b))
        return len(maps) == 2 and maps[0] == maps[1][::-1]
        