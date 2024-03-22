class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maxVal = max(counter.keys())

        @cache
        # counter nah
        def dfs(maxVal):
            if maxVal == 0:
                return 0
            
            if maxVal == 1:
                return counter[1]
            
            return max(
                dfs(maxVal - 1),
                counter[maxVal] * maxVal + dfs(maxVal - 2)
            )
        
        return dfs(maxVal)