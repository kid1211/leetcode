class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = 0
        maxSum = nums[0]
        for num in nums:
            currMax = max(currMax, 0) + num
            maxSum = max(maxSum, currMax)
        return maxSum
