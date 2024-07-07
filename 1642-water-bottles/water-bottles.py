class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = empty = 0

        while numBottles > 0:
            # print(res, numBottles, empty)
            res += numBottles
            empty += numBottles
            exchanged = empty // numExchange
            empty -= exchanged * numExchange
            numBottles = exchanged
        return res
# 0 15 4
# 15 3 4
# 18 1 4