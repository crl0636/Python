class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for item in findNums:
            pos = nums.index(item)
            tag = 0
            for x in nums[pos:]:
                if x > item:
                    result.append(x)
                    tag = 1
                    break
            if tag == 0:
                result.append(-1)
        return result

if __name__=='__main__':
    solution = Solution()
    findnNum=[4,1,2]
    nums = [1,3,4,2]
    solution.nextGreaterElement(findnNum, nums)