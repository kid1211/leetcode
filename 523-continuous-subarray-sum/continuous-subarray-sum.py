class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remain = {}
        remain[0] = -1
        rolling = 0

        for i in range(len(nums)):
            rolling += nums[i]
            if rolling % k in remain:
                if i - remain[rolling % k] > 1:
                    return True
            else:
                remain[rolling % k] = i
        return False