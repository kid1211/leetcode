class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        
        for x in range(1, rows):
            for y in range(cols):
                if land[x][y] == 1:
                    land[x][y] = land[x - 1][y] + 1
        
        res = []
        for x in range(rows):
            width = 0
            for y in range(cols):
                if land[x][y] == 0:
                    width = 0
                    continue
                down = land[x + 1][y] == 0 if x + 1 < rows else True
                right = land[x][y + 1] == 0 if y + 1 < cols else True
                width += 1
                if down and right:
                    res += [[
                        x - land[x][y] + 1, y - width + 1, x, y
                    ]]
        
        # print(land)
        return res
[
    [1,1,0,0,0,1],
    [1,1,0,0,0,0]]