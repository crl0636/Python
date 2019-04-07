class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """

    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(self.dfs(nums, i, 0))
            else:
                res.append(0)

        return max(res)

    def dfs(self, nums, i, j):
        if i < 0 or i >= len(nums) or j>= len(nums) or (nums[i] == 0 and j != 0):
            return 0

        sum = 1
        sum += self.dfs(nums, i - 1, j + 1) + self.dfs(nums, i + 1, j+1)
        return sum


if __name__ == '__main__':
    so = Solution()
    so.findMaxConsecutiveOnes([1,0,1,1,0])