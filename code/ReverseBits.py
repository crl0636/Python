class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[:1:-1]
        return int(b + '0' * (32-len(b)), 2)