# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        res = []
        nums = []
        self.helper(root, 0, res)
        for item in res:
            nums.append(float(sum(item)) / float(len(item)))
        return nums

    def helper(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])

            res[level].append(root.val)
            self.helper(root.left, level + 1, res)
            self.helper(root.right, level + 1, res)