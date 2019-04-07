class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (len(nums) == 0):
            return 0
        elif (len(nums) == 1):
            return nums[0]
        else:
            profit = [0] * (len(nums) + 2)
            for i in range(len(nums)):
                current_profit = 0
                current_profit = nums[i]
                for j in range(i + 2, len(nums), 2):
                    current_profit += nums[j]
                profit.append(current_profit)
        return max(profit)

if __name__ ==  '__main__':
    solution = Solution()
    solution.rob([2,7,9,3,1])