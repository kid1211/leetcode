class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = cumulate = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cumulate += nums[i]
            else:
                cumulate = nums[i]
            res = max(res, cumulate)
        return res