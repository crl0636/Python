# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        if not intervals:
            return ans

        intervals.sort(key=lambda x: x.start)
        ans.append(intervals[0])
        for interval in intervals[1:]:
            pre = ans[-1]
            if pre.end >= interval.start:
                pre.end = max(pre.end, interval.end)
            else:
                ans.append(interval)
        return ans

if __name__ == '__main__':
    so = Solution()
    so.merge([[1,3],[2,6],[8,10],[15,18]])