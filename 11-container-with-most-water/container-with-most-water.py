class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left max, right maxArea
        l, r = 0, len(height) - 1
        res = 0
    
        while l < r:
            # res = max(res, )
            if height[l] < height[r]:
                res = max(res, height[l] * (r - l))
                l += 1
            else:
                res = max(res, height[r] * (r - l))
                r -= 1
        return res

# 1,8,6,2,5,4,8,3,7]
# L               R 
#   L             R