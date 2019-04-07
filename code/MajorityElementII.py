class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        ans = []
        for key, val in dict.iteritems():
            if val > len(nums)//3:
                ans.append(key)

        return ans

if __name__ == '__main__':
    so =Solution()
    print so.majorityElement([3,2,3])