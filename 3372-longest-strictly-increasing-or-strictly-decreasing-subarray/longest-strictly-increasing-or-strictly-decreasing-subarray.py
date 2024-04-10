class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        def helper(ratio):
            res = 1
            left = 0
            for right in range(1, len(nums)):
                if nums[right] * ratio > nums[right - 1] * ratio:
                    res = max(res, right - left + 1)
                else:
                    left = right
            return res
        
        return max(helper(1), helper(-1))