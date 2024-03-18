class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @cache
        def dfs(startIdx):
            maxi = res = 0
            for i in range(k):
                if i + startIdx >= n:
                    break
                maxi = max(maxi, arr[i + startIdx])
                res = max(res, maxi * (i + 1) + dfs(i + startIdx + 1))
            return res
        
        return dfs(0)
