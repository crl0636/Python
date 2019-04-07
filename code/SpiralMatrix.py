class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0:
            return []
        
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        ans = []
        while top < bottom and left < right:
            for i in range(left, right):
                ans.append(matrix[top][i])
            for i in range(top, bottom):
                ans.append(matrix[i][right])
            for i in range(right, left, -1):
                ans.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                ans.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if left == right and top == bottom:
            ans.append(matrix[top][left])
        elif left == right:
            for i in range(top, bottom + 1):
                ans.append(matrix[i][left])
        elif top == bottom:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])

        return ans

if __name__ == '__main__':
    so  = Solution()
    so.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])