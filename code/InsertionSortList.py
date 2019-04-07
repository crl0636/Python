# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        cur = dummy
        while head:
            if cur and cur.val > head.val:
                cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, cur.next.next, head = head, cur.next, head.next

        return dummy.next

if __name__ == '__main__':
    so = Solution()
    node1 = ListNode(3)
    node2 = ListNode(1)
    node2.next = node1

    node3 = ListNode(2)
    node3.next = node2

    node4 = ListNode(4)
    node4.next = node3
    so.insertionSortList(node4)