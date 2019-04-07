class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        current = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[current] = nums[i]
                current = current + 1

        return current


if __name__ == '__main__':
    obj = Solution()
    obj.removeElement([3,2,2,3], 3)