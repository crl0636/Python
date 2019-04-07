class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        diff = (sum(A) - sum(B)) // 2

        A = set(A)
        for item in B:
            if item + diff in A:
                return [item + diff, item]