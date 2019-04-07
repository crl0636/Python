class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here

        m = len(A)
        n = len(A[0])
        k = len(B[0])

        c = [[0 for _ in xrange(k)] for _ in xrange(m)]

        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for o in range(k):
                        c[i][o] += A[i][j] * B[j][o]
        return c

if __name__ == '__main__':
    so = Solution()
    so.multiply([
  [ 1, 0, 0],
  [-1, 0, 3]
], [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
])