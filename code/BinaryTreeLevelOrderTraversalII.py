# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
            :type root: TreeNode
            :rtype: List[List[int]]
        """
        res = []

        if root is None:
            return []

        self.search_tree(root, 0, res)
        return res[::-1]

    def search_tree(self, root, level, res):

        if root:
            if len(res) < level + 1:
                res.append([])

            res[level].append(root.val)
            self.search_tree(root.left, level + 1, res)
            self.search_tree(root.right, level + 1, res)
