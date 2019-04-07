# Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        return self.validBST(root, -sys.maxint, sys.maxint)

    def validBST(self, root, min, max):
        """
                :type root: TreeNode
                :rtype: bool
                """
        if not root:
             return True

        if root.val >= max or root.val <= min:
            return False

        return self.validBST(root.left, min, root.val) and self.validBST(root.right, root.val, max)

