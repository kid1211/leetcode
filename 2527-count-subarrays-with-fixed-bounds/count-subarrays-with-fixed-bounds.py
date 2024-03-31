class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        minPos = maxPos = left = -1
        res = 0
        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                left = right
            
            if nums[right] == minK:
                minPos = right
            if nums[right] == maxK:
                maxPos = right
            
            res += max(0, min(minPos, maxPos) - left)
        return res
# 1,3,5,2,7,5
# 1
# 1 3
# 1 3 5
# 3 5
# 1 3 5 2
# 3 5 2
# 5 2
# 5