class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        rows, cols = len(matrix), len(matrix[0])
        hasZeroOnFirstRow = hasZeroOnFirstCol = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        hasZeroOnFirstRow = True
                    if j == 0:
                        hasZeroOnFirstCol = True

        for i in range(1, rows):
            if matrix[i][0] != 0:
                continue
            
            for j in range(cols):
                matrix[i][j] = 0

        for j in range(1, cols):
            if matrix[0][j] != 0:
                continue
            
            for i in range(rows):
                matrix[i][j] = 0

        # print(hasZeroOnFirstRow, hasZeroOnFirstCol)
        if hasZeroOnFirstRow:
            for i in range(cols):
                matrix[0][i] = 0
        if hasZeroOnFirstCol:
            for i in range(rows):
                matrix[i][0] = 0
