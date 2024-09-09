class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def dfs(curr):
            nonlocal res
            if len(curr) == len(nums):
                res += [list(curr)]
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue

                visited.add(i)
                curr += [nums[i]]

                dfs(curr)
                
                curr.pop()
                visited.remove(i)
        dfs([])
        return res