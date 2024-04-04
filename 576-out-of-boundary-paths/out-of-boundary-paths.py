class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 10 ** 9 + 7
        @cache
        def dfs(x, y, remainMove):
            # print('in', x, y, remainMove)
            if remainMove == 0:
                return 0 if 0 <= x < m and 0 <= y < n else 1
            
            res = 0
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    res += dfs(nx, ny, remainMove - 1) % M
                else:
                    res += 1
            return res % M

        return dfs(startRow, startColumn, maxMove)
# in 0 1 3
# in 0 2 2
# in 0 1 1
# in 0 2 0
# out 0 2 0 0
# in 0 0 0
# out 0 0 0 0
# out 0 1 1 2
# out 0 2 2 5
# in 0 0 2
# out 0 0 2 3
# out 0 1 3 10