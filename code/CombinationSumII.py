class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.helper(res, [], candidates, target, 0)
        return res

    def helper(self, res, list_, candidates, target, pos):
        if target < 0:
            return
        elif target == 0:
            if list_ not in res:
                return res.append(list(list_))
        else:
            for i in range(pos, len(candidates)):
                list_.append(candidates[i])
                self.helper(res, list_, candidates, target - candidates[i], i + 1)
                list_.pop()

if __name__ == '__main__':
    so = Solution()
    print so.combinationSum2([2,5,2,1,2], 5)