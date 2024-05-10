from heapq import heappush, heappop
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []

        for i in range(len(arr)):
            heappush(heap, (
                arr[i] / arr[-1], i, len(arr) - 1
            ))
        
        # Iteratively remove the top element (smallest fraction) 
        # and replace it with the next smallest fraction
        for _ in range(k - 1):
            # 0 <= i < j < arr.length
            _, top, down = heappop(heap)
            down -= 1 # add all the top
            if down > top:
                heappush(heap, (
                    arr[top] / arr[down], top, down
                ))
    
        res = heappop(heap)
        return [arr[res[1]], arr[res[2]]]
        
