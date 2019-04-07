class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        current_price = prices[0]
        current_profit = 0
        max_profit = 0

        for i in range(1, len(prices)):
            if current_price < prices[i]:
                current_profit = prices[i] - current_price

                if i < len(prices) - 1:
                    current_price = prices[i]
            else:
                current_price = prices[i]

            max_profit += current_profit
            current_profit = 0

        return max_profit