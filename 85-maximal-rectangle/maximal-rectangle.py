class Solution:

    # Get the maximum area in a histogram given its heights
    def leetcode84(self, heights):
        stack = [-1]

        maxarea = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxarea
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights += [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                res = max(res, height * (i - left - 1))
            stack += [i]
        return res
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0 for _ in range(cols)]
        res = 0
        for x in range(rows):
            for y in range(cols):
                # only intrested in last row
                dp[y] = dp[y] + 1 if matrix[x][y] == "1" else 0
            res = max(res, self.largestRectangleArea(dp))
        
        # print(dp)
        return res

[
    [1, 0, 1, 0, 0], 
    [1, 0, 1, 1, 1], 
    [1, 1, 1, 1, 1], 
    [1, 0, 0, 1, 0]
]