class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        for key, val in dict.iteritems():
            if val != 1:
                return key
