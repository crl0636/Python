import math
class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """
    def getFactors(self, n):
        # write your code here
        if not n:
            return []

        res = []
        self.helper(res, [], n, 2)
        return res

    def helper(self, res, list_, n, factor):
        """

        :type res: List
        :type list_: list[]
        :param n:
        :param factor:
        :return:
        """
        if n == 1:
            if len(list_) > 1:
                res.append(list(list_))
                return

        for i in xrange(factor, n + 1):
            if n % i == 0:
                list_.append(i)
                self.helper(res, list_, n / i, i)
                list_.pop()

if __name__ == '__main__':
    so = Solution()
    print so.getFactors(23848713)