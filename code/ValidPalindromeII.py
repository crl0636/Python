class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return self.is_valid_palindrome(s, start + 1, end) or self.is_valid_palindrome(s, start, end - 1)

            start += 1
            end -= 1
        return True

    def is_valid_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -=1

        return True

if __name__ == '__main__':
    so = Solution()
    print so.validPalindrome("deee")