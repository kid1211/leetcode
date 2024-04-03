class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        n = len(word)
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(x, y, idx):
            nonlocal visited
            if idx == n - 1:
                return True
            
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == word[idx + 1] and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if dfs(nx, ny, idx + 1):
                        return True
                    visited.remove((nx, ny))
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 0):
                        return True
                    visited.remove((i, j))
        return False