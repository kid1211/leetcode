class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minPos = maxPos = left = -1
        res = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                left = i
            if nums[i] == minK:
                minPos = i
            if nums[i] == maxK:
                maxPos = i
            # print(minPos, maxPos, min(minPos, maxPos) - left)
            res += max(0, min(minPos, maxPos) - left)
        return res