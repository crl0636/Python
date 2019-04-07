# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """

        if not headA or not headB:
            return None

        list = set()

        while headA != None:
            list.add(headA.val)
            headA = headA.next

        while headB:
            if headB.val in list:
                return headB

            headB = headB.next
        return None