from math import sqrt
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        @cache
        def Prime(n):
            if n <= 1:
                return False

            for i in range(2, int(sqrt(n)) + 1):
                if (n % i == 0):
                    return False
            return True
    
        left, right = 0, len(nums) - 1
        while left < right and not Prime(nums[right]):
            right -= 1
        while left < right and not Prime(nums[left]):
            left += 1
        
        if left <= right and Prime(nums[right]) and Prime(nums[left]):
            return right - left

        return 0