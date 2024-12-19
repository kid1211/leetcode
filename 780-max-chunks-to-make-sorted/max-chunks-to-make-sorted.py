class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxi = -1
        res = 0
        for i in range(len(arr)):
            maxi = max(maxi, arr[i])
            if maxi <= i:
                res += 1
        return res