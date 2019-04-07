class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_len = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                tag = False
                for k in range(len(words[j])):
                    if words[j][k] in words[i]:
                        tag = True
                        break

                if tag:
                    continue

                max_len = max(max_len, len(words[i]) * len(words[j]))
        return max_len

if __name__ == '__main__':
    so =  Solution()
    print so.maxProduct(["a","aa","aaa","aaaa"])
