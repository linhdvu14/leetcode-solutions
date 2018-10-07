# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:
# Input: 1->1->2
# Output: 1->2

# Example 2:
# Input: 1->1->2->3->3
# Output: 1->2->3

# ----------------------------------------------
# Ideas: 
# - fast+slow pointers, fast increments until fast != slow
# - just 1 pointer

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates_2pointers(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
            slow.next = fast
            slow = slow.next
        return head


    def deleteDuplicates_1pointer(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next  # skip over duplicates
            curr = curr.next  # now curr.val != curr.next val
        return head