class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict = {}
        result = 0
        for letter in s:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1

        odd = 0
        for key, value in dict.iteritems():
            result += value if value %2 == 0 else value -1

            if value & 1:
                odd = 1

        result += odd

        return result