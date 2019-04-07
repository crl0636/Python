import collections
class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here

        ans = []
        for i in xrange(len(nums)):
            for j in xrange(i, len(nums)):
                cur = nums[i:j+1]
                if sum(cur) == k:
                    ans.append(cur)
        if not ans:
            return 0

        return max([len(_) for _ in ans])

if __name__ == '__main__':
    so = Solution()
    print so.maxSubArrayLen([-2, -1, 2, 1], 1)