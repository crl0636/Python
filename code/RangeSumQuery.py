class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        list = self.nums[i:j]

        return sum(list)

if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    param_1 = obj.sumRange(0,2)