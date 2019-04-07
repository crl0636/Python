import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        if c < 0:
            return False

        left, right = 0, int(math.sqrt(c))
        while left <= right:
            if left * left + right * right < c:
                left += 1
            elif left * left + right * right >c:
                right -= 1
            else:
                return True
        return False