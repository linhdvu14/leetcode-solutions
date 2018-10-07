# Given a linked list, remove the n-th node from the end 
# of list and return its head.

# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.

# Follow up:
# Could you do this in one pass?

# ----------------------------------------------
# Ideas: Have 2 runners n nodes apart

# Considerations: 
# - what if head needs removing?
# - edge cases: [1] and 1, [1, 2] and 2

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        fake_head.next = head

        slow, fast = fake_head, fake_head

        # move fast n nodes ahead
        for _ in range(n):
            fast = fast.next

        # move till fast is last node
        while fast.next != None:
            slow = slow.next
            fast = fast.next

        # slow.next is n-th node from last
        slow.next = slow.next.next

        return fake_head.next

