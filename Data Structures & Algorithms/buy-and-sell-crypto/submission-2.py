class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        best_buy = prices[0]
        best_profit = 0

        for p in prices:
            best_profit = max(best_profit, p - best_buy)
            best_buy = min(best_buy, p)

        return best_profit



