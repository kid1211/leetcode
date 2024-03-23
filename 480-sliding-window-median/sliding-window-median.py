from sortedcontainers import SortedList
from operator import neg
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxheap, minheap = SortedList(), SortedList(key=lambda item: (-item[0], item[1]))
        
        def add(idx):
            nonlocal maxheap, minheap
            val = (nums[idx], idx)

            if len(minheap) < len(maxheap):
                minheap += [val]
            else:
                maxheap += [val]
            
            if minheap and minheap[-1] < maxheap[-1]:
                maxheap += [minheap.pop()]
                minheap += [maxheap.pop()]
        
        def remove(idx):
            nonlocal maxheap, minheap
            val = (nums[idx], idx)
            minheap.discard(val)
            maxheap.discard(val)

            if len(maxheap) < len(minheap):
                maxheap += [minheap.pop()]
        
        for i in range(k - 1):
            add(i)
        
        res = []
        for i in range(k - 1, len(nums)):
            add(i)
            res += [
                maxheap[-1][0] if k % 2 == 1 else
                (maxheap[-1][0] + minheap[-1][0]) / 2
            ]
            remove(i - k + 1)
        return res
