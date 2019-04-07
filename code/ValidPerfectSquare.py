class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        left, right = 1, num

        mid = (left + right) // 2
        while left <= right and mid * mid != num:
            if mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2

        return mid * mid == num
