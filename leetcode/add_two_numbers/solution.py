# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r_val = l1.val + l2.val
        extra = r_val // 10
        r_val = r_val % 10
        root_node = prev_node = ListNode(r_val)

        while l1.next is not None or l2.next is not None or extra == 1:
            l1 = self.get_next(l1)
            l2 = self.get_next(l2)

            r_val = l1.val + l2.val + extra
            extra = r_val // 10
            r_val = r_val % 10

            prev_node.next = ListNode(r_val)
            prev_node = prev_node.next

        return root_node

    def get_next(self, node):
        return node.next if node.next is not None else ListNode(0)
