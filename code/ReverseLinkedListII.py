# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        node  = dummy

        for i in range(m-1):
            node = node.next

        pre = node.next
        cur = pre.next

        for i in range(n-m):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        node.next.next = cur
        node.next = pre

        return dummy.next