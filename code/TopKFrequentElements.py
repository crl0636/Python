import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = collections.defaultdict(int)

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        ans = set()
        values = sorted(dict.values())[::-1]
        for i in range(k):
            for key, val in dict.iteritems():
                if val == values[i]:
                    ans.add(key)

        return ans
if __name__ == '__main__':
    so = Solution()
    so.topKFrequent([4,1,-1,2,-1,2,3], 2)