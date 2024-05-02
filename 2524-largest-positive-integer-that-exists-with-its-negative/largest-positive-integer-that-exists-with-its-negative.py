class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if -nums[left] == nums[right]:
                return nums[right]
            elif -nums[left] < nums[right]:
                right -= 1
            else:
                left += 1
        return -1