class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        scoreAndIdx = [(score[i], i) for i in range(n)]
        res = [-1 for _ in range(n)]
        i = 0
        for _, idx in sorted(scoreAndIdx, reverse=True):
            if i == 0:
                res[idx] = "Gold Medal"
            elif i == 1:
                res[idx] = "Silver Medal"
            elif i == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(i + 1)
            i += 1
        return res
