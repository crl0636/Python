"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0

        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        i = j = ans = 0
        while i < len(intervals):
            if start[i] > end[j]:
                j += 1
            elif start[i] < end[j]:
                i += 1
            else:
                i += 1
                j += 1
            ans  = max(ans, i - j)
        return ans

if __name__ == '__main__':
    so = Solution()
    obj1 = Interval(0, 30)
    obj2 = Interval(5, 10)
    obj3 = Interval(15, 20)
    print so.minMeetingRooms([obj1, obj2, obj3])