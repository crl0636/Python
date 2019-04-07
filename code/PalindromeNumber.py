class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = 1
        reversed = 0

        if x < 0:
            flag = -1
            x = abs(x)

        while x > 0:
            reversed = reversed * 10 + x%10
            x = x / 10

        return x == reversed * flag


if '__name__' == '__main__':
    obj  = Solution()
    obj.isPalindrome(121)
