# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = set()
        self.helper(root, res)
        return len(res) == 1

    def helper(self, root, res):
        if root:
            res.add(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)

if __name__ == '__main__':
    so = Solution()
    so.isUnivalTree()