class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i for i in range(1,n + 1)]
        self.helper(res, [], nums)
        return "".join([str(num) for num in res[k - 1]])

    def helper(self, res, list_, nums):
        """
               :type list_: list
               :type nums: list
               :type res: list
        """
        if len(list_) == len(nums):
            res.append(list(list_))
            return

        for i in range(len(nums)):
            if nums[i] in list_:
                continue

            list_.append(nums[i])
            self.helper(res, list_, nums)
            list_.pop()

if __name__ == '__main__':
    so = Solution()
    print so.getPermutation(4, 9)