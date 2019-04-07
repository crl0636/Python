class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        cur = 1
        pre = 0

        if not s:
            return res

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                pre = cur
                cur = 1

            if pre >= cur:
                res += 1

        return res