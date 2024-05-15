class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y):
            res = 0
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    res = max(res, grid[nx][ny] + dfs(nx, ny))
                    visited.remove((nx, ny))
            return res

        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    continue
                visited.add((x, y))
                res = max(res, dfs(x, y) + grid[x][y])
                visited.remove((x, y))
        return res