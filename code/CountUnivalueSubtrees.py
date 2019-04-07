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
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """
    ans = 0

    def countUnivalSubtrees(self, root):
        # write your code here
        if not root:
            return 0
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        """

        :type root: TreeNode
        :param ans:
        :return:
        """
        if not root.left and not root.right:
            self.ans += 1
            return True

        if not root.left and root.right:
            r = self.dfs(root.right)

            if root.val == root.right.val and r:
                self.ans += 1
                return True
            else:
                return False
        elif not root.right:
            l = self.dfs(root.left)
            if l and root.val == root.left.val:
                self.ans += 1
                return True
            else:
                return False
        else:
            l = self.dfs(root.left)
            r = self.dfs(root.right)
            if l and r and root.val == root.right.val and root.val == root.left.val:
                self.ans += 1
                return True
            else:
                return False
if __name__ == '__main__':
    so = Solution()
