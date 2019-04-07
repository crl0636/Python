# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        return self.is_same(root.left, root.right)

    def is_same(self, p, q):
        """
            :type p: TreeNode
            :type q: TreeNode
            :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        return p.val == q.val and self.is_same(p.left, q.right) and self.is_same(p.right, q.left)