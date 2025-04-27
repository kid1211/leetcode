class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance[0], entrance[1])])
        rows, cols = len(maze), len(maze[0])
        res = 0

        def isStart(x, y):
            return x == entrance[0] and y == entrance[1]
        
        visited = set([(entrance[0], entrance[1])])

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                if (x == 0 or x == rows - 1 or y == 0 or y == cols - 1) and res > 0:
                    return res

                for (dx, dy) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == "." and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            res += 1
        return -1
