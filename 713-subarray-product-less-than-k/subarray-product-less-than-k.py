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
                # print(right, left, nums[left:right + 1])
                res += (right - left + 1)
        return res