class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """

        if buckets == 1:
            return 0

        test = minutesToTest/minutesToDie + 1
        pigs = 0
        while test ** pigs < buckets:
            pigs += 1

        return pigs