class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        dict = {}

        res = False
        for num in nums:
            if num in dict:
                res = True
            else:
                dict[num] = 1

        return res