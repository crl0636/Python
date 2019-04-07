class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res  = []
        if n == 0:
            return res
        self.helper(n, n , '', res)

        return res

    def helper(self, left, right, val, res):
        if left > right:
            return

        if left == 0 and right == 0:
            res.append(val)
            return

        if left > 0:
            self.helper(left -1, right, val + '(', res)
        if right > 0:
            self.helper(left, right - 1, val + ')', res)


if __name__ == "__main__":
    assert (Solution().generateParenthesis(3)) == ['((()))', '(()())', '(())()', '()(())', '()()()']