class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = defaultdict(int)

        for i in range(n):
            rows[tuple(grid[i])] += 1
        res = 0
        for i in range(n):
            col = tuple([ grid[j][i] for j in range(n)])
            if col in rows:
                res += rows[col]
        return res