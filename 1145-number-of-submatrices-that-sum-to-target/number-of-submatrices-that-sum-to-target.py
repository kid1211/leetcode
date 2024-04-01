class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])

        prefix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix[i][j] = (
                    prefix[i - 1][j] + 
                    prefix[i][j - 1] - 
                    prefix[i - 1][j - 1] + 
                    matrix[i - 1][j - 1])

        res = 0
        for r1 in range(1, rows + 1):
            for r2 in range(r1, rows + 1):
                h = defaultdict(int)
                h[0] = 1

                for c in range(1, cols + 1):
                    rolling = prefix[r2][c] - prefix[r1 - 1][c]
                    res += h[rolling - target]
                    h[rolling] += 1
        return res