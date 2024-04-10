from heapq import heappush, heappop
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        minStack, maxStack = [], []
        # Size of min stack > maxStack
        # so taht we always take the minstack
        # [3] [3]
        # [2] [3]
        def add(num):
            if len(minStack) > len(maxStack):
                heappush(maxStack, -num)
            else:
                heappush(minStack, num)
            
            if maxStack and -maxStack[0] > minStack[0]:
                heappush(minStack, -heappop(maxStack))
                heappush(maxStack, -heappop(minStack))

        for num in nums:
            add(num)
    
        res = 0
        while minStack[0] != k:
            delta = abs(k - minStack[0])
            if minStack[0] > k:
                prev = heappop(minStack)
                add(prev - delta)
            else:
                prev = heappop(minStack)
                add(prev + delta)
            res += delta
        return res
