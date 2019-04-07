# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []

        self.helper(root, 0, res)
        return res


    def helper(self, root, level, res):
        """
        :type root: TreeNode
        :param level:
        :type res: List[List[int]]
        :return:
        """

        if root:
            if len(res) < level + 1:
                res.append([])

            res[level].append(root.val)
            self.helper(root.left, level + 1, res)
            self.helper(root.right, level + 1, res)