class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        uniqueC = defaultdict(int)

        balls = {}
        res = []
        for x, y in queries:
            ori = balls[x] if x in balls else -1
            balls[x] = y

            if ori != -1:
                uniqueC[ori] -= 1
                if uniqueC[ori] == 0:
                    del uniqueC[ori]
            uniqueC[y] += 1
            res += [len(uniqueC)]
        return res