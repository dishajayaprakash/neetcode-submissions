class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            # If the price at r is higher than at l, we can make a profit 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            # If today's price is cheaper than your current buying price, the old buying price can never be optimal anymore
            else: 
                l = r
            r += 1
        return max_profit
        