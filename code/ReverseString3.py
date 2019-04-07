class Solution(object):
    def reverse_words(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for sub_string in s.split():
            if res == '':
                res = sub_string[::-1]
            else:
                res = res + ' ' + sub_string[::-1]
        return res

if __name__ == '__main__':
    s = Solution()
    test = "Let's take LeetCode contest"
    print s.reverse_words(test)