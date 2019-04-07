class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def generateAbbreviations(self, word):
        # Write your code here

        res = []
        self.helper(res, word, 0, '', 0)
        return res

    def helper(self, res, word, pos, cur, count):
        if pos == len(word):
            if count > 0:
                cur = cur + str(count)
            res.append(cur)
        else:
            self.helper(res, word, pos + 1, cur, count + 1)
            if count > 0:
                cur = cur + str(count) + word[pos]
            else:
                cur = cur + word[pos]
            self.helper(res, word, pos + 1, cur, 0)

if __name__ == '__main__':
    so = Solution()
    so.generateAbbreviations('word')