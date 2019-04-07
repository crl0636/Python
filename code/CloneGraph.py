# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        return self.helper(node, {})

    def helper(self, node , dict):

        if node in dict:
            return dict[node]

        output = UndirectedGraphNode(node.label)
        dict[node] = output

        for neighbor in node.neighbors:
            node.neighbors.append(self.helper(neighbor, dict))

        return output