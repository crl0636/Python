class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        for letter in s:
            res = res * 26 + ord(letter) - 64
        return res