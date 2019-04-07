# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        pre = cur = dummy

        while pre and n >=0:
            pre = pre.next
            n -= 1

        while pre:
            pre = pre.next
            cur = cur.next

        cur.next = cur.next.next
        return dummy.next