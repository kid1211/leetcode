from heapq import heappush, heappop, heapify
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted([ (nums1[i], nums2[i]) for i in range(len(nums2))], key= lambda item: -item[1])
        minheap = [item[0] for item in pairs[:k]]
        curr = sum(minheap)
        heapify(minheap)
        res = curr * pairs[k-1][1]
        # print(res)
        for i in range(k, len(nums1)):
            heappush(minheap, pairs[i][0])
            curr += pairs[i][0]
            curr -= heappop(minheap)
            res = max(res, curr * pairs[i][1])
            # print(res, curr * pairs[i][1])

        return res

        