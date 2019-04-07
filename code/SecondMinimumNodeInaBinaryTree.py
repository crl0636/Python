# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        if not root.left and not root.right:
            return -1
        res = set()

        self.dfs(root, res)
        res = list(res)
        list.
        if len(res) == 1:
            return -1
        return sorted(res)[1]


    def dfs(self, root, res):
        """

        :type root: TreeNode
        :type res: set
        :return:
        """
        if root:
            res.add(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)

if __name__ == '__main__':
    so = Solution()
    node1  = TreeNode(5)
    node2 = TreeNode(8)
    node3 = TreeNode(5)
    node3.left = node2
    node3.right = node1
    print so.findSecondMinimumValue(node3)