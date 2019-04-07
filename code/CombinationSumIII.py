class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans =[]
        self.helper(ans, [], n, k, 1)
        return ans

    def helper(self, res, list_, n, k, pos):
        if len(list_) > k:
            return
        if len(list_) == k and sum(list_) == n:
            if sorted(list_) not in res:
                res.append(list(list_))
                return

        for i in range(pos, 10):
            if i not in list_:
                list_.append(i)
                self.helper(res, list_, n, k, pos + 1)
                list_.pop()

if __name__ == '__main__':
    so = Solution()
    print so.combinationSum3(3, 7)
