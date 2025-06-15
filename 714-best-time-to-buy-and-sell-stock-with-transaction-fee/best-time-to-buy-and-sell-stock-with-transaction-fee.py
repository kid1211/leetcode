class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = [0] * n, [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            # hold
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)

        return free[-1]

        # @cache
        # def dfs(day, isHolding):
        #     if day == len(prices):
        #         return 0

        #     doNothing = dfs(day + 1, isHolding)
        #     if isHolding:
        #         return max(
        #             doNothing,
        #             dfs(day + 1, not isHolding) + prices[day] - fee,
        #         )
        #     else:
        #         return max(
        #             doNothing,
        #             dfs(day + 1, not isHolding) - prices[day]
        #         )

        # return dfs(0, False)
