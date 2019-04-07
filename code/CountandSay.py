class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'

        for i in xrange(n - 1):
            new_res = ''
            j = 0
            while j < len(res):
                count = 1
                while j < len(res) - 1 and res[j] == res[j + 1]:
                    j += 1
                    count += 1
                j += 1
                new_res += str(count) + res[j - 1]
            res = new_res
        return res
