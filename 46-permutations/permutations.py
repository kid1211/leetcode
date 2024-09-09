class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def dfs(curr):
            nonlocal res
            if len(curr) == len(nums):
                res += [curr]
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                dfs(curr + [nums[i]])
                visited.remove(i)
        dfs([])
        return res