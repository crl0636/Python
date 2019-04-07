# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        if not newInterval:
            return intervals

        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals):
        """
            :type intervals: List[Interval]
            :rtype: List[Interval]
        """
        res = []

        if not intervals:
            return res

        intervals.sort(key=lambda x: x.start)

        res.append(intervals[0])

        for interval in intervals[1:]:
            pre = res[-1]
            if pre.end < interval.start:
                res.append(interval)
            elif pre.end >= interval.start:
                pre.end = max(pre.end, interval.end)

        return res

if __name__ == '__main__':
    so = Solution()
    print so.insert([[1,3],[6,9]], [2,5])