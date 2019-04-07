class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        res = []

        self.dfs(res, [], nums, 0)
        if len(res) == 0:
            return False
        return True

    def dfs(self, res, list_, nums, idx):
        if len(list_) == 3 and list_ not in res:
            res.append(list(list_))

        for i in range(idx, len(nums)):
            if not list_ or list_[-1] < nums[i]:
                list_.append(nums[i])
                self.dfs(res, list_, nums, i + 1)
                list_.pop()