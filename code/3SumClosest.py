class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        res = nums[0] + nums[1] + nums[len(nums) -1]
        nums.sort()
        for i in range(len(nums) -2):
            l, r = i+1, len(nums) - 1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > target:
                    r -= 1
                else:
                    l += 1
                if abs(sum - target) < abs(res - target):
                    res = sum

        return res