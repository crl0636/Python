class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict = {}
        if not s:
            return -1

        for letter in s:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1

        for letter in s:
            if dict[letter] == 1:
                return s.index(letter)

        return -1

if __name__ == '__main__':
    solution = Solution()
    solution.firstUniqChar('leetcode')