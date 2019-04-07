class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = sorted(list(set(candidates)))
        self.helper(res, [], candidates, target, 0)
        return res

    def helper(self, res, list_, candidates, target, pos):
        if target == 0:
            return res.append(list(list_))

        for i in range(pos, len(candidates)):
            if target < 0:
                return
            list_.append(candidates[i])
            self.helper(res, list_, candidates, target - candidates[i], i)
            list_.pop()

if __name__ == '__main__':
    so = Solution()
    print so.combinationSum([2,3,6,7],7)