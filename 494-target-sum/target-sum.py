class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.cache
        def dfs(currIdx, currSum):
            if currIdx == len(nums):
                return 1 if currSum == target else 0
    
            res = 0
            res += dfs(currIdx + 1, currSum + nums[currIdx])
            res += dfs(currIdx + 1, currSum - nums[currIdx])
            return res

        return dfs(0, 0)