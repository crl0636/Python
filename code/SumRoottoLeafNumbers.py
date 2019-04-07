# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = []

        self.helper(res, root, "")

        return sum([int(val) for val in res])

    def helper(self, res, root, path):
        """
                :type root: TreeNode
                :type res: List
                """
        if not root.left and not root.right:
            res.append(path + str(root.val))

        if root.left:
            self.helper(res, root.left, path + str(root.val))

        if root.right:
            self.helper(res, root.right, path + str(root.val))

if __name__ == '__main__':
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node = TreeNode(1)
    node.left = node1
    node.right = node2
    so = Solution()
    print so.sumNumbers(node)