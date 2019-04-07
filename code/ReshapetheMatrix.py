class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        m = len(nums)
        n = len(nums[0])

        if m*n != r*c:
            return nums

        numbers = [n for num in nums for n in num]
        res =[]
        for i in range(0, len(numbers), c):
            res.append(numbers[i:i+c])
        return res
if __name__ == '__main__':
    so = Solution()
    so.matrixReshape([[1,2],[3,4]],2,2)