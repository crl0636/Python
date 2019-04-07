class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans = 0

        dict = {}

        for i in A:
            for j in B:
                key = i + j
                if key in dict:
                    dict[key] = dict.get(key) + 1
                else:
                    dict[key] = 1

        for i in C:
            for j in D:
                key = -(i + j)
                if key in dict:
                    ans += dict.get(key)

        return ans