class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        res = []
        self.helper(res, [], nums, 0)
        count = 0
        max_len = max([len(i) for i in res])
        for item in res:
            if len(item) == max_len:
                count += 1

        return count

    def helper(self, res, list_, nums, idx):
        if len(nums) == idx:
            res.append(list(list_))
            return

        for i in range(idx, len(nums)):
            if not list_ or list_[-1] < nums[i]:
                list_.append(nums[i])
                self.helper(res, list_, nums, i + 1)
                list_.pop()

if __name__ == '__main__':
    so =Solution()
    print so.findNumberOfLIS([2,2,2,2,2])