class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 0:
            return 0
        if N == 1:
            return 1
        if N >= 2:
            dp = [0] * (N + 1)
            dp[0] = 0
            dp[1] = 1
            for i in range(2, N + 1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[N]

    def fib2(self, N):
        if N <= 0: return 0

        if N == 1: return 1

        if N >= 2:
            return self.fib2(N-1) + self.fib2(N-2)

if __name__ == '__main__':
    so = Solution()
    print so.fib(4)