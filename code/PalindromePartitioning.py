class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []

        res = []
        self.helper(res, [], s)
        return res

    def is_partition(self, s):
        return s == s[::-1]

    def helper(self, res, list_, s):
        if not s:
            res.append(list(list_))
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_partition(prefix):
                list_.append(prefix)
                self.helper(res, list_, s[i:])
                list_.pop()
