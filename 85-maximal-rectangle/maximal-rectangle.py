class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        def helper(nums):
            nums += [0]
            stack = []
            res = 0
            for i in range(len(nums)):
                while stack and nums[stack[-1]] > nums[i]:
                    height = nums[stack.pop()]
                    left = stack[-1] if stack else -1
                    res = max(res, height * (i - left - 1))
                stack += [i]
            return res


        
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * cols
        res = 0
        for x in range(rows):
            for y in range(cols):
                dp[y] = dp[y] + 1 if matrix[x][y] == "1" else 0
            res = max(res, helper(dp))
        return res