class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []

        res = []
        m = len(s)
        n = len(p)
        for i in range(m - n + 1):
            if self.sort(s[i:i + n]) == self.sort(p):
                res.append(i)
        return res

    def sort(self, s):
        list = []
        for c in s:
            list.append(c)

        list.sort()
        return "".join(list)

if __name__ == "__main__":
    so = Solution()
    print so.findAnagrams('abab', 'ab')