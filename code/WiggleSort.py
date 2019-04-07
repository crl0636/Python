class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here

        if not nums:
            pass

        for i in range(len(nums)):
            if (i + 1) % 2 != 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]

            if (i + 1) % 2 == 0 and nums[i] < nums[i - 1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]

        print nums

if __name__ == '__main__':
    so = Solution()
    so.wiggleSort([3, 5, 2, 1, 6, 4])