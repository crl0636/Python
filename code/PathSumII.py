# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []

        if not root: return []

        self.helper(res, root, sum, [])
        return res

    def helper(self, res, root, sum, path):
        """
               :type root: TreeNode
               :type sum: int
               :type res: List[List[int]]
               :type path: List[]
               """
        if not root.left and not root.right and sum == root.val:
            res.append(path + [root.val])

        if root.left:
            self.helper(res, root.left, sum-root.val, path + [root.val])

        if root.right:
            self.helper(res, root.right, sum-root.val, path + [root.val])