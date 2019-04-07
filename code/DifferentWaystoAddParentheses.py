class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        if not input:
            return []

        if input.isdigit():
            return [int(input)]

        dict = {'+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y}

        res = []
        for i in range(len(input)):
            if input[i] in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        res.append(dict[input[i]](l, r))

        return res

if __name__ ==  '__main__':
    so = Solution()
    print so.diffWaysToCompute('2-1-1')