class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 1
        h = x
        while l <= h:
            mid = l + (h-l)/2
            if mid * mid > x:
                h = mid - 1
            else:
                l = mid + 1

        return h