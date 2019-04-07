import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum = ans = 0
        d = collections.defaultdict(int)
        d[0] = 1

        for i in xrange(len(nums)):
            sum += nums[i]

            if k - sum in d:
                ans += d[k -sum]

            d[sum] += 1

        return ans