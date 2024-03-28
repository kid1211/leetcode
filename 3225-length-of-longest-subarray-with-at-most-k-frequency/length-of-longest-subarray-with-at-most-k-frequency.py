class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int)
        
        left = res = 0
        for right in range(len(nums)):
            frequency[nums[right]] += 1

            while left < right and frequency[nums[right]] > k:
                frequency[nums[left]] -= 1
                left += 1
    
            res = max(res, right - left + 1)
        return res


# class Solution:
#     def maxSubarrayLength(self, nums: List[int], k: int) -> int:
#         ans, start = 0, 0
#         frequency = Counter()
#         for end in range(len(nums)):
#             frequency[nums[end]] += 1
#             while frequency[nums[end]] > k:
#                 frequency[nums[start]] -= 1
#                 start += 1
#             ans = max(ans, end - start + 1)
#         return ans