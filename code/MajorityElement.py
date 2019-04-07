class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}

        mid = len(nums) / 2

        for num in nums:
            if num in dict:
                number = dict[num]
                number += 1
                dict[num] = number
            else:
                dict[num] = 1

        for key, value in dict.iteritems():
            if value > mid :
                return key

if __name__ == '__main__':
    obj = Solution()
    obj.majorityElement([2,2,1,1,1,2,2])