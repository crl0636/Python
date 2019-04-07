# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        if root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1

        if root.right is None and root.left is not None:
            return self.minDepth(root.left) + 1

        left_length = self.minDepth(root.left)
        right_length = self.minDepth(root.right)

        return min(left_length, right_length) + 1