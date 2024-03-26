class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @cache
        def dfs(lastNum, start):
            if start >= len(nums):
                return 0
            
            # skip current
            res = 0
            for i in range(start, len(nums)):
                if nums[i] > lastNum:
                    res = max(res, dfs(nums[i], i + 1) + 1)
            
            return res

        return dfs(-sys.maxsize, 0)