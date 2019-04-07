class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        if n != 1:
            while n > 1:
                if n % 2 != 0:
                    return False
                n /= 2
            return True
        else:
            return True