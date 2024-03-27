class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        maxSum = minSum = nums[0]
        totalSum = currMin = currMax = 0

        for num in nums:
            totalSum += num

            currMax = max(currMax + num, num)
            maxSum = max(maxSum, currMax)

            currMin = min(currMin + num, num)
            minSum = min(minSum, currMin)

        if totalSum == minSum:
            return maxSum
        return max(maxSum, totalSum - minSum)
