class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(cols):
                    grid[i][j] = 1 - grid[i][j]
        
        for j in range(1, cols):
            number = 0
            for i in range(rows):
                number += 1 if grid[i][j] == 1 else -1
            
            if number < 0:
                for i in range(rows):
                    grid[i][j] = 1 - grid[i][j]

        
        res = 0
        for i in range(rows):
            res += int("".join(
                [str(digit) for digit in grid[i]]
            ), 2)

        return res

# 0011
# 0101
# 0011

# 1011
# 1101
# 1011

# 1111
# 1001
# 1111