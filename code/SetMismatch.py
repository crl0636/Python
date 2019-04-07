class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        dict = {}
        missing = []

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        for key, val in dict.iteritems():
            if val == 2:
                missing.append(key)

        for i in range(1,len(nums)):
            if i not in dict:
                missing.append(i)

        return missing