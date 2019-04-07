class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        if not findNums or not nums:
            return None

        res = []

        for find_num in findNums:
            pos = nums.index(find_num)
            found = False
            for i in range(pos + 1, len(nums)):
                if nums[i] >= find_num:
                    res.append(nums[i])
                    found = True
                    break
            if not found:
                res.append(-1)

        return res

if __name__ == '__main__':
    so  = Solution()
    print so.nextGreaterElement([4,1,2], [1,3,4,2])