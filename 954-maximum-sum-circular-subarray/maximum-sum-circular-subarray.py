class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        rolling = mini = maxi = 0
        minRes = maxRes = nums[0]

        for num in nums:
            rolling += num

            maxi = max(maxi, 0) + num
            maxRes = max(maxRes, maxi)

            mini = min(mini, 0) + num
            minRes = min(minRes, mini)
        print(maxRes, minRes, rolling)
        return max(maxRes, rolling - minRes if rolling != minRes else -sys.maxsize)
            


