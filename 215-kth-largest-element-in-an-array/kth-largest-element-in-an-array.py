from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # smallest to contain large
        heap = []

        for num in nums:
            heappush(heap, num)

            if len(heap) > k:
                heappop(heap)
        
        return heap[0]