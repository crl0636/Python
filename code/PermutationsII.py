class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.help(res, [], nums)
        return res

    def help(self, res, list_, nums):
        if not nums:
            res.append(list(list_))
            return

        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                continue
            list_.append(nums[i])
            self.help(res, list_, nums[:i] + nums[i + 1:])
            list_.pop()

if __name__ == '__main__':
    so = Solution()
    print so.permute([1,1,2])