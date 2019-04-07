class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        self.helper(s, res, [])
        return res


    def is_palindromic(self, s):
        return s == s[::-1]

    def helper(self, s, res, list_):
        if not s:
            res.append(list(list_))
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindromic(prefix):
                list_.append(prefix)
                self.helper(s[i:],res, list_)
                list_.pop()

if __name__ == '__main__':
    so =Solution()
    print so.countSubstrings('aaa')