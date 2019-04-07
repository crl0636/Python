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
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        if not root:
            return []
        res = {}
        ans  = []
        max_path = self.helper(root, res)
        for i in range(max_path):
            ans.append(res[i])
        return ans

    def helper(self, root, res):
        if not root:
            return -1
        left = self.helper(root.left, res)
        right = self.helper(root.right, res)

        cur = max(left, right) + 1
        if len(res) == cur:
            res.append([])

        res[cur].append(root.val)
        return cur
