class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        nums = set(nums)
        for i in range(1, n + 1):
            if i not in nums:
                res.append(i)

        return res

if __name__ == '__main__':
    so = Solution()
    print so.findDisappearedNumbers([1,1])