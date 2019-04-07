class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        if not s and not t:
            return False
            # write your code here
        m = len(s)
        n = len(t)
        if m == n:
            return self.is_change(s, t)
        elif m - 1 == n:
            return self.is_one_delete(t, s)
        elif n - 1 == m:
            return self.is_one_delete(s, t)
        else:
            return False

    def is_change(self, s, t):
        flag = False
        for i in range(len(s)):
            if s[i] != t[i]:
                if flag:
                    return False
                flag = True
        return flag

    def is_one_delete(self, short, longer):
        for i in range(len(short)):
            if short[i] != longer[i]:
                return short[i:] == longer[i + 1:]

        return True

if __name__ == '__main__':
    so = Solution()
    print so.isOneEditDistance('aDb', 'aDb')