class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        tmp = []
        for i in range(1, n + 1):
            tmp.append(str(i))

        tmp.sort()
        return [int(i) for i in tmp ]