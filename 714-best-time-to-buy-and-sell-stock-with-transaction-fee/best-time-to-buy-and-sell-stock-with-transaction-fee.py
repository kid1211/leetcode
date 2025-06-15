class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dfs(day, isHolding):
            if day == len(prices):
                return 0

            doNothing = dfs(day + 1, isHolding)
            if isHolding:
                return max(
                    doNothing,
                    dfs(day + 1, not isHolding) + prices[day] - fee,
                )
            else:
                return max(
                    doNothing,
                    dfs(day + 1, not isHolding) - prices[day]
                )
        
        return dfs(0, False)