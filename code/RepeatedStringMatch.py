class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        tmp = ''
        i = 0

        while i < len(B) / len(A) + 3:
            tmp += A
            i += 1
            if B in tmp:
                return i
        return -1