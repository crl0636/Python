# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = []
        if not t:
            return ""

        self.helper(t, res)
        return ''.join(str(item) for item in res)

    def helper(self, root, res):
        if not root:
            return

        res.append(root.val)
        if root.left or root.right:
            res.append('(')
            self.helper(root.left, res)
            res.append(')')

        if root.right:
            res.append('(')
            self.helper(root.right, res)
            res.append(')')

