class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        divisor = []
        for i in xrange(num):
            if i * i > num:
                break
            if num % i == 0:
                divisor.append(i)

        if sum(divisor) == num:
            return True

        return False