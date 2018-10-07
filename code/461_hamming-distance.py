# The Hamming distance between two integers is the number of 
# positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        |   |

# The above arrows point to positions where the corresponding bits are different.

# ----------------------------------------------
# Ideas: count number of bits set in x XOR y

# Considerations: 

# Complexity: time, space
# ----------------------------------------------


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        num_bits_set = 0
        while xor != 0:
            xor = xor & (xor - 1)
            num_bits_set += 1
        return num_bits_set
        