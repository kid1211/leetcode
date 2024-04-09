class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        good = [(1, 1) for _ in range(n)]

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                good[i] = (good[i - 1][0] + 1, good[i][1])
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                good[i] = (good[i][0], good[i + 1][1] + 1)
        
        res = []
        for i in range(1, len(nums) - 1):
            if good[i - 1][0] >= k and good[i + 1][1] >= k:
                res += [i]
        return res
        