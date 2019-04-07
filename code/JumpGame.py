class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = 0

        for i in range(len(nums)):
            if i > index:
                return False
            index = max(index, i + nums[i])

        return True