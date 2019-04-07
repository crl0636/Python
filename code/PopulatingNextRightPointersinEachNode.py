# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            pass
        res = []
        self.helper(res, root, 0)
        for i in range(len(res)):
            for j in range(len(res[i]) - 1):
                res[i][j].next = res[i][j + 1]

    def helper(self, res, root, level):
        if root:
            if len(res) < level + 1:
                res.append([])

            res[level].append(root)
            self.helper(res, root.left, level + 1)
            self.helper(res, root.right, level + 1)
