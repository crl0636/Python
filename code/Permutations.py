class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.help(res, [], nums)
        return res

    def help(self, res, list_, nums):
        if len(list_) == len(nums):
            res.append(list(list_))
            return

        for i in range(len(nums)):
            if nums[i] in list_:
                continue

            list_.append(nums[i])
            self.help(res, list_, nums)
            list_.pop()

if __name__ == '__main__':
    so = Solution()
    print so.permute([1,2,3])