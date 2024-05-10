from heapq import heappop, heappush, heapify
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = [ -item for item in happiness]
        heapify(heap)
        res = 0
        for i in range(k):
            val = heappop(heap)
            res += max(-val - i, 0)
        return res
