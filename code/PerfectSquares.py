class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1

        return dp[n]

if __name__ == '__main__':
    so = Solution()
    so.numSquares(12)