class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        tmp = []
        for nums in A:
            tmp.append(nums[::-1])

        res = []
        for nums in tmp:
            tmp1 = []
            for num in nums:
                if num == 0:
                    tmp1.append(1)
                if num ==1:
                    tmp1.append(0)
            res.append(tmp1)
        return res