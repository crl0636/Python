class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        l, r = 0, 0
        sum = 0
        res = float('inf')

        while r < len(nums):
            sum += nums[r]

            while sum >= s:
                res = min(res, (r - l + 1))
                sum -= nums[l]
                l += 1
            r += 1

        return res if res != float('inf') else 0