# Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.

# Example 1:
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5

# Example 2:
# Input: 1->1->1->2->3
# Output: 2->3

# ----------------------------------------------
# Ideas: maintain prev pointer, if cur.val == cur.next.val, 
# skip over

# Considerations: 
# - first node can be duplicate -> need fake head
# - edge cases: [1], [1, 1], [1, 1, 1]

# Complexity: O(n) time, O(1) space
# ----------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if head.next and head.val == head.next.val:  # has duplicate
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates_recursive(head.next)
        head.next = self.deleteDuplicates_recursive(head.next)
        return head


    def deleteDuplicates_iterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fake_head = ListNode(0)
        fake_head.next = head
        prev, curr = fake_head, head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next is curr:  # curr is not duplicate
                prev = curr
            else:  # curr is duplicate
                prev.next = curr.next
            curr = curr.next
        return fake_head.next

