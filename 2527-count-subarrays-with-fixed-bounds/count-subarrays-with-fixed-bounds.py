class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minPos = maxPos = left = -1
        res = 0

        for i in range(len(nums)):
            val = nums[i]

            if val < minK or val > maxK:
                left = i
            if val == minK:
                minPos = i
            if val == maxK:
                maxPos = i
            res += max(0, min(minPos, maxPos) - left)
        return res