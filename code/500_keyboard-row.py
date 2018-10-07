# Given a List of words, return the words that can be typed using letters of 
# alphabet on only one row's of American keyboard like the image below.

# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

# Note:
#     You may use one character in the keyboard more than once.
#     You may assume the input string will only contain letters of alphabet.

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        char2row = {c:i for i, row in enumerate(['qwertyuiop', 'asdfghjkl', 'zxcvbnm']) for c in row}
        result = []
        for word in words:
            ref_char = word[0].lower()
            if all(char2row[c.lower()] == char2row[ref_char] for c in word):
                result.append(word)
        return result