class Solution:    
    def kInversePairs(self, n: int, k: int) -> int:
        M = 10**9 + 7

        @cache
        def dfs(n, k):
            if n == 0 or k < 0:
                return 0
            if k == 0:
                return 1
            
            val = dfs(n - 1, k)
            val += dfs(n, k - 1) - dfs(n - 1, k - n) 
            return val % M
        
        res = dfs(n, k)
        if k > 0:
            res -= dfs(n, k - 1)
        return res % M
        

        # dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        # M = 10**9 + 7
        # for i in range(1, n + 1):
        #     for j in range(k + 1):
        #         if j == 0:
        #             dp[i][j] = 1
        #         else:
        #             # dp[i - 1][j - 0]
        #             # 123 + 4 i = 4 往前挪3为
        #             # 4123 => k=> 3
        #             # dp[i - 1][j - (i - 1)]
        #             # dp[i - 1][0]
        #             # for p in range(min(j, i - 1) + 1):
        #             #     dp[i][j] += dp[i - 1][j - p]
        #             #     dp[i][j] %= 10**9 + 7
        #             val = dp[i - 1][j]
        #             if j >= i:
        #                 val -= dp[i - 1][j - i]
        #             dp[i][j] = dp[i][j - 1] + val
        #             dp[i][j] %= M
        
        # print(dp)
        # res = dp[n][k]
        # if k > 0:
        #     res -= dp[n][k - 1]
        # return res % M
# k inverse pairs and n elements
# k = 4 + (4 - 4)
# k = 3 + (4 - 3)
# k = 2 + (4 - 2)
# k = 1 + (4 - 1)
# k = 0 + (4 - 0)
# k = lastK + (j - lastK)

# [
#     [0, 0,  0,  0,  0,  0], 
#     [1, 1,  1,  1,  1,  1], 
#     [1, 2,  2,  2,  2,  2], 
#     [1, 3,  5,  6,  6,  6], 
#     [1, 4,  9, 15, 20, 23], 
#     [1, 5, 14, 29, 49, 71]
# ]
# 5 - 0
# 5 - 1
# 5 - 2
# 5 - 3 = 2, 3 = 4 - 1
# [#k. 0. 1.  2.  3.  4.  5
#     [0, 0,  0,  0,  0,  0], #n = 0
#     [1, 0,  0,  0,  0,  0], #n = 1
#     [1, 1,  0,  0,  0,  0], #n = 2
#     [1, 2,  2,  1,  0,  0], #n = 3
#     [1, 3,  5,  6,  5,  3], #n = 4
#     [1, 4,  9, 15, 20, 22]  #n = 5
# ]
# i = 5
# k = 5, no k = 0 de case
# 1234 + 5
# 51234 => 4 != 5
# 51243
# 5xxxx => 1 => 5

