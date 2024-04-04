class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            # print(left, right, mid)

            if target == nums[mid]:
                return mid
            
            # left, target mid, right
            if nums[left] <= target < nums[mid]:
                right = mid
                continue
            elif nums[mid] < target <= nums[right]:
                left = mid
                continue
            elif nums[left] >= nums[mid]:
                right = mid
            else:
                left = mid
                # left target mid right
                # left mid target right
                # break

        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
        