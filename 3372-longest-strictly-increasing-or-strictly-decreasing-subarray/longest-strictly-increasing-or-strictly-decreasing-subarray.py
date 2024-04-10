class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        def helper1():
            res = 1
            left = 0
            for right in range(1, len(nums)):
                if nums[right] > nums[right - 1]:
                    res = max(res, right - left + 1)
                else:
                    left = right
            return res

        def helper2():
            res = 1
            left = 0
            for right in range(1, len(nums)):
                if nums[right] < nums[right - 1]:
                    res = max(res, right - left + 1)
                else:
                    left = right
            return res
        
        return max(helper1(), helper2())