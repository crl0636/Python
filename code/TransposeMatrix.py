class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        output = [[0]*len(A) for i in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                output[j][i] = A[i][j]

        return output

if __name__ == '__main__':
    so = Solution()
    print so.transpose([[1,2,3],[4,5,6]])