class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        stack = [(-1, 0)]
        max_len = 0
        for item in input.split('\n'):
            level = item.count('\t')
            item = item.replace('\t', '')

            while stack and level <= stack[-1][0]:
               stack.pop()

            if '.' in item:
                stack.append([level, len(item) + stack[-1][1]] + 1)
            else:
                max_len = max(max_len, len(item) + stack[-1][1])
        return max_len