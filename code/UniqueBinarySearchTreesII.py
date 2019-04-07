# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return [None]
        return self.dfs(1, n)

    def dfs(self, start, end):
        res = []
        if start > end:
            res.append(None)

        for idx in range(start, end + 1):
            left_list = self.dfs(start, idx - 1)
            right_list = self.dfs(idx + 1, end)
            for left_node in left_list:
                for right_node in right_list:
                    root = TreeNode(idx)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        return res

if __name__ == "__main__":
    so = Solution()
    so.generateTrees(3)