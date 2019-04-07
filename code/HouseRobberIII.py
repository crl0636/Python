# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return 0, 0

        rob_l, no_rob_l = self.dfs(root.left)

        rob_r, no_rob_r = self.dfs(root.right)

        return max(root.val + no_rob_l + no_rob_r, rob_l + rob_r), rob_l + rob_r