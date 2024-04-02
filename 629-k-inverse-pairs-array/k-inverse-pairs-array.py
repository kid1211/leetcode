class Solution:    
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        M = 10**9 + 7
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    val = dp[i - 1][j]
                    if j - i >= 0:
                        val -= dp[i - 1][j - i]
                    dp[i][j] = dp[i][j - 1] + val
                    dp[i][j] %= M
        
        res = dp[n][k]
        if k > 0:
            res -= dp[n][k - 1]
        return res % M