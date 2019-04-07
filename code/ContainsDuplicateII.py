class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        dict = {}

        for i in range(len(nums)):
            idx = dict.get(nums[i])

            if idx >= 0 and i - idx <= k:
                return True

            dict[nums[i]] = i
        return False