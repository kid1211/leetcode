class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(x, y):
            
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    dfs(nx, ny)
        
        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    grid[x][y] == "0"
                    dfs(x, y)
                    res += 1
        return res