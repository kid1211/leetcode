class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        @cache
        def dfs(startIdx, remain):
            if startIdx >= len(candidates):
                return []
            
            res = []
            for i in range(startIdx, len(candidates)):
                num = candidates[i]
                if remain - num < 0:
                    break
                if remain - num == 0:
                    res += [[num]]
                    break
                for tmp in dfs(i, remain - num):
                    res += [
                        [num] + tmp
                    ]
            return res
        candidates.sort()
        return dfs(0, target)