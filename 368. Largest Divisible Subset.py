class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        @cache
        def dfs(last):
            if last >= len(nums):
                return []
            res = []
            for i in range(last):
                if nums[last] % nums[i] == 0:
                    res = max(res, dfs(i), key=len)
            return [nums[last]] + res
        
        return max([
            dfs(i) for i in range(len(nums))
        ], key=len)
