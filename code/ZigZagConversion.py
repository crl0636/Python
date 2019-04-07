class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        res = [''] * numRows

        for i in range(len(s)):
            line = i % (2*numRows - 2)
            if line >= numRows:
                line = 2*numRows -2 - line

            res[line] += s[i]

        return ''.join(res)