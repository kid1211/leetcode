class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])

        def getLargest(x, y):
            maxi = -sys.maxsize
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    # if 0 <= i < rows and 0 <= j < cols:
                    maxi = max(maxi, grid[i][j])
            return maxi
        res = []
        for x in range(1, rows - 1):
            tmp = []
            for y in range(1, cols - 1):
                tmp += [getLargest(x, y)]
            res += [tmp]
        return res