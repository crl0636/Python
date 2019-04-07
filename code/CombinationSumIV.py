class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(target + 1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i-j]
        return dp[target]

if __name__ == '__main__':
    so =Solution()
    print so.combinationSum4([1, 2, 3], 4)