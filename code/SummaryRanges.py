class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        ans = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] + 1 == nums[j+1]:
                j += 1
            if i != j:
                ans.append(str(nums[i]) + '->' + str(nums[j]))
            else:
                ans.append(str(nums[i]))
            i = j + 1
        return ans

if __name__ == '__main__':
    so = Solution()
    print so.summaryRanges([0,2,3,4,6,8,9])