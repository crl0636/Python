class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []

        ans =[[0] * n for i in range(n)]

        top = left = 0
        bottom = n - 1
        right = n - 1
        num = 1

        while top < bottom and left < right:
            for i in range(left, right):
                ans[top][i] = num
                num += 1
            for i in range(top, bottom):
                ans[i][right] = num
                num += 1
            for i in range(right, left, -1):
                ans[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                ans[i][left] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if top == bottom and left == right:
            ans[top][left] = num
        return ans

if __name__ == '__main__':
    so  = Solution()
    print so.generateMatrix(3)