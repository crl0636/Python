from Queue import Queue
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here

        if len(edges) != n - 1:
            return False

        visited = {}
        neighbors = {}

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        queue = Queue()
        queue.put(0)

        while not queue.empty():
            cur = queue.get()
            visited[cur] = True
            for node in neighbors[cur]:
                if node not in visited:
                    visited[node] = True
                    queue.put(node)

        return len(visited) == n