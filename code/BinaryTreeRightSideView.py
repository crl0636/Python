# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        self.helper(root, 0, res)
        print res
        return res

    def helper(self, root, level, res):
        """

        :type root: TreeNode
        :type res: List[int]
        :return:
        """
        if root:
            if level == len(res):
                res.append(root.val)

            if root.right:
                self.helper(root.right, level + 1, res)
            if root.left:
                self.helper(root.left, level + 1, res)


if __name__ == '__main__':
    so = Solution()
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(3)
    node3.right = node2
    node4 = TreeNode(2)
    node4.right = node1
    node5 = TreeNode(1)
    node5.left = node4
    node5.right = node3

    so.rightSideView(node5)