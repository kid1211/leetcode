class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSumSorted(left, right, target) -> [[int, int, int]]:
            res = []
            while left < right:
                if res and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if res and nums[right] == nums[right + 1]:
                    right -= 1
                    continue

                tmp = nums[left] + nums[right] + target

                if tmp == 0:
                    res += [[nums[left], nums[right], target]]
                    left += 1
                    right -= 1
                elif tmp < 0:
                    left += 1
                else:
                    right -= 1
            return res
        
        nums.sort()
        n = len(nums)
        res = []
        for i in range(len(nums)):
            if res and nums[i] == nums[i - 1]:
                continue
            res += twoSumSorted(i + 1, n - 1, nums[i])
        return res