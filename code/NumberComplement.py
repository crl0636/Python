class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = ''
        for i in bin(num)[2:]:
            x += str(1 - int(i))

        return int(x, 2)