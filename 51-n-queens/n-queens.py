class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        col_set = set()
        plus_set = set()
        minus_set = set()

        def dfs(row, curr):
            nonlocal res
            if len(curr) == n:
                res += [curr]
                return
            
            for col in range(n):
                if col in col_set:
                    continue
                
                if row + col in plus_set:
                    continue
                
                if row - col in minus_set:
                    continue
                
                col_set.add(col)
                plus_set.add(row + col)
                minus_set.add(row - col)

                dfs(row + 1, curr + [col])

                col_set.remove(col)
                plus_set.remove(row + col)
                minus_set.remove(row - col)
                pass
        
        dfs(0, [])
        
        # draw board
        converted = []
        for ans in res:
            sol = []
            for pos in ans:
                tmp = ["." for _ in range(n)]
                tmp[pos] = "Q"
                sol += ["".join(tmp)]
                # sol += 
            converted += [sol]


        return converted
    

# draw board
    # col number to => ["..Q.",".Q.." ] 
    # [2, 1, 3, 0] For example

# how to generate that?
#  go thorugh each column at a time
# make sure no vertical or diagonal (x + y, and x-y), no need for horizontal, because one at a time
# put it in, continue, then pop it out and continue
# no need for memo, so use index, and curr