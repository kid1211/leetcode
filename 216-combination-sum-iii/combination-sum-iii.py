class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(curr, currSum, startIdx):
            nonlocal res

            if len(curr) == k:
                if currSum == n:
                    res += [curr]
                return

            for i in range(startIdx, 10):
                # if curr and i <= curr[-1]:
                #     continue
                dfs(curr + [i], currSum + i, i + 1)

        dfs([], 0, 1)
        return res

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:

#         res = []
#         def dfs(curr, index):
#             nonlocal res
#             if len(curr) == k:
#                 res += [curr]
#                 return
            
#             for i in range(index, n + 1):
#                 dfs(curr + [i], i + 1)

#         dfs([], 1)
#         return res