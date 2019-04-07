# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        sum = 0

        if root:
            l, r = root.left, root.right
            if l and (l.left is None and l.right is None):
                sum += l.val

            sum += self.sumOfLeftLeaves(l) + self.sumOfLeftLeaves(r)

        return sum