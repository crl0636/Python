class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount

        for i in range(amount):
            if dp[i] < 0:
                continue
            for c in coins:
                if i + c > amount:
                    continue
                if dp[i + c] < 0 or dp[i + c] > dp[i] + 1:
                    dp[i + c] = dp[i] + 1

        return dp[amount]



if __name__ == '__main__':
    so = Solution()
    print so.coinChange([1,2,3,5], 31)