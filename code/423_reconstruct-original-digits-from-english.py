# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

# Note:
#     Input contains only lowercase English letters.
#     Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
#     Input length is less than 50,000.

# Example 1:
# Input: "owoztneoer"
# Output: "012"

# Example 2:
# Input: "fviefuro"
# Output: "45"

# ----------------------------------------------
# Ideas:
# - count z for zero, w for two, u for four, x for six, g for eight
# - count o for one, t for three, f for five, s for seven, i for nine

# Considerations: 

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        id_chars = {'z':0, 'o':1, 'w':2, 't':3, 'u':4, 'f':5, 'x':6, 's':7, 'g':8, 'i':9}
        counts = [0] * 10
        for c in s:
            if c in id_chars:
                pos = id_chars[c]
                counts[pos] += 1
        counts[1] -= counts[0] + counts[2] + counts[4]
        counts[3] -= counts[2] + counts[8]
        counts[5] -= counts[4]
        counts[7] -= counts[6]
        counts[9] -= counts[6] + counts[8] + counts[5] 
        return ''.join(str(i) * counts[i] for i in range(10))