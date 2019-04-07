class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        model = [['Q','W','E', 'R','T','Y','U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                        ['Z','X','C', 'V', 'B', 'N', 'M']]

        res = []

        if not words or len(words) == 0:
            return res

        for line in model:
            for word in words:
                is_same_line = True

                for character in word.upper():
                    if character not in line:
                        is_same_line = False
                        break

                if is_same_line:
                    res.append(word)

        return res

if __name__ == '__main__':
    so = Solution()
    print so.findWords(["Hello", "Alaska", "Dad", "Peace"])
