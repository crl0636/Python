# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        res = [[]]
        if root is None:
            return []

        queue = [(root,0)]

        while queue:
            node, level = queue.pop(0)

            if level >= len(res):
                return res.append([])

            res[level] = res.append(node.val)

            for child in node.children:
                queue.append(child, level + 1)


