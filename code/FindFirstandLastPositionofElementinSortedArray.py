class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums:
            return [-1, -1]

        res = []
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                res.append(mid)
                break

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if not res:
            return [-1, -1]

        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == right - 1 or nums[mid + 1] != target):
                res.append(mid)
                break

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return res
    
if __name__ == '__main__':
    so = Solution()
    so.searchRange([1], 1)

