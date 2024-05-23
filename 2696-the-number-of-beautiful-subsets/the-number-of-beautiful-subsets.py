class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = []

        def isValid(curr, match):
            for num in curr:
                if abs(num - match) == k:
                    return False
            return True

        def dfs(startIdx, curr):
            nonlocal res
            if curr:
                res += [curr]
            if startIdx >= len(nums):
                return

            for i in range(startIdx, len(nums)):
                if isValid(curr, nums[i]):
                    dfs(i + 1, curr + [nums[i]])

        dfs(0, [])
        return len(res)
