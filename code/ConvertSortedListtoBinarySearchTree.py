# Definition for singly-linked list.
import os

os.path

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.cur = None

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        return self.helper(self.get_size(head))

    def helper(self, size):
        if size <= 0:
            return None

        l = self.helper(size / 2)
        root = TreeNode(self.cur.val)
        self.cur = self.cur.next
        r = self.helper(size - size/2 - 1)
        root.left = l
        root.right = r
        return root

    def get_size(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count