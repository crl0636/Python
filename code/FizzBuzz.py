class Solution(object):
    def fizz_buzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = list()
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result


if __name__ == '__main__':
    s = Solution()
    print s.fizz_buzz(20)