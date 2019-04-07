# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        if len(intervals) == 0:
            return 0

        count = 0
        j = 0

        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
            if intervals[j].end > intervals[i].start:
                count += 1
                j = i if intervals[i].end < intervals[j].start else j
            else:
                j = i

        return count


if __name__ == '__main__':
    so = Solution()
    so.eraseOverlapIntervals([[1,2],[2,3]])