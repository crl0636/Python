import sys
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for i in range(n + 1)]
        for j in range(2, n + 1):
            dp[j - 1][j] = min(j, j - 1)
            for i in range(j - 2, 0, -1):
                temp = float("inf")
                for k in range(i + 1, j):
                    temp = min(temp, k + max(dp[i][k - 1], dp[k + 1][j]))
                dp[i][j] = temp
        return dp[1][n]
if __name__ == '__main__':
    so = Solution()
    print so.getMoneyAmount(2)