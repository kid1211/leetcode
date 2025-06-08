class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        hasZero = False
        res = 0
        for i in range(n):
            while j < n and (nums[j] == 1 or hasZero is False):
                if nums[j] == 0:
                    hasZero = True
                j += 1
            res = max(
                res,
                j - i - 1 if hasZero else j - i - 1
            )

            if nums[i] == 0:
                hasZero = False
        return res
