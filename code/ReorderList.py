# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        mid = self.find_middle(head)
        tail = self.reverse(mid.next)
        mid.next = None
        self.merge(head, tail)

    def find_middle(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp

        return pre

    def merge(self, head1, head2):
        index = 0
        dummy = ListNode(0)
        while head1 and head2:
            if index%2==0:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
            index += 1
        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2

