class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if nums[left] <= target < nums[mid]:
                right = mid
            elif nums[mid] < target <= nums[right]:
                left = mid
            # target not in the sorted portion
            elif nums[left] >= nums[mid]:
                right = mid
            else:
                left = mid

        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
        