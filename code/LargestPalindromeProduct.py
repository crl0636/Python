class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9

        upper = pow(10, n) - 1
        lower = upper/10 + 1
        max_num = upper * upper
        parlindrome = 0
        half = max_num/pow(10, n)
        found = False

        while not found:
            parlindrome = self.create_num(half)
            i = upper
            while i >= lower:
                if i * i < parlindrome:
                    break

                if parlindrome % i == 0:
                    found = True
                    break
                i -= 1
            half -= 1
        return int(parlindrome % 1337)

    def create_num(self, num):
        tmp = str(num)[::-1]
        return int(str(num) + tmp)

if __name__ == '__main__':
    so = Solution()
    print so.largestPalindrome(8)