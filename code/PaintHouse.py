class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here

        if not costs:
            return 0
        m = len(costs)
        if m == 1:
            return min(costs[0][0], costs[0][1], costs[0][2])

        dp = [[0 for i in range(3)] for j in range(m)]

        for i in range(m):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

        return min(dp[m - 1][0], dp[m - 1][1], dp[m - 1][2])