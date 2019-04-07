import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        result = ["JFK"]

        dic = collections.defaultdict(list)  # defaultdict never raise KeyError
        for flight in tickets:
            dic[flight[0]] += flight[1],

        self.dfs_helper(dic, "JFK", result, len(tickets))

        return result

    def dfs_helper(self, dic, departure, result, flights):
        if len(result) == flights + 1:
            return result

        currentDst = sorted(dic[departure])
        for dst in currentDst:
            dic[departure].remove(dst)
            result.append(dst)

            valid = self.dfs_helper(dic, dst, result, flights)
            if valid:
                return valid

            result.pop()
            dic[departure].append(dst)


if __name__ == '__main__':
    so = Solution()
    print so.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
