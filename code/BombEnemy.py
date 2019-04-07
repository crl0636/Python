class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here

        m = len(grid)
        n = len(grid[0])
        row = 0
        ans = 0
        col = [0 for i in xrange(n)]
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == "W":
                    row = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        elif grid[i][k] == 'E':
                            row += 1

                if i == 0 or grid[i - 1][j] == 'W':
                    col[j] = 0

                    for k in range(i, m):
                        if grid[i][k] == 'W':
                            break
                        elif grid[i][k] == 'E':
                            col[j] += 1
                if grid[i][j] == '0' or row + col[j] > ans:
                    ans = row + col[j]
        return ans

if __name__ == '__main__':
    so = Solution()
    print so.maxKilledEnemies(["0E00","E0WE","0E00"])