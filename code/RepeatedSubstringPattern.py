class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for i in range(1, len(s) / 2 + 1):
            if len(s) % i == 0:
                sub_str = s[:i]

                if sub_str * (len(s) / i) == s:
                    return True

        return False
