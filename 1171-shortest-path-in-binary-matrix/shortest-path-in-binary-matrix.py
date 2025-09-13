class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0:
            return -1

        queue = deque([(0,0)])
        grid[0][0] = 1
        n = len(grid)
        res = 0
        
        while queue:
            res += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                if x == y == n - 1:
                    return res


                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        queue.append((nx, ny))
                        grid[nx][ny] = 1
        
        return -1
