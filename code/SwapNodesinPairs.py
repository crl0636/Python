# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        dummy = cur = ListNode(0)
        dummy.next = head
        while head and head.next:
            p = head.next.next
            cur.next = head.next
            cur.next.next = head
            head.next = p
            cur = head
            head = p
        return dummy.next