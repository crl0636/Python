class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = []

        i = 0
        j = len(height) - 1
        while i < j:
            container = min(height[i], height[j]) * (j - i)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            res.append(container)

        return max(res)

if __name__ == '__main__':
    so = Solution()
    print so.maxArea([1,8,6,2,5,4,8,3,7])