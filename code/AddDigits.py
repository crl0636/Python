import os
os

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        sum = 0

        while num != 0:
            sum += num%10
            num /=10

        if sum >= 10:
            return self.addDigits(sum)
        else:
            return sum

if __name__ == '__main__':
    so = Solution()
    so.addDigits(19)