# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        ans = []
        self.pre_order_trvel(root, ans)

        copy = root
        for i in range(1, len(ans)):
            copy.left = None
            copy.right = ans[i]
            copy = ans[i]

    def pre_order_trvel(self, root, ans):
        if not root:
            return
        ans.append(root)
        self.pre_order_trvel(root.left, ans)
        self.pre_order_trvel(root.right, ans)