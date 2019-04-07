"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here

        if not root:
            return 0

        res = self.helper(root, None, 0)
        return res

    def helper(self, root, parent, res):
        """

        :type root: TreeNode
        :type parent: TreeNode
        :type res: List
        :param out:
        :return:
        """
        if root:
            if parent and root.val - parent.val ==  1:
                res += 1
            else:
                res = 1

            return max(res, self.helper(root.left, root, res), self.helper(root.right, root, res))