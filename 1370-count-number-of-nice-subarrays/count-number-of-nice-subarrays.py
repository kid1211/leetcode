class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def dfs(k):
            res = odd = left = 0

            for right in range(len(nums)):
                odd += nums[right] % 2

                while odd > k:
                    odd -= nums[left] % 2
                    left += 1

                res += right - left + 1
            return res
        return dfs(k) - dfs(k - 1)