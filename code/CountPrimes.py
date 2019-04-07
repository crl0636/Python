class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        prime = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(i**2, n, i):
                    prime[j] = False

        return sum(prime) - 2

    def count_primes(self,n):
        is_prime = [True] * (n + 1)
        primes = [0] * (n + 1)
        p = 0
        is_prime[0] = is_prime[1] = False
        for i in range(2, n):
            if is_prime[i]:
                primes[p] = i
                p += 1
                for j in range(i**2, n + 1, i):
                    is_prime[j] = False
        return p


if __name__ == '__main__':
    so = Solution()
    print so.count_primes(150000)
