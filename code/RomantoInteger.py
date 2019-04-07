class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        MCMXCIV
        """
        pairs = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        result = pairs.get(s[-1])

        for i in range(len(s) -2 , -1 , -1):
            if pairs.get(s[i]) > pairs.get(s[i-1]):
                result -= pairs.get(s[i-1])
            else:
                result += pairs.get(s[i-1])
        return result