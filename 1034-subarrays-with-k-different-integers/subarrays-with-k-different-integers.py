class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k):
            if k == 0:
                return 0
            unique = defaultdict(int)
            res = left = 0
            for right in range(len(nums)):
                unique[nums[right]] += 1

                while left < right and len(unique) > k:
                    unique[nums[left]] -= 1
                    if unique[nums[left]] == 0:
                        del unique[nums[left]]
                    left += 1
                res += right - left + 1
            return res
        return helper(k) - helper(k - 1)