# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k < 2:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre is not None:
            pre = self.reverse_next_k_nodes(pre, k)
        return dummy.next

    def reverse_next_k_nodes(self, head, k):
        n1 = head.next
        nk = head
        for _ in range(k):
            nk = nk.next
            if nk is None:
                return None
        nk_next = nk.next

        pre, cur = head, n1
        while cur != nk_next:
            cur.next, cur, pre = pre, cur.next, cur
        n1.next = nk_next
        head.next = pre
        return n1
