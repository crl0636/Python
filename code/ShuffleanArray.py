import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums[:]

        self.nums = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        tmp = self.nums[:]
        for i in range(len(self.nums)):
            j = random.randint(0, len(tmp) - 1)
            self.nums[i] = tmp[j]
            del tmp[j]

        return self.nums
