class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        
        count = 1

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[count] = nums[i]
                count = count + 1
        return count

if __name__ == '__main__':
    obj = Solution()
    print obj.removeDuplicates([1,2])