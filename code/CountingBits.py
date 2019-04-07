class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num + 1):
            res.append(self.to_bits(i).count('1'))

    def to_bits(self, num):
        return bin(num)

if __name__ == '__main__':
    so =Solution()
    so.countBits(5)