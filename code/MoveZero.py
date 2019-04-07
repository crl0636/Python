class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0

        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1


