class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            pass

        size = len(nums)
        snums = sorted(nums)
        for x in list(range(1, size, 2)) + list(range(0, size, 2)):
            nums[x] = snums.pop()

if __name__ == '__main__':
    so = Solution()
    so.wiggleSort([1, 5, 1, 1, 6, 4])