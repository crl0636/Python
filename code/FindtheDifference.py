class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for letter in set(t):
            if t.count(letter) != s.count(letter):
                return letter

if __name__ == '__main__':
    solution = Solution()
    solution.findTheDifference('abcd','abcde')