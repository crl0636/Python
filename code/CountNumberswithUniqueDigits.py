class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2 : return 10 ** n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 10
        dp[2] = 81
        for i in range(3, n + 1):
            dp[i] = dp[i-1] * (10 - i + 1)
        ans  = 0

        for i in range(1, n + 1):
            ans += dp[i]
        return ans

if __name__ == '__main__':
    so = Solution()
    print so.countNumbersWithUniqueDigits(4)