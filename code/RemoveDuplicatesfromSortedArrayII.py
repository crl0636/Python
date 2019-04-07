class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)

        i = 2

        while i < len(nums):
            if nums[i] == nums[i-1] and nums[i-1] == nums[i-2]:
                nums.pop()
            else:
                i += 1

        return len(nums)