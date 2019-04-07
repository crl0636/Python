class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here

        if len(nums) < 3:
            return 0

        ans = 0
        nums.sort()
        for i in range(len(nums) - 2):

            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < target:
                    ans += r - l
                    l += 1
                else:
                    r -= 1

        return ans

if __name__ == '__main__':
    so = Solution()
    print so.threeSumSmaller([1,-2,2,1,0], 1)