# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res =[]
        ans = 0
        self.helper(root, res, 0)
        for item in res:
            ans += len(item)

        return ans

    def helper(self, root, res, level):
        """

        :type root: TreeNode
        :type res:  List[int]
        :param level:
        :return:
        """
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)

            if root.left:
                self.helper(root.left, res, level + 1)

            if root.right:
                self.helper(root.right, res, level + 1)