# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return abs(self.sum_tree(root.left) - self.sum_tree(root.right)) + self.findTilt(root.left) + self.findTilt(
            root.right)

    def sum_tree(self, root):
        if not root:
            return 0

        return self.sum_tree(root.left) + self.sum_tree(root.right) + root.val