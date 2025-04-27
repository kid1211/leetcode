class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        res = 0
        while queue:
            res += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        fresh -= 1

                        if fresh == 0:
                            return res

                        grid[nx][ny] = 2
                        queue.append((nx, ny))
        return -1 if fresh > 0 else 0
