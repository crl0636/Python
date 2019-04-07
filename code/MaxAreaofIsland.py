class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dummy = len(grid[0])
        res = []
        for i in range(len(grid)):
            for j in range(dummy):
                if grid[i][j] == 1:
                    res.append(self.dfs(grid, i, j))
                else:
                    res.append(0)
        return max(res)

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0

        grid[i][j] = 0

        sum = 1
        sum += self.dfs(grid, i - 1, j) + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j - 1) + self.dfs(grid, i, j + 1)
        return sum