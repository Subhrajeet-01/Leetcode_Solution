class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                notBuy = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, notBuy)
            else:
                sell = dfs(i + 1, not buying) + prices[i] - fee
                notSell = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, notSell)
            
            return dp[(i, buying)]
        
        return dfs(0, True)