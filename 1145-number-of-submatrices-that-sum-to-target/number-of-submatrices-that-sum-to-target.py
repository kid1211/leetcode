class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # right, down, down_right
        rows, cols = len(matrix), len(matrix[0])
        prefix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix[i][j] = (
                    prefix[i][j - 1] + 
                    prefix[i - 1][j] - 
                    prefix[i - 1][j - 1] + 
                    matrix[i - 1][j - 1]
                    )
        # print(prefix)
        res = 0
        for r1 in range(1, rows + 1):
            for r2 in range(r1, rows + 1):
                h = defaultdict(int)
                h[0] = 1 

                for col in range(1, cols + 1):
                    curr_sum = prefix[r2][col] - prefix[r1 - 1][col]
                    res += h[curr_sum - target]
                    h[curr_sum] += 1
                                        
        return res
# [ 
#     [0, 1, 1],
#     [1, 3, 4],
#     [1, 4, 5]]
# [
#     [0, 0, 0, 0], 
#     [0, 0, 1, 1], 
#     [0, 1, 3, 4], 
#     [0, 1, 4, 5]
# ]
# end: (2, 2) start: (0, 2) newWin: 0 up_left: 1 up: 1 left: 5

# 0 0 2 2
# 5 - 

# 0 0 1 1
# 0 0 1 2
# 0 1 1 2
# 0 0 2 1
# 1 0 2 1
# 0 0 2 2
# 0 1 2 2
# 1 0 2 2
# 1 1 2 2