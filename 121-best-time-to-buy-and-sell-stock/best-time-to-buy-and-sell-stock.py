class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = sys.maxsize
        res = 0

        for num in prices:
            mini = min(mini, num)
            res = max(res, num - mini)
        return res