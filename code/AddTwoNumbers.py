# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        sum = 0
        cur = dummy
        p1, p2 = l1, l2

        while p1 or p2:
            if p1:
                sum += p1.val
                p1 = p1.next

            if p2:
                sum += p2.val
                p2 = p2.next

            cur.next = ListNode(sum%10)
            sum /= 10
            cur = cur.next
        if sum == 1:
            cur.next = ListNode(1)

        return dummy.next