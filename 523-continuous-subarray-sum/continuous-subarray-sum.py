class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remain = {}
        rolling = 0
        remain[0] = -1

        for i in range(len(nums)):
            rolling += nums[i]

            if rolling % k in remain:
                last = remain[rolling % k]
                if i - last > 1:
                    return True
            else:
                remain[rolling % k] = i
        return False

