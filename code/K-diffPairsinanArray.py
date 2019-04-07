import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 0:
            return 0
        count  = 0
        c = collections.Counter(nums)
        for i in c:
            if (k > 0 and i + k in c) or (k == 0 and c[i] > 1):
                count += 1
        return count



if __name__ == '__main__':
    so  = Solution()
    so.findPairs([3, 1, 4, 1, 5], 2)