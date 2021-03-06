# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next