class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        case1 = True

        for i in range(len(A) - 1):
            j = i + 1
            if A[i] > A[j]:
                case1 = False
                break

        case2 = True

        for i in range(len(A) - 1):
            j = i + 1
            if A[i] < A[j]:
                case2= False
                break

        return case1 or case2