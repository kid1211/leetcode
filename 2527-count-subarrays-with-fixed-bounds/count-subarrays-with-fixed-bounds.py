class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        left = minPos = maxPos = -1
        res = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                left = i
            
            if nums[i] == minK:
                minPos = i
            if nums[i] == maxK:
                maxPos = i
            
            res += max(min(minPos, maxPos) - left, 0)
        return res