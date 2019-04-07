# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(0)
        small_head = ListNode(0)
        big_head = ListNode(0)

        dummy.next = head
        pre = dummy
        small = small_head
        big = big_head
        while pre.next:
            cur = pre.next
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next
            pre = pre.next
        big.next = None
        small.next = big_head.next
        return small_head.next
