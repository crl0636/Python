class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices or len(prices) == 1:
            return 0

        hold = [0] * len(prices)
        un_hold = [0] * len(prices)
        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            if i == 1:
                hold[i] = max(hold[i-1], -prices[1])
            else:
                hold[i] = max(hold[i-1], un_hold[i-2] - prices[i])

            un_hold[i] = max(un_hold[i-1], hold[i-1] + prices[i])
        return un_hold[len(prices)-1]