class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums = set(sorted(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            for i in range(2):
                value = max(nums)
                nums.remove(value)
            return max(nums)

if __name__ == '__main__':
    so = Solution()
    print so.thirdMax([1, 2])