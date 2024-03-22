class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_nums = set([ i ** 2 for i in range(1, int(n**0.5) + 1)])

        @cache
        def dfs(remain, ans):
            if ans == 1:
                return remain in sqrt_nums
            
            for num in sqrt_nums:
                if remain < num:
                    continue
    
                if dfs(remain - num, ans - 1):
                    return True
            return False
        
        for ans in range(1, n + 1):
            if dfs(n, ans):
                return ans

        return False

# class Solution:
#     def numSquares(self, n: int) -> int:
#         sqrt_nums = [ i ** 2 for i in range(1, int(n**0.5) + 1)]
        
#         @cache
#         def dfs(startIdx, remain):
#             # if startIdx >= len(sqrt_nums):
#             #     return sys.maxsize
            
#             res = sys.maxsize
#             for i in range(startIdx, len(sqrt_nums)):
#                 val = sqrt_nums[i]

#                 if remain < val:
#                     break
                
#                 if remain == val:
#                     res = 1
#                     break
                
#                 res = min(res, 1 + dfs(i, remain - val))
#             return res
        
#         return dfs(0, n)