# You have a list of words and a pattern, and you want to know which 
# words in words matches the pattern.

# A word matches the pattern if there exists a permutation of letters p 
# so that after replacing every letter x in the pattern with p(x), we 
# get the desired word.

# (Recall that a permutation of letters is a bijection from letters to 
# letters: every letter maps to another letter, and no two letters map 
# to the same letter.)

# Return a list of the words in words that match the given pattern. 

# You may return the answer in any order.

# Example 1:
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
# since a and b map to the same letter.

# Note:
#     1 <= words.length <= 50
#     1 <= pattern.length = words[i].length <= 20


# ----------------------------------------------
# Ideas:
# - findAndReplacePattern_1(): keep 2 maps to record both
#	mapping directions
# - findAndReplacePattern_2(): if len(map1) == len(set(word1))
# 	then map1 (word1 -> word2) is one-to-one i.e. each char in word1
#	only maps to one char in word2

# Considerations: 

# Complexity: O(mn) time, O(mn) space where m = len(words), n = len(words[i])
# ----------------------------------------------

class Solution:
    def findAndReplacePattern_1(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """   
        def match(word1, word2):
            map1, map2 = {}, {}
            for c1, c2 in zip(word1, word2):  # pair of corresponding chars
                if c1 not in map1:
                    map1[c1] = c2
                if c2 not in map2:
                    map2[c2] = c1
                if map1[c1] != c2 or map2[c2] != c1:
                    return False
            return True
        return [word for word in words if match(word, pattern)]
            
        
    def findAndReplacePattern_2(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """ 
        def match(word1, word2):
            map1 = set(zip(word1, word2))
            map2 = set(zip(word2, word1))
            return len(map1) == len(map2) and len(map1) == len(set(word1)) and len(map2) == len(set(word2))
        return [word for word in words if match(word, pattern)]
