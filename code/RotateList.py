# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return None

        cur = head
        length = 1
        while cur:
            cur = cur.next
            length += 1

        cur.next = head
        curr = head
        shift = length - k%length

        while shift > 0:
            cur = cur.next
            shift -= 1

        ans  = cur.next
        cur.next = None

        return ans