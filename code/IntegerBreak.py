class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:return n - 1

        dp = [0] * (n + 1)

        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            dp[i] = max(3 * dp[i - 3], 2 * dp[i - 2])

        return dp[n]