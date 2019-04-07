class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        num = 0

        while True:
            n = int(n / 5)
            if n == 0:
                break
            num = num + n

        return num

if __name__ == '__main__':
    solution = Solution()
    solution.trailingZeroes(6860)