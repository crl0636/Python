import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        return math.sqrt(n)

if __name__ == '__main__':
    so = Solution()
    print so.bulbSwitch(3)