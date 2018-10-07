# You are playing the following Nim Game with your friend: There 
# is a heap of stones on the table, each time one of you take turns 
# to remove 1 to 3 stones. The one who removes the last stone will 
# be the winner. You will take the first turn to remove the stones.

# Both of you are very clever and have optimal strategies for the 
# game. Write a function to determine whether you can win the game 
# given the number of stones in the heap.

# Example:
# Input: 4
# Output: false 
# Explanation: If there are 4 stones in the heap, then you will never win the game;
#              No matter 1, 2, or 3 stones you remove, the last stone will always be 
#              removed by your friend.


# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Solution:
    def canWinNim_const(self, n):
        """
        :type n: int
        :rtype: bool
        """    
        return not (n % 4 == 0)
    
    def canWinNim_lin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n <= 3:
            return True
        prev3, prev2, prev1, curr = False, True, True, False
        for _ in range(3, n + 1, 1):
            curr = not prev1 or not prev2 or not prev3
            prev3, prev2, prev1 = prev2, prev1, curr
        return curr
