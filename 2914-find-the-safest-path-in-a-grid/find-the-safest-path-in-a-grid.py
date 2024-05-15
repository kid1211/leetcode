from heapq import heappush, heappop
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        thief = []
        rows, cols = len(grid), len(grid[0])
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    # edge case
                    if (x, y) == (0, 0) or (x, y) == (rows - 1, cols - 1):
                        return 0

                    thief.append((x, y))
                    grid[x][y] = 0
                else:
                    grid[x][y] = -1

        queue = deque(thief)
        # step = -1
        while queue:
            # step += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                # grid[x][y] = step
                for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == -1:
                        queue.append((nx, ny))
                        grid[nx][ny] = grid[x][y] + 1

        heap = [(-grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        # visited = [[0 for _ in range(cols)] for _ in range(rows)]
        while heap:
            cumulated, x, y = heappop(heap)
            actualCumulate = -cumulated

            if (x, y) == (rows - 1, cols - 1):
                return actualCumulate

            # visited[x][y] = actualCumulate


            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    val = min(actualCumulate, grid[nx][ny])

                    # if val <= visited[nx][ny]:
                    #     continue
                    heappush(heap, (-val, nx, ny))
                    visited.add((nx, ny))
        return 0


# class Solution:
#     def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
#         n = len(grid)

#         multi_source_queue = deque()
#         # Mark thieves as 0 and empty cells as -1, and push thieves to the queue
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     # Push thief coordinates to the queue
#                     multi_source_queue.append((i, j))
#                     # Mark thief cell with 0
#                     grid[i][j] = 0
#                 else:
#                     # Mark empty cell with -1
#                     grid[i][j] = -1

#         # Calculate safeness factor for each cell using BFS
#         while multi_source_queue:
#             size = len(multi_source_queue)
#             while size > 0:
#                 curr = multi_source_queue.popleft()
#                 # Check neighboring cells
#                 for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                     di, dj = curr[0] + d[0], curr[1] + d[1]
#                     val = grid[curr[0]][curr[1]]
#                     # Check if the cell is valid and unvisited
#                     if 0 <= di < n and 0 <= dj < n and grid[di][dj] == -1:
#                         # Update safeness factor and push to the queue
#                         grid[di][dj] = val + 1
#                         multi_source_queue.append((di, dj))
#                 size -= 1
        
#         # Priority queue to prioritize cells with higher safeness factor
#         pq = [[-grid[0][0], 0, 0]] # [maximum_safeness_till_now, x-coordinate, y-coordinate]
#         grid[0][0] = -1 # Mark the source cell as visited

#         # BFS to find the path with maximum safeness factor
#         while pq:
#             safeness, i, j = heapq.heappop(pq)
            
#             # If reached the destination, return safeness factor
#             if i == n - 1 and j == n - 1:
#                 return -safeness
            
#             # Check neighboring cells
#             for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 di, dj = i + d[0], j + d[1]
#                 # Check if the neighboring cell is valid and unvisited
#                 if 0 <= di < n and 0 <= dj < n and grid[di][dj] != -1:
#                     heapq.heappush(pq, [-min(-safeness, grid[di][dj]), di, dj])
#                     grid[di][dj] = -1

#         return -1
