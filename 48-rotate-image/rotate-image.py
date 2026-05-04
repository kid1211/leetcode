class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = (
                    matrix[c][r], matrix[r][c])
        
        # 1, 4, 7
        # 2, 5, 8
        # 3, 6, 9

        # print(matrix)

        for r in range(n):
            for c in range(n//2):
                matrix[r][c], matrix[r][n - c - 1] = (
                    matrix[r][n - c - 1], matrix[r][c]
                )
        # print(matrix)


# [
#     [1, 4, 7], 
#     [4, 5, 8], [7, 8, 9]]
# [[7, 4, 7], [8, 5, 8], [9, 8, 9]]