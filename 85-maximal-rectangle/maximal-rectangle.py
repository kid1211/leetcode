class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def helper(nums):
            nonlocal res
            nums += [0]
            stack = []
            for i in range(len(nums)):
                while stack and nums[stack[-1]] > nums[i]:
                    height = nums[stack.pop()]
                    left = stack[-1] if stack else -1
                    res = max(res, height * (i - left - 1))
                stack += [i]
        
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        dp = [0] * cols
        for x in range(rows):
            for y in range(cols):
                dp[y] = dp[y] + 1 if matrix[x][y] == "1" else 0
            helper(dp)
        return res