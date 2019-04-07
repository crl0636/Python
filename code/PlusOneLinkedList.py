"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        if not head:
            return head

        reversed_item = self.reversed(head)
        cur = reversed_item
        cur.val += 1
        while cur and cur.val >= 10:
            cur.val -= 10

            if cur.next:
                cur.next.val += 1
            else:
                cur.next = ListNode(1)
            cur = cur.next

        reversed_item = self.reversed(reversed_item)
        return reversed_item

    def reversed(self, head):
        """
        :type head:  ListNode
        :return:
        """
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre
