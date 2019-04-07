class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        ans = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1

            ans = min(ans, nums[mid])
        return ans