class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for i in range(len(haystack)):
            print haystack[i:i+len(needle)]
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

if __name__ == '__main__':
    obj = Solution()
    print obj.strStr('hello','ll')