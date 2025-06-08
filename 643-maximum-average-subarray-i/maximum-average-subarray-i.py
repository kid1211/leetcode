class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -sys.maxsize
        avg = 0

        for i in range(k - 1):
            avg += nums[i] / k
    
        for i in range(k - 1, len(nums)):
            avg += nums[i] / k
            res = max(res, avg)
            avg -= nums[i - k + 1] / k

        return res
