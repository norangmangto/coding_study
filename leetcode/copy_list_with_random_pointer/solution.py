# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None: return head

        copy_map = {}

        ori_head = head
        while head != None:
            # copy head
            if head not in copy_map:
                copy_map[head] = RandomListNode(head.label)
            cur = copy_map[head]

            # copy head.next
            if head.next is None:
                cur.next = None
            else:
                if head.next not in copy_map:
                    copy_map[head.next] = RandomListNode(head.next.label)

                cur.next = copy_map[head.next]

            # copy head.random
            if head.random is None:
                cur.random = None
            else:
                if head.random not in copy_map:
                    copy_map[head.random] = RandomListNode(head.random.label)

                cur.random = copy_map[head.random]

            # move to next node
            head = head.next

        return copy_map[ori_head]
