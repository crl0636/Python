class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dict = {}
        for num in nums:
            if num in dict:
                dict[num] = 'false'
            else:
                dict[num] = 'true'

        for key, value in dict.iteritems():
            if value == 'true':
                return key


if __name__ == '__main__':
    solution = Solution()
    solution.singleNumber([4,1,2,1,2])