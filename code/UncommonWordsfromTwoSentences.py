class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dict_A = {}
        dict_B = {}
        ans = []

        for item in A.split():
            if item not in dict_B:
                dict_B[item] = 0
            dict_B[item] += 1

        for item in B.split():
            if item not in dict_A:
                dict_A[item] = 0
            dict_A[item] += 1

        for k, v in dict_A.iteritems():
            if v == 1 and k not in dict_B:
                ans.append(k)

        for k, v in dict_B.iteritems():
            if v == 1 and k not in dict_A:
                ans.append(k)
        return ans

if __name__ == '__main__':
    so = Solution()
    print so.uncommonFromSentences('this apple is sweet', 'this apple is sour')