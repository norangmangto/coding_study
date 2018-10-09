# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return lists

        # To remove empty list (ex. [[]])
        for i in range(len(lists)-1, -1, -1):
            if lists[i] is None:
                lists.pop(i)

        head = prev = ListNode(0)
        while len(lists) > 0:
            min_index = 0
            min_node = lists[0]
            for i in range(1, len(lists)):
                if min_node.val > lists[i].val:
                    min_index = i
                    min_node = lists[i]

            if min_node.next is None:
                lists.pop(min_index)
            else:
                lists[min_index] = min_node.next
            prev.next = min_node
            prev = prev.next

        return head.next
