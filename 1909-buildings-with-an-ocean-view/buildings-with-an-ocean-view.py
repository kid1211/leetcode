class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            if not stack or heights[stack[-1]] < heights[i]:
                stack += [i]
        stack.reverse()
        return stack