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

        prev = dummy
        cur = prev.next

        while cur is not None:
            # check if there is(are) next k-1 node(s)
            tmp = cur
            for _ in range(k-1):
                tmp = tmp.next
                if tmp is None: return dummy.next

            # there is(are) next k-1 node(s)
            prev.next = self.reverse_k_nodes(cur, k)
            prev = cur
            cur = cur.next

        return dummy.next

    def reverse_k_nodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode (new head)
        """
        pre = None
        cur = head
        for i in range(k):
            cur.next, cur, pre = pre, cur.next, cur
        head.next = cur

        return pre
