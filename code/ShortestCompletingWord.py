class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        dict_li = {}
        res = []
        for letter in licensePlate:
            if letter.isalpha():
                if letter.lower() not in dict_li:
                    dict_li[letter.lower()] = 1
                else:
                    dict_li[letter.lower()] += 1

        for word in words:
            dict_w = {}

            for letter in word:
                if letter.lower() not in dict_w:
                    dict_w[letter.lower()] = 1
                else:
                    dict_w[letter.lower()] += 1

            same = True
            for key, val in dict_li.iteritems():
                if key in dict_w:
                    if val > dict_w[key]:
                        same = False
                        break
                else:
                    same = False
                    break
            if same:
                res.append(word)

        res.sort(key=lambda x:len(x))
        return res

if __name__ == '__main__':
    so = Solution()
    print so.shortestCompletingWord("GrC8950", ["measure", "other", "every", "base", "according", "level", "meeting", "none", "marriage", "rest"])
