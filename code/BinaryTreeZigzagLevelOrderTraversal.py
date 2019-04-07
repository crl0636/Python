# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :c root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        output = []*len(res)

        if root is None:
            return []

        self.helper(root, 0, res)

        for level in range(len(res)):
            if level % 2 != 0:
                output.append(res[level][::-1])
            else:
                output.append(res[level])

        return output

    def helper(self, root, level, res):
        """

        :type root:  TreeNode
        :param level:
        :TreeNode res: List[List[int]]
        :return:
        """
        if root:
            if len(res) < level + 1:
                res.append([])

            res[level].append(root.val)

            self.helper(root.left, level + 1, res)
            self.helper(root.right, level + 1, res)