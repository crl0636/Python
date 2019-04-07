class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')

        n = 1
        for node in nodes:
            n -= 1
            if n < 0:
                return False

            if node != '#':
                n += 2

        return n == 0