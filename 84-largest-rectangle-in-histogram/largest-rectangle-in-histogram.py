class Solution:
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