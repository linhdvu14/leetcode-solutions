# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single 
# digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# ----------------------------------------------
# Ideas:

# Considerations: 

# Complexity: O(max(m, n)) time, O(max(m, n)) space
# ----------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        carry = 0
        p, p1, p2 = fake_head, l1, l2

        while p1 or p2 or carry:
            v1 = v2 = 0
            if p1:
                v1 = p1.val
                p1 = p1.next
            if p2:
                v2 = p2.val
                p2 = p2.next

            carry, v = divmod(v1 + v2 + carry, 10)
            p.next = ListNode(v)
            p = p.next

        return fake_head.next

