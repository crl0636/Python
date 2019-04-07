class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        result = 0
        if x < 0:
            x = abs(x)
            flag = -1

        while x > 0:
            if result > 2147483647 or result < -2147483648:
                return 0

            result = result * 10 + x % 10
            x /= 10
        return result * flag


if __name__ == '__main__':
    so = Solution()
    print so.reverse(123)