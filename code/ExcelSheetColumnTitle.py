class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""

        return self.convertToTitle((n-1) / 26) + chr((n-1) % 26 + ord('A'))