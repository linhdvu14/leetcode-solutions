# Determine whether an integer is a palindrome. An integer is a palindrome 
# when it reads the same backward as forward.

# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it 
# becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Follow up:
# Coud you solve it without converting the integer to a string?

# ----------------------------------------------
# Ideas:
# - check if number == its reverse

# Considerations: 
# - not palindrome if: < 0, ends with 0
# - edge cases: 1, 1100, 010, -11

# Complexity: time, space
# ----------------------------------------------


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_rev, x_tmp = 0, x
        while x_tmp > 0:
            x_rev = x_rev * 10 + x_tmp % 10
            x_tmp = x_tmp // 10
        return x_rev == x


