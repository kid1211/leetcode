class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        zeros = j = 0
        res = 0

        for i in range(n):
            while j < n and (nums[j] == 1 or zeros < k):
                zeros += 1 if nums[j] == 0 else 0
                j += 1

            # if j < n:
            res = max(res, j - i)

            if nums[i] == 0:
                zeros -= 1

        return res