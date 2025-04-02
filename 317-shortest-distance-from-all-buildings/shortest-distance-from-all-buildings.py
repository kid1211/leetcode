class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        weights = [[0 for _ in range(cols) ] for _ in range(rows)]

        def bfs(start, houseIdx):
            queue = deque([start])
            res = sys.maxsize
            step = -1

            while queue:
                step += 1
                for _ in range(len(queue)):
                    x, y = queue.popleft()

                    if step > 0:
                        weights[x][y] += step
                        res = min(res, weights[x][y])
                        
                    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                        nx, ny = x + dx, y + dy
                        
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == -houseIdx:
                            grid[nx][ny] -= 1
                            queue.append((nx, ny))
            return res if res != sys.maxsize else -1

        houseIdx = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    res = bfs((x, y), houseIdx)
                    houseIdx += 1
        return res