import random
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.item = []

        while head:
            self.item.append(head.val)
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return random.sample(self.item, 1).pop()