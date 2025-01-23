class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    rows[i].add((i, j))
                    cols[j].add((i, j))

        res = set()
        for key in rows:
            if len(rows[key]) <= 1:
                continue
            for item in rows[key]:
                res.add(item)

        for key in cols:
            if len(cols[key]) <= 1:
                continue
            for item in cols[key]:
                res.add(item)
        return len(res)
