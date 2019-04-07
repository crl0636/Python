class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


if __name__ == '__main__':
    so = Solution()
    so.hammingWeight(128)