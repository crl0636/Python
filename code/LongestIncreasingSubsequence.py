class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        res = []

        self.helper(res, [], nums, 0)
        ans = 0
        print res
        for i in range(len(res)):
            ans = max(ans, len(res[i]))
        return ans

    def helper(self, res, list_, nums, idx):
        """

        :type res: List[List[String]
        :type list_: List[int]
        :param nums: List[int]
        :param idx: int
        :param cur: int
        :return:
        """

        if len(list_) >=1 and list_ not in res:
            res.append(list(list_))
        for i in range(idx, len(nums)):
            if not list_ or list_[-1] < nums[i]:
                list_.append(nums[i])
                self.helper(res, list_, nums, i + 1)
                list_.pop()


if __name__ == '__main__':
    so = Solution()
    print so.lengthOfLIS(
[10,9,2,5,3,7,101,18])