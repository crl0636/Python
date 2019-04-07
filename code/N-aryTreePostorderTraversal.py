"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        res = []

        if root is None:
            return []

        self.postorder2(root, res)

        return res

    def postorder2(self, root, res):

        for child in root.children:
            self.preorder2(child, res)

        if root:
            res.append(root.val)
