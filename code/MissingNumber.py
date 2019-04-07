class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums = sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return nums[i]
            else:
                continue



if __name__ == '__main__':
    so = Solution()
    print so.missingNumber([9,6,4,2,3,5,7,0,1])