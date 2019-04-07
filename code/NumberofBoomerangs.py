import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0

        dict = collections.Counter()

        for i in xrange(len(points)):
            dict.clear()
            for j in xrange(len(points)):
                if i == j:
                    continue

                distance = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + \
                            (points[i][1] - points[j][1]) * (points[i][1] - points[j][1])

                dict[distance] += 1
            for distance in dict:
                res += dict[distance] * (dict[distance] - 1)

        return res