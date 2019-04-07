# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        if not root:
            return 0

        self.max_path(root)
        return self.result

    def max_path(self, root):
        if not root:
            return 0

        left = self.max_path(root.left)
        right = self.max_path(root.right)

        self.result = max(self.result, left + right)
        return max(left, right) + 1
