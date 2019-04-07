class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd =[]
        even = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])

        return even + odd

if __name__ == '__main__':
    so = Solution()
    print so.sortArrayByParity([3,1,2,4])