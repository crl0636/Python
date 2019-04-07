class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, len(nums) - 1
                while l < r:
                    sum_ = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum_ == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif sum_ < target:
                        l += 1
                    else:
                        r -= 1
        return res

if __name__ == '__main__':
    so = Solution()
    so.fourSum([1, 0, -1, 0, -2, 2], 0)