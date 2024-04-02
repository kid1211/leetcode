class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rolling = 0
        remain = {}
        remain[0] = -1
        for i in range(len(nums)):
            rolling += nums[i]
            rolling %= k

            if rolling in remain:
                if i - remain[rolling] > 1:
                    return True
            else:
                remain[rolling] = i
        return False