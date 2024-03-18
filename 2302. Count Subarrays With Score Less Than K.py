class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        left = rolling = 0
        res = 0
        for right in range(len(nums)):
            rolling += nums[right]

            while left <= right and rolling * (right - left + 1) >= k:
                
                rolling -= nums[left]
                left += 1

            # garantee rolling * (right - left + 1) < k,
            res += (right - left + 1)
            # Q:123
            # iteration 1: 1
            # iteration 2: 12
            # iteration 2: 2
            # iteration 3: 123
            # iteration 3: 23
            # iteration 3: 3

        return res


