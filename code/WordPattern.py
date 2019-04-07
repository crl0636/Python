class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        dict = {}
        strs = str.split(" ")
        if len(pattern) != len(strs):
            return False

        for i in range(len(pattern)):
            letter_pattern = pattern[i]
            word_str = strs[i]

            if letter_pattern in dict:
                if dict[letter_pattern] == word_str:
                    continue
                else:
                    return False
            else:
                if word_str not in dict.values():
                    dict[letter_pattern] = word_str
                else:
                    return False

        return True


if __name__ == '__main__':
    so = Solution()
    so.wordPattern('abba', 'dog cat cat dog')