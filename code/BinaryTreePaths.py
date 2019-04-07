# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        res = []

        if not root:
            return res

        self.helper(res, root, "")
        return res

    def helper(self, res, root, path):
        if not root.left and not root.right:
            res.append(path + str(root.val))

        if root.left:
            self.helper(res, root.left, path + str(root.val) + "->")

        if root.right:
            self.helper(res, root.right, path + str(root.val) + "->")
