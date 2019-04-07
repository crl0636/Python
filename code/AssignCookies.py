class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0

        if not g or not s:
            return 0

        i, j = 0, 0
        g.sort()
        s.sort()
        while i< len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j +=1
        return res