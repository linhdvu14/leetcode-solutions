# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes 
# of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# ----------------------------------------------
# Ideas:

# Considerations: 
# - can stop merging as soon as one list runs out

# Complexity: O(min(m, n)) time, space
# ----------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists_iterative(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        p, p1, p2 = fake_head, l1, l2

        while p1 and p2:
            if p1.val < p2.val:
                p.next = ListNode(p1.val)
                p1 = p1.next
            else:
                p.next = ListNode(p2.val)
                p2 = p2.next
            p = p.next

        p.next = p1 or p2
        return fake_head.next


    def mergeTwoLists_recursive(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists_recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_recursive(l1, l2.next)
            return l2



