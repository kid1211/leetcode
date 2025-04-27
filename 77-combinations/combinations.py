class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [ i for i in range(1, n + 1) ]

        res = []
        def dfs(curr, index):
            nonlocal res
            if len(curr) == k:
                res += [curr]
                return
            
            for i in range(index, n + 1):
                dfs(curr + [i], i + 1)

        dfs([], 1)
        return res