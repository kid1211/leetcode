class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        xSet = set()
        ySet = set()
        xPySet = set()
        xMySet = set()

        def dfs(curr):
            nonlocal res
            if len(curr) == n:
                res += [curr]
                return

            row = len(curr)
            for col in range(n):
                if row in xSet:
                    continue
                if col in ySet:
                    continue
                if row + col in xPySet:
                    continue
                if row - col in xMySet:
                    continue

                xSet.add(row)
                ySet.add(col)
                xPySet.add(row + col)
                xMySet.add(row - col)
                dfs(curr + [col])
                xSet.remove(row)
                ySet.remove(col)
                xPySet.remove(row + col)
                xMySet.remove(row - col)

        def drawBoard(colList):
            res = []
            for col in colList:
                res += ["". join(col * '.' + 'Q' + (n - col - 1) * '.')]
            return res

        dfs([])
        print(res)

        return [
            drawBoard(colList) for colList in res
        ]