class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def search(lookForFirst):
            left, right = 0, len(nums) - 1

            while left + 1 < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid
                elif nums[mid] > target:
                    right = mid
                else:
                    if lookForFirst:
                        right = mid
                    else:
                        left = mid

            if nums[left] != target and nums[right] != target:
                return -1
            elif lookForFirst:
                return left if nums[left] == target else right
            else:
                return right if nums[right] == target else left


        return [
            search(True),
            search(False)
        ]