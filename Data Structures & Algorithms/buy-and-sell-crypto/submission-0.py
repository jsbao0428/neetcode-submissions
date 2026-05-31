class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy

        max_profit = 0

        min_price = prices[0]
        n = len(prices)
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_price)

            min_price = min(prices[i], min_price)



        return max_profit