# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []

        if root is None:
            return []

        self.preorder2(root, res)

        return res

    def preorder2(self, root, res):
        if root:
            res.append(root.val)

        for child in root.children:
            self.preorder2(child, res)