# Implement function ToLowerCase() that has a string parameter 
# str, and returns the same string in lowercase.

# Example 1:
# Input: "Hello"
# Output: "hello"

# Example 2:
# Input: "here"
# Output: "here"

# Example 3:
# Input: "LOVELY"
# Output: "lovely"


# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(n) time, O(n) space
# ----------------------------------------------


class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join([chr(ord(c) - ord('A') + ord('a')) if ord('A') <= ord(c) <= ord('Z') else c for c in str])
        # oneliner:
        # return str.lower()