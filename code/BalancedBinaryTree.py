# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if abs(self.max_depth(root.left) - self.max_depth(root.right)) <= 1:
            return self.isBalanced(root.left)  and self.isBalanced(root.right)
        else:
            False

    def max_depth(self, root):
        """
            :type root: TreeNode
            :rtype: int
        """
        if root is None:
            return 0

        left_length = self.max_depth(root.left)
        right_length = self.max_depth(root.right)

        return max(left_length, right_length) + 1


if __name__ == '__main__':
    solution = Solution()
    solution.isBalanced([1,2,2,3,3,None,None,4,4])