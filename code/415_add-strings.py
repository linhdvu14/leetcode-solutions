Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(m + n) time, O(1) space
# ----------------------------------------------

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i1, i2, carry = len(num1) - 1, len(num2) - 1, 0
        result = ''
        while i1 >= 0 or i2 >= 0 or carry:
            val = carry
            if i1 >= 0:
                val += int(num1[i1])
            if i2 >= 0:
                val += int(num2[i2])
            carry, val = divmod(val, 10)
            result += str(val)
            i1 -= 1
            i2 -= 1
        return result[::-1]