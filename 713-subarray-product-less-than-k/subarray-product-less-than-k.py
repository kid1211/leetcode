class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        rolling = 1
        left = res = 0
        n = len(nums)
        for right in range(n):
            rolling *= nums[right]
            while left < right and rolling >= k:
                rolling /= nums[left]
                left += 1

            if rolling < k:
                res += (right - left + 1)
        return res
# [10,5,2,6]
# k = 100
# [10]
# [10, 5]
# [5, 2]
# [5, 2, 6]