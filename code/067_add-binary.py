# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(m + n) time, O(1) space
# ----------------------------------------------

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        ia, ib, carry = len(a) - 1, len(b) - 1, 0
        while ia >= 0 or ib >= 0 or carry > 0:
            val = carry
            if ia >= 0:
                val += int(a[ia])
            if ib >= 0:
                val += int(b[ib])
            carry, val = divmod(val, 2)
            result += str(val)
            ia -= 1
            ib -= 1
        return result[::-1]
            