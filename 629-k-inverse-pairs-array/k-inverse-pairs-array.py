class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        M = 10**9 + 7
        @cache
        def dfs(n, k):
            if k < 0 or n == 0:
                return 0
            if k == 0:
                return 1
            
            return (
                dfs(n, k - 1) +
                dfs(n - 1, k) - dfs(n - 1, k - n)
            ) % M
        
        return (dfs(n, k) - dfs(n, k - 1)) % M