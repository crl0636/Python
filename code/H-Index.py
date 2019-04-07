class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if not citations:
            return 0

        citations.sort()
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0

if __name__ == '__main__':
    so = Solution()
    print so.hIndex([3,0,6,1,5])