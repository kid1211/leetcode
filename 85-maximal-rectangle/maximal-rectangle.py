class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        res = 0
        for x in range(rows):
            for y in range(cols):
                if matrix[x][y] == "0":
                    continue
                
                width = dp[x][y] = dp[x][y - 1] + 1 if y else 1

                for height in range(x, -1, -1):
                    width = min(width, dp[height][y])
                    res = max(res, width * (x - height + 1))
        
        # print(dp)
        return res

[
    [1, 0, 1, 0, 0], 
    [1, 0, 1, 1, 1], 
    [1, 1, 1, 1, 1], 
    [1, 0, 0, 1, 0]
]