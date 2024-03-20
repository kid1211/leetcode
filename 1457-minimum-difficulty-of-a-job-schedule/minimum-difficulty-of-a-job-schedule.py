class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        remain = [0] * n
        remain[-1] = jobDifficulty[-1]
        for i in range(n - 2, -1, -1):
            remain[i] = max(jobDifficulty[i], remain[i + 1])
        
        print(remain)


        @cache
        def dfs(curr, startIdx):
            if startIdx >= n:
                return sys.maxsize
            if curr == d:
                # last day
                return remain[startIdx]

            mustLeaveRoom = d - curr
            localMax = -sys.maxsize
            res = sys.maxsize
            for i in range(startIdx, len(jobDifficulty) - mustLeaveRoom):
                localMax = max(localMax, jobDifficulty[i])
                res = min(res, localMax + dfs(curr + 1, i + 1))
            return res

        return dfs(1, 0)