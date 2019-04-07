# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return []

        res =[]
        self.helper(root, res)
        return res[k - 1]

    def helper(self, root, res):
        """
        :type root: TreeNode
        :type res: List[]
        :return:
        """
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

if __name__ == '__main__':
    so = Solution()
    print so.kthSmallest([3,1,4,None,2], 1)