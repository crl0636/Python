# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n
        while start <= end:
            mid = (end + start) / 2
            if not isBadVersion(mid):
                start = mid + 1
            elif isBadVersion(mid):
                if isBadVersion(mid - 1):
                    end = mid - 1
                else:
                    return mid
