class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != sort[i]:
                res += 1
        return res