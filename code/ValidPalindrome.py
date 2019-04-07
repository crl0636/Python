class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        list = []
        for c in s.lower():
            if c.isalnum():
                list.append(c)

        return list == list[::-1]