class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        """

        :param words:
        :param word1:
        :param word2:
        :return:
        """

        if not words:
            return 0

        i = 0
        ans = float("inf")
        idx1 = idx2 = None
        is_same = False
        if word1 == word2:
            is_same = True

        while i < len(words):
            if words[i] == word1:
                if is_same and idx1:
                    ans = min(ans, abs(idx1 - i))
                idx1 = i
            if words[i] == word2:
                idx2 = i

            if idx1 and idx2:
                ans = min(ans, abs(idx1 - idx2))

            i += 1

        return ans

if __name__ == '__main__':
    so = Solution()
    print so.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes')