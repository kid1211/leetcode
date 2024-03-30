class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def slidingWindowAtMostK(k):
            if k == 0:
                return 0
            left = res = 0
            unique = defaultdict(int)
            for right in range(len(nums)):
                unique[nums[right]] += 1

                while left < right and len(unique) > k:
                    unique[nums[left]] -= 1
                    if unique[nums[left]] == 0:
                        del unique[nums[left]]
                    left += 1
                res += right - left + 1
            return res
        return slidingWindowAtMostK(k) - slidingWindowAtMostK(k - 1)