class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(nums)):
            if nums[i] == 1:
                res.append(self.dfs(nums, i))
            else:
                res.append(0)

        return max(res)

    def dfs(self, nums, i):
        if i < 0 or i >= len(nums) or nums[i] == 0:
            return 0

        nums[i] = 0
        sum = 1
        sum += self.dfs(nums, i-1) + self.dfs(nums, i+1)

        return sum