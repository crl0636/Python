class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        visted = set()

        if n == 0: return False

        while True:
            num = 0
            while n > 0:
                num += (n % 10) ** 2
                n /= 10

            if num in visted:
                return False

            if num == 1:
                return True

            visted.add(num)

            n = num

        return False