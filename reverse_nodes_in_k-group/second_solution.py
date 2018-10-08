# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverse_k_nodes(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode (new head)
    """
    prev_node = None
    cur_node = head
    for i in range(k):
        next_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node
    head.next = cur_node

    return prev_node


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2 or head is None is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        cur = prev.next

        while(cur is not None):
            # check if there is(are) next k-1 node(s)
            tmp = cur
            for i in range(k-1):
                tmp = tmp.next
                if tmp is None: return dummy.next

            # there is(are) next k-1 node(s)
            prev.next = reverse_k_nodes(cur, k)
            prev = cur
            cur = cur.next

        return dummy.next
