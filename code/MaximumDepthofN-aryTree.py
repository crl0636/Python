# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return 0

        res = []
        for child in root.children+[None]:
            child_dapth = self.maxDepth(child)
            res.append(child_dapth)

        return max(res) + 1
