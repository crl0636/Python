class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1

        left = 0

        right = sum(nums[1:])

        for i in range(1, len(nums)):
            left += nums[i - 1]
            right -= nums[i]

            if left == right:
                return i

        return -1

if __name__ == '__main__':
    so = Solution()
    print so.pivotIndex([1, 7, 3, 6, 5, 6])