# Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.previous = self.minimum = float('inf')
        self.inorder(root)
        return self.minimum

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.minimum = min(self.minimum, abs(node.val - self.previous))
            self.previous = node.val
            self.inorder(node.right)