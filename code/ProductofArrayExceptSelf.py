class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return 0

        prod = 1
        zero = 0
        for i in nums:
            if i != 0:
                prod = prod * i
            else:
                zero += 1

        if zero > 1:
            return [0] * len(nums)

        res = []
        for i in nums:
            if zero == 1:
                if i != 0:
                    res.append(0)
                else:
                    res.append(prod)
            elif i != 0:
                res.append(prod / i)
            else:
                res.append(0)

        return res

if __name__ == '__main__':
    so = Solution()
    print so.productExceptSelf([1,0])