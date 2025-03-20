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

        while len(lists) > 1:
            new_lists = []
            if len(lists) % 2 == 1:  # odd
                new_lists.append(lists.pop())

            for i in range(0, len(lists), 2):
                new_lists.append(self.merge_lists(lists[i], lists[i+1]))

            lists = new_lists

        return lists[0]

    def merge_lists(self, list1, list2):
        head = point = ListNode(0)

        while list1 is not None or list2 is not None:
            if list1 is None:
                point.next = list2
                break
            elif list2 is None:
                point.next = list1
                break
            else:
                if list1.val < list2.val:
                    point.next = list1
                    list1 = list1.next
                    point = point.next
                else:
                    point.next = list2
                    list2 = list2.next
                    point = point.next
        return head.next
