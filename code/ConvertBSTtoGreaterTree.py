# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.sum = 0
        self.helper(root)
        return root

    def helper(self, root):

        if not root:
            return

        if root.right:
            self.helper(root.right)
        tmp = root.val
        root.val += self.sum
        self.sum += tmp
        if root.left:
            self.helper(root)