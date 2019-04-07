class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        self.helper(res, [], n, k, 1)
        return res

    def helper(self, res, list_, n, k, pos):
        if k < 0:
            return
        elif k == 0:
            return res.append(list(list_))
        else:
            for i in range(pos, n + 1):
                list_.append(i)
                self.helper(res, list_, n, k - 1, i + 1)
                list_.pop()

if __name__ == '__main__':
    so  = Solution()
    print so.combine(4, 3)