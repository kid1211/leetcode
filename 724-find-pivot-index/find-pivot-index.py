class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix, suffixSum
        # 2*N
        total = sum(nums)

        rolling = 0
        for i in range(len(nums)):
            if rolling == total - rolling - nums[i]:
                return i
            rolling += nums[i]

        return -1