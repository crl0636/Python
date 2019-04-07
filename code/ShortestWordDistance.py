class Solution(object):

    def shortestDistance(self, words, word1, word2):
        idx1 = len(words)
        idx2 = len(words)
        ans = 0
        for i in range(len(words)):
            if word1 == words[i]:
                idx1 = i
                ans = min(ans, abs(idx2 - idx1))
            elif word2 == words[i]:
                idx2 = i
                ans = min(ans, abs(idx2 - idx1))
        return ans