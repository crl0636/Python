class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.helper(res, [], nums)
        return res

    def helper(self, res, list_, nums):
        if not nums:
            res.append(list(list_))
            return

        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                continue
            list_.append(nums[i])
            self.helper(res, list_, nums[:i] + nums[i + 1:])
            list_.pop()

if __name__ == '__main__':
    so = Solution()
    print so.subsetsWithDup([1,2,2])