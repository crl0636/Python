class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], nums)
        return res

    def helper(self, res, list_, nums):
        """

        :type res: list
        :type list_: list
        :type nums: list[int]
        :return:
        """
        res.append(list(list_))

        for i in range(len(nums)):
              list_.append(nums[i])
              self.helper(res, list_, nums[i+1:])
              list_.pop()

if __name__ == '__main__':
    so = Solution()
    print so.subsets([1, 2, 3])