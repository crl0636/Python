class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()

        dp = [0] * len(nums)
        parent = [0] * len(nums)
        mx = 0
        mx_idx = -1
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_idx = i
        res = list()
        for k in range(mx + 1):
            res.append(nums[mx_idx])
            mx_idx = parent[mx_idx]
        return res[::-1]

if __name__ == '__main__':
    so = Solution()
    so.largestDivisibleSubset([1, 2, 4, 8])

