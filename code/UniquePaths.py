class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]

        return dp[m-1][n-1]