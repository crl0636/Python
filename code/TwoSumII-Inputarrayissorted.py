class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}

        for i in range(len(numbers)):
            if numbers[i] in dict:
                return [dict[numbers[i]] + 1, i + 1]
            else:
                dict[target - numbers[i]] = i

if __name__ == '__main__':
    obj  = Solution()
    obj.twoSum([2,7,11,15], 9)