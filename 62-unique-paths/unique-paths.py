class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n) ] for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                print((row, col), dp[row - 1][col], dp[row][col - 1])
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]

