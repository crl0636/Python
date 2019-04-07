class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def compare(x, y):
            return int(y + x) - int(x + y)

        nums = [str(num) for num in nums]
        ans = sorted(nums, cmp=compare)
        if ans == '0':
            return '0'
        return ''.join(ans).lstrip('0')



if __name__ == '__main__':
    so = Solution()
    print so.largestNumber([3, 30, 34, 5, 9])