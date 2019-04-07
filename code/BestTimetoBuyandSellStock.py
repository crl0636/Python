class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices or len(prices) == 0:
            return 0

        min_value = prices[0]
        profit = 0

        for price in prices:
            if price < min_value:
                min_value = price

            profit = max(profit, price - min_value)

        return profit