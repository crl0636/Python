class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        longest = 0
        for key, value in dict.iteritems():
            if key - 1 in dict:
                longest = max(longest, value + dict[key - 1])
            if key + 1 in dict:
                longest = max(longest, value + dict[key + 1])
        return longest