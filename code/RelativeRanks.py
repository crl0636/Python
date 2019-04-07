class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        numssort = nums[:]
        numssort.sort()
        numssort = numssort[::-1]
        ls = []
        for i in nums:
            j = numssort.index(i) + 1
            if j == 1:
                ls.append("Gold Medal")
            elif j == 2:
                ls.append("Silver Medal")
            elif j == 3:
                ls.append("Bronze Medal")
            else:
                ls.append(str(j))
        return ls


if __name__ == '__main__':
    so = Solution()
    print so.findRelativeRanks([5,4,3,2,1])