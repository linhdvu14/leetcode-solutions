# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# ----------------------------------------------
# Ideas:
# - Follow up: use hash table

# Considerations: 

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for c in t:
            counts[c] = counts.get(c, 0) - 1
        return all(v == 0 for v in counts.values())
        