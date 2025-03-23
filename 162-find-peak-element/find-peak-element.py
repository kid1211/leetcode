class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # if n == 1:
        #     return 0
        # elif n == 2:
        #     return 0 if nums[0] > nums[1] else 1

        while left + 1 < right:
            mid = (left + right) // 2

            if (
                mid == 0 and nums[mid] > nums[mid + 1] or
                mid == n - 1 and nums[mid] > nums[mid - 1] or
                nums[mid - 1] < nums[mid] > nums[mid + 1]
                ):
                return mid
            elif nums[mid] > nums[mid - 1]:
                left = mid 
            else:
                right = mid

        return left if nums[left] > nums[right] else right