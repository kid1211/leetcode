class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        def getPerimeter(x, y):
            res = 0
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    continue
                res += 1
            return res
        
        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    res += getPerimeter(x, y)
        return res