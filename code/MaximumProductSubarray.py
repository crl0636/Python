class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0] = nums[0]
        dp2[0] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            dp1[i] = max(nums[i], dp1[i-1] * nums[i], dp2[i-1] * nums[i])
            dp2[i] = min(nums[i], dp1[i-1] * nums[i], dp2[i-1] * nums[i])

            res = max(res, dp1[i])
        return res