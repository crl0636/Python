class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        return 'LLL' not in s and  s.count('A') < 2